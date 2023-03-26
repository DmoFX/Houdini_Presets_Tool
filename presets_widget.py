import sys,os,time,re
from presets_ui import Ui_Form
from presets_list import PresetsList,PresetsItem
from presets_screencapture import ScreenCapture
from PySide2.QtWidgets import QApplication,QMainWindow,QDialog,QWidget,QLabel,QVBoxLayout,QPushButton,QDial,QTreeWidget, QTreeView,QTreeWidgetItem,QListWidgetItem,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile,QTimer,QThreadPool,QRunnable,Signal
from PySide2 import QtGui
from PySide2.QtCore import Qt,QModelIndex,QSize,QEvent,QObject
from PySide2.QtGui import QMovie,QPixmap,QImage,QMouseEvent,QIcon
try:
    import hou
except:
    pass

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget,self).__init__()
        self.setAcceptDrops(True)
        # self.__load_ui() # Autocompletion won't work this way.
        # self.label = self.findChild(QLabel,"label")
        # print(self.label.text())
        self.libs_path = "C:/Users/lllde/Documents/houdini19.5/python3.9libs/"
        self.folder = "D:/Docs/Work/Python/Projects/Presets"
        self.user = os.environ.get("USERNAME")
        self.presets = PresetsList(self.folder)
        self.node_path = ""
        self.selected_setup = ""


        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(["User presets","Show presets","FX presets"])
        self.type = 0
        self.ui.comboBox.setCurrentIndex(self.type)
        self.ui.comboBox.currentIndexChanged.connect(self.__comboBox_clicked)
        self.__load_tree_widget()
        self.__load_list_widget()
        self.__load_label_info()
        self.__load_label_screenshots()
        self.__load_label_username()

        self.ui.listWidget.itemSelectionChanged.connect(self.__listWidget_clicked)
        self.ui.tabWidget.currentChanged.connect(self.__tabWidget_clicked)
        self.ui.treeWidget.itemSelectionChanged.connect(self.__treeWidget_clicked)
        self.ui.btn_create.clicked.connect(self.__btn_create_clicked)
        self.ui.btn_load.clicked.connect(self.__btn_load_clicked)
        self.ui.btn_r_record.clicked.connect(self.__btn_r_record_clicked)
        self.ui.btn_r_next.clicked.connect(self.__btn_r_next_clicked)
        self.ui.btn_r_back.clicked.connect(self.__btn_r_back_clicked)
        self.ui.btn_l_next.clicked.connect(self.__btn_l_next_clicked)
        self.ui.btn_l_back.clicked.connect(self.__btn_l_back_clicked)

        self.screenshot_img = ""
        self.load_screenshot_img = ""
        # Install Event Filter to preview screenshots in a larger window.
        self.ui.label_record.installEventFilter(self)
        self.ui.label_screenshots.installEventFilter(self)
        self.ui.label_record.setMouseTracking(True)
        self.ui.label_screenshots.setAlignment(Qt.AlignTop)

        self.ui.btn_l_next.setIcon(QIcon(f"{self.libs_path}icons/next_icon.png"))
        self.ui.btn_r_next.setIcon(QIcon(f"{self.libs_path}icons/next_icon.png"))
        self.ui.btn_l_back.setIcon(QIcon(f"{self.libs_path}icons/back_icon.png"))
        self.ui.btn_r_back.setIcon(QIcon(f"{self.libs_path}icons/back_icon.png"))
        self.ui.btn_r_record.setIcon(QIcon(f"{self.libs_path}icons/record_video.png"))
        self.ui.btn_r_show.setIcon(QIcon(f"{self.libs_path}icons/play_icon.png"))
        self.ui.btn_l_show.setIcon(QIcon(f"{self.libs_path}icons/play_icon.png"))

    # Load *.ui file as user interface. Autocompletion is not supported this way.
    # def __load_ui(self):
    #     loader = QUiLoader()
    #     path = os.path.join(os.path.dirname(__file__), "presets_ui.ui")
    #     print(path)
    #     ui_file = QFile(path)
    #     ui_file.open(QFile.ReadOnly)
    #     loader.load(ui_file, self)
    #     ui_file.close()
    def __load_tree_widget(self):
        #self.ui.treeWidget.setHeaderLabels(["Presets"])
        #self.ui.treeWidget.setHeaderLabels(["presets","user"])
        self.ui.treeWidget.setHeaderHidden(True)
        # tree_widget_item1 = QTreeWidgetItem(["Destruction"])
        # self.ui.treeWidget.addTopLevelItem(tree_widget_item1)
        # tree_widget_item1.addChild(QTreeWidgetItem(["rbd_setup"]))
        self.ui.treeWidget.clear()
        categories = self.presets.getCategories(self.type)
        users = self.presets.getUsers()
        # print("-------------------")
        if self.type == 0:
            #print(f"{self.user}")
            self.__createTreeWidgetItems([self.user], categories)
        elif self.type == 1:
            users = self.presets.getShowUsers()
            #print("show_users:",users)
            self.__createTreeWidgetItems(users,categories)
        elif self.type == 2:
            users = self.presets.getUsers()
            self.__createTreeWidgetItems(users,categories)
        #print(categories)

    def __load_list_widget(self):
        #categories = ["category_"+str(s) for s in range(30)]
        self.ui.listWidget.clear()
        categories = self.presets.getCategories(2)
        for category in categories:
            self.ui.listWidget.addItem(QListWidgetItem(category))
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget.sortItems(Qt.AscendingOrder)
        self.ui.lineEdit_name.setText(f"{self.ui.listWidget.currentItem().text()}/")

    # Return name of the category in the listWidget
    def __listWidget_clicked(self):
        #index = self.ui.listWidget.currentIndex()
        #print(self.ui.listWidget.currentItem().text())
        category = self.ui.listWidget.currentItem().text()
        txt = self.ui.lineEdit_name.text()
        s = txt.split("/")
        name = s[1] if len(s)>1 else ""
        self.ui.lineEdit_name.setText(f"{category}/{name}")

    # Update listWidget every time tab is changed
    def __tabWidget_clicked(self):
        if self.ui.tabWidget.currentIndex() == 1:
            self.__load_list_widget()
        else:
            self.presets = PresetsList(self.folder)
            self.__load_tree_widget()
        #print(self.ui.tabWidget.currentIndex(), self.ui.tabWidget.currentWidget().objectName())
    def __comboBox_clicked(self):
        self.type = self.ui.comboBox.currentIndex()
        self.__load_tree_widget()
    def __treeWidget_clicked(self):
        print("Tree Widget clicked.")
        #print("Selected: ", self.ui.treeWidget.currentItem().text(0),self.ui.treeWidget.currentItem().parent().text(0))
        try:
            self.selected_setup = f"{self.ui.treeWidget.currentItem().user}/{self.ui.treeWidget.currentItem().category}/{self.ui.treeWidget.currentItem().setup}"
            print("Selected: ", self.selected_setup)
            self.__load_label_info()
            self.__load_label_username()
            self.__load_label_screenshots()
            # if len(self.ui.treeWidget.currentItem().setup)>0:
            #     self.ui.label_username.setText("user: {}.".format(self.ui.treeWidget.currentItem().user))
            # else:
            #     self.ui.label_username.setText("")
        except:
            pass

    def __createTreeWidgetItems(self,users,categories):
        for category in categories:
            # item = QTreeWidgetItem([category])
            item = PresetsItem([category], category, "FX")
            # print(f"FX:     {category}")
            self.ui.treeWidget.addTopLevelItem(item)
            for user in users:
                # print(f"FX: {user}", categories)
                for setup in self.presets.getSetups(user, category):
                    # item.addChild(QTreeWidgetItem([setup]))
                    item.addChild(PresetsItem([setup], category, user, setup))
            self.ui.treeWidget.sortItems(0,Qt.AscendingOrder)
    def __btn_create_clicked(self):
        # print("btn_create: ",self.ui.lineEdit_name.text(),)
        if len(self.ui.txtEdit_info.toPlainText())==0 or self.ui.txtEdit_info.toPlainText()=="Add description of your setup please.":
            QMessageBox.warning(self, "Attention!", "Add description of your setup please.", QMessageBox.Ok)
        else:
            if self.__lineEdit_name_check() is True:
                setup_path = "{}/{}/{}".format(self.folder,self.user,self.ui.lineEdit_name.text())
                self.presets.writeSetupAsCode(setup_path,self.node_path,self.ui.txtEdit_info.toPlainText())
                # print(setup_path)
                self.ui.label_drop.setText("Drop your preset here.")
            else:
                QMessageBox.warning(self,"Warning!","Setup name must be unique.\n"
                                                    "Drag and drop your setup into the slot.",QMessageBox.Ok)
    def __btn_load_clicked(self):
        print("btn_load: ")
        # Create setup from data.
        s = self.selected_setup.split("/")
        if len(s)==3 and len(s[2])>0:
            setup_path = self.folder+"/"+self.selected_setup
            print("btn_load: ", self.selected_setup,setup_path)
            description = self.presets.readSetupAsCode(setup_path)
            self.ui.label_info.setText(description)
        else:
            QMessageBox.warning(self,"Warning!","Select a setup from the list please.",QMessageBox.Ok)

    def __load_label_username(self):
        try:
            if len(self.ui.treeWidget.currentItem().setup) > 0:
                self.ui.label_username.setText("user: {}.".format(self.ui.treeWidget.currentItem().user))
            else:
                self.ui.label_username.setText("user: ")
        except:
            pass
    def __load_label_info(self):
        # print("load info")
        setup_path = self.folder + "/" + self.selected_setup
        # Check if user selected setup in the treeWidget
        s = self.selected_setup.split("/")
        if len(s)==3 and len(s[2])>0:
            setup_description = self.presets.getSetupDescription(setup_path)
            self.ui.label_info.setText(setup_description)
            self.ui.label_info.setAlignment(Qt.AlignTop)
        else:
            self.ui.label_info.setText("Preset Information")
            self.ui.label_info.setAlignment(Qt.AlignCenter)
    def __load_label_screenshots(self):
        self.load_default_gif()

    def dragEnterEvent(self, event):
        # print("dragEnter")
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            # print("dropEvent")
            # print(event.mimeData().hasText(), event.mimeData())
            event.setDropAction(Qt.DropAction.CopyAction)
            self.node_path = event.mimeData().text()
            print("dropEvent: ", self.node_path)
            print("dropEvent: ", self.node_path.split("\t"))
            s = self.node_path.split("\t")
            if len(s)>1:
                self.node_path = " ".join(s)
                print("join",len(s),s)
            print("dropEvent: ", self.node_path,len(self.node_path))
            if len(self.node_path)>0:
                try:
                    # node = hou.node(self.node_path)
                    # node.setColor(hou.Color(0.384, 0.184, 0.329))
                    pxmap = QPixmap("{}icons/accepted_icon.png".format(self.libs_path)).scaled(100,100)
                    self.ui.label_drop.setPixmap(pxmap)
                    print("adding texture")
                    QTimer.singleShot(2000, self.__label_drop_change_text)
                except:
                    pass
                event.accept()
                # time.sleep(3)
                # self.ui.label_drop.setText("Setup is accepted. Path: {}".format(self.node_path))
        else:
            event.ignore()
    def __label_drop_change_text(self):
        self.ui.label_drop.setText("Setup is accepted.\n\n      Path: {}".format(self.node_path))

    def __btn_r_record_clicked(self):
        # print("btn_r_record clicked.")
        if self.__lineEdit_name_check() is True:
            folder_path = "{}/{}/{}/".format(self.folder, self.user, self.ui.lineEdit_name.text())
            icons_path = f"{self.libs_path}icons/"
            # Create the ScreenCapture main window
            self.record_dialog = ScreenCapture(folder_path, icons_path)
            self.record_dialog.show()

            # Receive custom Signal from ScreenCapture class. Set QLabel with screenshot icon.
            self.record_dialog.result.connect(self.label_record_setIcon)
        else:
            QMessageBox.warning(self, "Warning!", "Setup name must be unique and final before recording.\n"
                                                  "Drag and drop your setup into the slot.",QMessageBox.Ok)
    def label_record_setIcon(self,img_path):
        # Receiving signal from ScreenCapture and setting QLabel with QIcon(img_path)
        print("label_record, signal: ",img_path)
        if len(img_path)>0 and os.path.isfile(img_path) is True:
            pxmap = self.__scaled_pxmap(img_path,350)
            self.ui.label_record.setPixmap(pxmap)
            self.screenshot_img = img_path
        self.ui.lineEdit_name.setDisabled(True)
    def __lineEdit_name_check(self):
        s = self.ui.lineEdit_name.text().split("/")
        setup_category, setup_name = s[0], s[1].lower()
        unique_check = self.presets.isSetupUnigue(self.user, setup_category, setup_name)
        result = False
        if len(setup_name) > 0 and unique_check is True and len(self.node_path) > 0:
            result = True
        return result

    def __scaled_pxmap(self,img_path,width):
        pxmap = QPixmap(img_path)
        w = pxmap.size().width()
        h = pxmap.size().height()
        ratio = h/w
        pxmap = QPixmap(img_path).scaled(width,int(width*ratio))
        return pxmap
    def __btn_r_next_clicked(self):
        print("btn_r_Next")
        self.r_icon_change("next")
    def __btn_r_back_clicked(self):
        print("btn_r_Back")
        self.r_icon_change("back")
    def r_icon_change(self,choice="next"):
        # print("----------- r_icon_change ----------")
        if self.__lineEdit_name_check() is True:
            folder_path = "{}/{}/{}/".format(self.folder, self.user, self.ui.lineEdit_name.text())
            # print(self.screenshot_img)
            s = re.findall(r'\d+', self.screenshot_img)  # Returns list of numbers in a string: [0,5,3]
            num = s[len(s) - 1]
            # Based on choice will be Next or Back image
            val = 1 if choice=="next" else -1
            num_next = int(num) + val if int(num) + val > 0 else 0 # clamp below 0
            # print("num: ", num, num_next)
            count = self.get_screenshot_count(f"{folder_path}screenshots/") -1
            num_next = num_next if num_next < count else count  # clamp above max
            next_img = folder_path + f"screenshots/img_{num_next}.png"
            # print(next_img)
            if os.path.isfile(next_img) is True:
                pxmap = self.__scaled_pxmap(next_img, 350)
                self.ui.label_record.setPixmap(pxmap)
                self.screenshot_img = next_img
    def eventFilter(self, src:QObject, e:QEvent):
        if e.type()==QEvent.MouseButtonDblClick and src is self.ui.label_record:
            print("double clicked on label_record")
            self.preview_full_size_icon(self.screenshot_img)
        if e.type()==QEvent.MouseButtonDblClick and src is self.ui.label_screenshots:
            print("double clicked on label_screenshots")
            self.preview_full_size_icon(self.load_screenshot_img)
        return super(MainWidget,self).eventFilter(src,e)
    def preview_full_size_icon(self,img_path):
        if os.path.isfile(img_path) is True:
            print(img_path)
            # Create simple Dialog to preview image in full resolution.
            pxmap = QPixmap(img_path)
            x, y = (pxmap.size().width(), pxmap.size().height())
            self.preview = QDialog()
            self.preview.resize(x, y)
            self.preview.setWindowTitle("Screenshot Preview")
            self.preview.setWindowFlag(Qt.WindowStaysOnTopHint, True)
            self.preview.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
            label = QLabel()
            label.setPixmap(pxmap)
            layout = QVBoxLayout()
            layout.addWidget(label)
            self.preview.setLayout(layout)
            self.preview.show()
    def get_screenshot_count(sel,path):
        # print("----------- get_screenshot_count ----------")
        count = 0
        for f in os.listdir(path):
            if f.endswith(".png"):
                count +=1
        # print("total count: ",count)
        return count

    def __load_label_screenshots(self):
        print("----------- __load_label_screenshots ----------")
        setup_path = self.folder + "/" + self.selected_setup
        if self.treeWidget_selected_setup_check() is True:
            self.load_screenshot_img = setup_path + f"/screenshots/img_0.png"
            if os.path.isfile(self.load_screenshot_img) is True:
                print("Yes: ",self.load_screenshot_img)
                pxmap = self.__scaled_pxmap(self.load_screenshot_img, 300)
                self.ui.label_screenshots.setPixmap(pxmap)
        else:
            print("No: ","{}icons/default_icon.gif".format(self.libs_path))
            self.load_default_gif()
    def load_default_gif(self):
        movie = QMovie("{}icons/default_icon.gif".format(self.libs_path))
        movie.setScaledSize(QSize(300, 150))
        self.ui.label_screenshots.setMovie(movie)
        movie.start()
        # self.ui.label_screenshots.setAlignment(Qt.AlignAbsolute)
        # self.ui.label_screenshots.setAlignment(Qt.AlignTop)
    def treeWidget_selected_setup_check(self):
        # Check if user selected setup in the treeWidget
        result = False
        s = self.selected_setup.split("/")
        if len(s) == 3 and len(s[2]) > 0:
            result = True
        return result
    def __btn_l_next_clicked(self):
        print("----------- __btn_l_next_clicked ----------")
        self.l_icon_change("next")
    def __btn_l_back_clicked(self):
        print("----------- __btn_l_back_clicked ----------")
        self.l_icon_change("back")
    def l_icon_change(self,choice="next"):
        folder_path = self.folder + "/" + self.selected_setup+"/"
        if self.treeWidget_selected_setup_check() and os.path.isfile(self.load_screenshot_img):
            # img_path = setup_path + f"/screenshots/img_0.png"
            print("current img_path: ",self.load_screenshot_img)
            s = re.findall(r'\d+', self.load_screenshot_img)  # Returns list of numbers in a string: [0,5,3]
            num = s[len(s) - 1]
            # Based on choice will be Next or Back image
            val = 1 if choice == "next" else -1
            num_next = int(num) + val if int(num) + val > 0 else 0  # clamp below 0
            # print("num: ", num, num_next)
            count = self.get_screenshot_count(f"{folder_path}screenshots/") - 1
            num_next = num_next if num_next < count else count  # clamp above max
            next_img = folder_path + f"screenshots/img_{num_next}.png"
            # print(next_img)
            if os.path.isfile(next_img) is True:
                pxmap = self.__scaled_pxmap(next_img, 300)
                self.ui.label_screenshots.setPixmap(pxmap)
                self.load_screenshot_img = next_img










