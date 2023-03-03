import widget, presets_widget
from presets_list import PresetsList
import sys,shutil,os
try:
    import hou
except:
    pass
from PySide2.QtWidgets import  QApplication,QWidget,QLabel,QVBoxLayout
from PySide2.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PySide2 import QtGui
import PySide2.QtGui
from PySide2.QtCore import Qt

# Convert *.uic to *.py class
# pyside2-uic .\presets_ui.ui -o .\presets_ui.py

def copyFileToHoudiniFolder(names):
    for name in names: shutil.copyfile(f"./{name}",f"C:/Users/lllde/Documents/houdini19.5/python3.9libs/{name}")

app = QApplication(sys.argv)
#widget = widget.MainWidget()
widget = presets_widget.MainWidget()
widget.show()
app.exec_()
copyFileToHoudiniFolder(["widget.py","presets_widget.py","presets_ui.py","presets_list.py","accepted_icon.png","default_icon.gif"])

# presets = PresetsList("D:/Docs/Work/Python/Projects/Presets")
# print(presets.getUsers())
# print(presets.getCategories(1))
# presets.getSetups("lllde","White water")