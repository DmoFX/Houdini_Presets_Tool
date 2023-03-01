import sys,os
from presets_ui import Ui_Form
from presets_list import PresetsList,PresetsItem
from PySide2.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QDial,QTreeWidget, QTreeView,QTreeWidgetItem,QListWidgetItem,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2 import QtGui
from PySide2.QtCore import Qt,QModelIndex,QSize
from PySide2.QtGui import QMovie

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget,self).__init__()
        # self.__load_ui() # Autocompletion won't work this way.
        # self.label = self.findChild(QLabel,"label")
        # print(self.label.text())
        self.folder = "D:/Docs/Work/Python/Projects/Presets"
        self.user = os.environ.get("USERNAME")
        self.presets = PresetsList(self.folder)


        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(["User presets","Show presets","FX presets"])
        self.type = 0
        self.ui.comboBox.setCurrentIndex(self.type)
        self.ui.comboBox.currentIndexChanged.connect(self.__comboBox_clicked)
        self.__load_tree_widget()
        self.__load_list_widget()
        self.__load_label_info()

        self.ui.listWidget.itemSelectionChanged.connect(self.__listWidget_clicked)
        self.ui.tabWidget.currentChanged.connect(self.__tabWidget_clicked)
        self.ui.treeWidget.itemSelectionChanged.connect(self.__treeWidget_clicked)
        self.ui.btn_create.clicked.connect(self.__btn_create_clicked)
        self.ui.btn_load.clicked.connect(self.__btn_load_clicked)


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
        #print(self.ui.tabWidget.currentIndex(), self.ui.tabWidget.currentWidget().objectName())
    def __comboBox_clicked(self):
        self.type = self.ui.comboBox.currentIndex()
        self.__load_tree_widget()
    def __treeWidget_clicked(self):
        #print("Selected: ", self.ui.treeWidget.currentItem().text(0),self.ui.treeWidget.currentItem().parent().text(0))
        try:
            path = f"{self.ui.treeWidget.currentItem().user}/{self.ui.treeWidget.currentItem().category}/{self.ui.treeWidget.currentItem().setup}"
            print("Selected: ", path)
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
        print("btn_create: ",self.ui.lineEdit_name.text(),)
        s = self.ui.lineEdit_name.text().split("/")
        setup_category, setup_name = s[0],s[1].lower()
        unique_check = self.presets.isSetupUnigue(self.user,setup_category,setup_name)
        if len(self.ui.txtEdit_info.toPlainText())==0 or self.ui.txtEdit_info.toPlainText()=="Add description of your setup please.":
            QMessageBox.warning(self, "Attention!", "Add description of your setup please.", QMessageBox.Ok)
        else:
            if len(setup_name) > 0 and unique_check is True:
                setup_path = "{}/{}/{}".format(self.folder,self.user,self.ui.lineEdit_name.text())
                print(setup_path)
                # Add node path, check it's not empty
                # Dump data to disk.
            else:
                QMessageBox.warning(self,"Warning!","Setup name must be unique.",QMessageBox.Ok)
    def __btn_load_clicked(self):
        print("btn_load: ")
        # Create setup from data.
    def __load_label_info(self):
        movie = QMovie("D:/Docs/Work/Python/Projects/2.Houdini_Qt/default_icon.gif")
        movie.setScaledSize(QSize(300,150))
        self.ui.label_info.setMovie(movie)
        movie.start()
        # self.ui.label_info.setAlignment(Qt.AlignAbsolute)
        self.ui.label_info.setAlignment(Qt.AlignTop)




