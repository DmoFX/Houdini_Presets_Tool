# This code is used inside of Houdini Python Panel/Add New Interface to load Presets Widget.
import presets_widget,presets_ui,presets_list
import imp
imp.reload(presets_widget)
imp.reload(presets_ui)
imp.reload(presets_list)

def onCreateInterface():
    w = presets_widget.MainWidget()
    return w
