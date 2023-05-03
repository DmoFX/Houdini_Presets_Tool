
# Houdini Presets Tool.
This tool provides and easy way to store and keep availible any setups you are considering usefull and would like to access them any time in convinient manner. You can drag and drop your setups on any level like Sops, Obj etc, choose a category and name, add discription and create screenshots and video record your screen for best representation of what you've done.

Made in **PyCharm, PySide2, Python 3.9, Houdini 19.5.534**. Installation requires addiditional Python libraries as **pyautogui, Pillow, OpenCV, mss** to be availible through PYTHONPATH if you would like to have access to screencapture features.
## Video preview.
![Screenshot](screenshots/video.gif)

## Screenshots.
### Loading setup interface.
![Screenshot](screenshots/img_0.jpg)
### Adding setup to your library.
![Screenshot](screenshots/img_1.jpg)
### Compiled Qt widgets look.
![Screenshot](screenshots/img_2.jpg)
### Structured data folder.
You will need to modify presets_widget.py to choose your own folder for storing all data structure. <br />
self.folder = "D:/Docs/Work/Python/Projects/Presets" <br />
Data structure looks like: Presets_folder/User_folders/Category_folders/Setup_folders/Setup_folder/Screenshots_folder
![Screenshot](screenshots/img_3.jpg)
### Filter setups and Remove features.
![Screenshot](screenshots/img_5.jpg)

## Install.
1. git clone https://github.com/DmoFX/Houdini_Presets_Tool.git .
2. Go to your houdini home directory and create new folder based on your Houdini Python version. I have Houdini 19.5.534 and Python 3.9, so I created  python3.9libs folder. <br />
You can check Python version in Houdini Help/About/Show Details. <br />
**Minimum Python requirements: 3+.** 2.7 will produce some Errors.
"C:/Users/lllde/Documents/houdini19.5/python3.9libs/"
3. Copy python files and icons folder into this directory.
![Screenshot](screenshots/img_7.jpg)
4. Open presets_widget.py and modify next paths: <br />
 ------------------------  UPDATE  THIS INFO  ------------------------------ <br />
        self.libs_path = "C:/Users/lllde/Documents/houdini19.5/python3.9libs/"  # Path is used to load icons. <br />
        self.folder = "D:/Docs/Work/Python/Projects/Presets"  # Path is used to store presets data on disk. <br />
        self.vlc_path = "C:/Program Files/VideoLAN/VLC/vlc.exe"  # Direct path to VLC video launcher. <br />
  --------------------------------------------------------------------------- <br />
5. In Houdini open Python Panel/New Interface and copy/paste a code from houdini_panel.py. Save it.
6. At this point Presets Tool should work except screen capture features as we didn't install additional Python libraries yet.
7. So now we have to create Python virtual environment and install libs. <br />
![Screenshot](screenshots/img_8.jpg)
![Screenshot](screenshots/img_4.jpg)
![Screenshot](screenshots/img_6.jpg)

I would highly recommend to watch this video tutorial by Corey Schafer which explain the best how virtual environment works.  <br />
[![IMAGE ALT TEXT HERE](screenshots/img_9.jpg)](https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer)
8. Now Houdini should see all additional Python modules and screen capture should work.



