import sys,os
from presets_ui import Ui_Form
from presets_list import PresetsList,PresetsItem
from PySide2.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QDial,QTreeWidget, QTreeView,QTreeWidgetItem,QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2 import QtGui
from PySide2.QtCore import Qt,QModelIndex

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget,self).__init__()
        # self.__load_ui() # Autocompletion won't work this way.
        # self.label = self.findChild(QLabel,"label")
        # print(self.label.text())
        self.presets = PresetsList("D:/Docs/Work/Python/Projects/Presets")

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(["User presets","Show presets","FX presets"])
        self.type = 0
        self.ui.comboBox.setCurrentIndex(self.type)
        self.ui.comboBox.currentIndexChanged.connect(self.__comboBox_clicked)
        self.__load_tree_widget()
        self.__load_list_widget()

        self.ui.listWidget.itemSelectionChanged.connect(self.__listWidget_clicked)
        self.ui.tabWidget.currentChanged.connect(self.__tabWidget_clicked)
        self.ui.treeWidget.itemSelectionChanged.connect(self.__treeWidget_clicked)


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
        # tree_widget_item2 = QTreeWidgetItem(["Water"])
        # self.ui.treeWidget.addTopLevelItem(tree_widget_item2)
        # tree_widget_item2.addChild(QTreeWidgetItem(["white water"]))
        self.ui.treeWidget.clear()
        categories = self.presets.getCategories(self.type)
        users = self.presets.getUsers()
        if self.type == 0:
            for user in users:
                if user == os.environ.get("USERNAME"):
                    #print(f"{user}")
                    for category in categories:
                        # item = QTreeWidgetItem([category])
                        item = PresetsItem([category],category,user)
                        self.ui.treeWidget.addTopLevelItem(item)
                        for setup in self.presets.getSetups(user,category):
                            #item.addChild(QTreeWidgetItem([setup]))
                            item.addChild(PresetsItem([setup],category,user,setup))
        # choice = 0
        # if self.type == 0:
        #     users = self.presets.getUsers()
        #     os.environ.get("USERNAME")
        # elif self.type == 1:
        #     users = self.presets.getUsers()
        print(categories)
        #print(self.presets.getUsers())

    def __load_list_widget(self):
        #categories = ["category_"+str(s) for s in range(30)]
        self.ui.listWidget.clear()
        categories = self.presets.getCategories(self.ui.comboBox.currentIndex())
        for category in categories:
            self.ui.listWidget.addItem(QListWidgetItem(category))
        self.ui.listWidget.setCurrentRow(0)
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
        path = f"{self.ui.treeWidget.currentItem().user}/{self.ui.treeWidget.currentItem().category}/{self.ui.treeWidget.currentItem().setup}"
        print("Selected: ", path)




