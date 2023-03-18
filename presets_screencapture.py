import sys,os
from PySide2.QtWidgets import QMainWindow, QMenuBar, QMenu, QStatusBar
from PySide2.QtCore import *
from PySide2 import QtCore
from PySide2.QtCore import Qt,QTimer
from PySide2.QtCore import QEvent
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import QGuiApplication,QImageWriter
import numpy as np
import cv2 as cv
import time
from PIL import Image, ImageGrab
import pyautogui
import mss


class ScreenCapture(QMainWindow):
    def __init__(self,folder_path,icons_path):
        super(ScreenCapture, self).__init__()
        self.initUI()
        # Variables
        self.old_geo = self.geometry()
        self.P = self.pos()
        self.resized = 0
        self.folder_path = folder_path
        self.icons_path = icons_path
        self.screenshot_counter = 0
        self.stop_recording = False
        self.is_recording = False
        # self.setGeometry(100,0,700,500)


    def initUI(self):
        self.resize(700, 500)
        # self.setMouseTracking(True) # Tracks mouse only over the widget.
        widget = QWidget()
        # Create buttons: close, record, screenshot.
        self.btn_close = QPushButton(QIcon("./icons/close.png"), "")
        self.btn_record = QPushButton(QIcon("./icons/record.png"), "")
        self.btn_screenshot = QPushButton(QIcon("./icons/screenshot.png"), "")
        # Create signals: pressed, released, clicked.
        self.btn_close.clicked.connect(self.clicked_btn_closed)
        # Add animated gif for Record button.
        self.movie = QMovie("./icons/record_anim.gif")
        # self.movie.start()
        self.movie.frameChanged.connect(self.update_movie)
        self.btn_record.pressed.connect(self.pressed_btn_record)
        self.btn_record.released.connect(self.released_btn_record)
        self.btn_record.clicked.connect(self.clicked_btn_record)

        self.btn_screenshot.pressed.connect(self.pressed_btn_screenshot)
        self.btn_screenshot.released.connect(self.released_btn_screenshot)
        # Make buttons transparent.
        # self.btn_close.setStyleSheet("selection-color: rgb(129, 228, 255);background-color: qlineargradient(spread:pad, x1:0.915, y1:1, x2:1, y2:0, stop:0 rgba(120, 120, 120, 163), stop:1 rgba(255, 255, 255, 255));")
        self.btn_close.setStyleSheet("background: transparent;")
        self.btn_record.setStyleSheet("background: transparent;")
        self.btn_screenshot.setStyleSheet("background: transparent;")
        # Layout
        layout = QVBoxLayout()
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.btn_screenshot)
        hlayout.addWidget(self.btn_record)
        hlayout.addWidget(self.btn_close)
        hlayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        spacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)
        hlayout.addItem(spacer)
        layout.addLayout(hlayout)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # Transperent BG
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # Status bar. It creates a graping point fro resize.
        s = QStatusBar()
        self.setStatusBar(s)
        # s.showMessage("recording..")
        # t = self.addToolBar("play")

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        # Go full screen if double clicked.
        print("double")
        size = self.screen().size()
        if self.geometry().size() == size:
            self.setGeometry(self.old_geo)
        else:
            self.old_geo = self.geometry()
            self.setGeometry(QRect(0, 0, size.width(), size.height()))

    def mousePressEvent(self, event):
        print("pressed")
        self.P = event.globalPos()

    def mouseMoveEvent(self, event):
        print("move")
        print(self.resized)
        if self.resized == 0:
            delta = QPoint(event.globalPos() - self.P)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.P = event.globalPos()
        else:
            self.resized = 0
        # print(event.globalPos())

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        # print("resize")
        self.resized = 1

    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0)
        painter.setBrush(Qt.red)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.rect())
        # w = int(self.size().width())
        # h = int(self.size().height())
        # painter.drawRect(QRect(0,0,w,h))

        painter.setOpacity(1)
        # painter.setBrush(Qt.blue)
        pen = QPen(Qt.darkCyan, 5)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)
        w = int(self.size().width() * 1)
        h = int(self.size().height() * 1)
        painter.drawLines([QLine(0, 0, w, 0), QLine(w, 0, w, h), QLine(w, h, 0, h), QLine(0, h, 0, 0)])
        # print("size: ",self.size(),self.frameGeometry().size())

    def pressed_btn_record(self):
        # print("pressed")
        self.btn_record.setIcon(QIcon("./icons/record_focused1.png"))

    def released_btn_record(self):
        # print("pressed")
        self.movie.start()

    def clicked_btn_record(self):
        # print("clicked")
        if self.is_recording is False:
            self.is_recording = True  # To prevent recording from interrupting.
            # QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))
            # Create screenshots folder if not exist.
            img_folder_path = self.folder_path + "screenshots/"
            if os.path.isdir(img_folder_path) is False:
                os.makedirs(img_folder_path)
            # self.setWindowFlag(Qt.Res)
            # PIL Image.grab(x,y,x+w,y+h)
            box = (self.x(), self.y(), self.x() + self.size().width(), self.y() + self.size().height())

            # Mss screen grab: {y,x,w,h}
            # monitor = {"top": self.y(), "left": self.x(), "width": self.size().width(), "height": self.size().height()}
            # sct = mss.mss()

            screen_size = (self.size().width(),self.size().height())
            # print("box: ", monitor)
            # print("screen: ",screen_size)

            four_cc = cv.VideoWriter_fourcc(*'mp4v')
            file_name = img_folder_path+"video.mp4"
            video_output = cv.VideoWriter(file_name,four_cc,24.0,screen_size)
            img_cursor = Image.open(self.icons_path+"cursor.png")
            while True:
                # print("loop")
                # image = pyautogui.screenshot()
                # image = sct.grab(monitor)
                image = ImageGrab.grab(box)
                # Add cursor image on top of screenshot.
                cur_x, cur_y = pyautogui.position()
                # Box is in local coordinate system. So you need to subtract origin.
                cur_x = int(cur_x - self.x())
                cur_y = int(cur_y - self.y())
                image.paste(img_cursor, box=(cur_x, cur_y), mask=img_cursor)

                frame = np.array(image) # Convert image into byte array
                frame_rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
                video_output.write(frame_rgb)

                if self.stop_recording is True:
                    # print("end")
                    # self.video_output.release()
                    break
                key = cv.waitKey(1)  # Without this loop will be infinite.
            video_output.release()

    def pixmapToArray(self,pixmap:QPixmap):
        ## Get the size of the current pixmap
        size = pixmap.size()
        h = size.width()
        w = size.height()

        ## Get the QImage Item and convert it to a byte string
        qimg = pixmap.toImage()
        byte_str = qimg.bits().tobytes()

        ## Using the np.frombuffer function to convert the byte string into an np array
        img = np.frombuffer(byte_str, dtype=np.uint8).reshape((w, h, 4))

        return img
    def update_movie(self):
        # Update Record GIF Icon
        self.btn_record.setIcon(QIcon(self.movie.currentPixmap()))
        self.movie.setScaledSize(QSize(205, 178))
        # self.movie.start()

    def pressed_btn_screenshot(self):
        self.btn_screenshot.setIcon(QIcon("./icons/screenshot_focused1.png"))
        # print("Clicked screenshot.")
        # Create screenshots folder if not exist.
        img_folder_path = self.folder_path+"screenshots/"
        if os.path.isdir(img_folder_path) is False:
            os.makedirs(img_folder_path)
        file_name = img_folder_path+f"img_{self.screenshot_counter}.png"
        self.hide()
        # # Create screenshot using Qt
        # x,y,w,h = (self.x(),self.y(),self.size().width(),self.size().height())
        # # screen = QGuiApplication.primaryScreen()
        # screen = self.screen()
        # pxmap = screen.grabWindow(0,x,y,w,h)
        # img_writer = QImageWriter(file_name)
        # img_writer.write(pxmap.toImage())

        # Create screenshot using PIL
        box = (self.x(), self.y(), self.x()+self.size().width(), self.y()+self.size().height())
        image = ImageGrab.grab(box)
        # Add cursor image on top of screenshot.
        img_cursor = Image.open(self.icons_path+"cursor.png")
        cur_x, cur_y = pyautogui.position()
        # Box is in local coordinate system. So you need to subtract origin.
        cur_x = int(cur_x-self.x())
        cur_y = int(cur_y-self.y())
        image.paste(img_cursor, box=(cur_x, cur_y), mask=img_cursor)

        image = np.array(image)
        image = Image.fromarray(image)
        image.save(file_name)

        self.screenshot_counter += 1
        self.show()

    def released_btn_screenshot(self):
        self.btn_screenshot.setIcon(QIcon("./icons/screenshot.png"))

    def clicked_btn_closed(self):
        self.btn_close.setIcon(QIcon("./icons/close_focused.png"))
        self.stop_recording = True
        QTimer.singleShot(100,self.delayed_exit)

    def delayed_exit(self):
        self.close()



