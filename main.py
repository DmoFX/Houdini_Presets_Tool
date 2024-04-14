import presets_widget
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
    # for name in names: shutil.copyfile(f"./{name}",f"C:/Users/lllde/Documents/houdini19.5/python3.9libs/{name}")
    # Libs path should be the same Python version your current Houdini is using. Check Help/Houdini Info.
    libs_path = "C:/Users/lllde/Documents/houdini19.5/python3.9libs/"
    libs_path = "C:/Users/lllde/OneDrive/Documents/houdini20.0/python3.10libs/"
    if os.path.isdir(libs_path+"icons") is False:
        os.makedirs(libs_path+"icons")
    for name in names: shutil.copyfile(f"./{name}", f"{libs_path}{name}")

app = QApplication(sys.argv)
#widget = widget.MainWidget()
widget = presets_widget.MainWidget()
widget.show()
app.exec_()
copyFileToHoudiniFolder(["presets_widget.py","presets_ui.py","presets_list.py","presets_screencapture.py",
                         "icons/accepted_icon.png","icons/close.png","icons/close_focused.png","icons/cursor.png",
                         "icons/default_icon.gif","icons/record.png","icons/record_anim.gif","icons/record_focused1.png",
                         "icons/screenshot.png","icons/screenshot_focused1.png","icons/next_icon.png","icons/back_icon.png",
                         "icons/record_video.png","icons/play_icon.png"])

# Test for PresetsList
# presets = PresetsList("D:/Docs/Work/Python/Projects/Presets")
# print(presets.getUsers())
# print(presets.getCategories(1))
# presets.getSetups("lllde","White water")