import sys,os
from PySide2.QtWidgets import QTreeWidgetItem

class PresetsList():
    def __init__(self,dir_path=str):
        self.dir_path = dir_path
        self.data_structure = self.updateData()
        self.show_users = self.getShowUsers()

    def updateData(self):
        user_list = os.listdir(self.dir_path)
        data_structure = {}
        for user in user_list:
            category_list = os.listdir(self.dir_path+"/"+user)
            # print(f"{user}: {category_list}")
            cat_list = []
            for category in category_list:
                setups = os.listdir(self.dir_path+"/"+user+"/"+category)
                # print(f"{user}: {category} : {setups}")
                cat_list.append([category,setups])
            data_structure[user] = cat_list
        #print(data_structure)
        return data_structure
    def getUsers(self):
        return list(self.data_structure.keys())
    def getCategories(self,type=0):
        cat_list = set()
        if type == 0:
            # Current USER categories.
            for key in list(self.data_structure.keys()):
                if key == os.environ.get("USERNAME"):
                    [cat_list.add(f[0]) for f in self.data_structure[key]]
                    #print(values)
        elif type == 1:
            # Only SHOW users categories.
            for key in list(self.data_structure.keys()):
                for user in self.show_users:
                    if key == user:
                        [cat_list.add(f[0]) for f in self.data_structure[key]]
        elif type == 2:
            # All FX categories.
            for key in self.data_structure.keys():
                values = [f[0] for f in self.data_structure[key]]
                # print(values)
                [cat_list.add(value) for value in values]
        return cat_list
    def getShowUsers(self):
        return ["yrudakov"]
    def getSetups(self,user,category):
        setups = []
        #s = self.data_structure[user]
        #print(s)
        try:
            setups = [f[1] for f in self.data_structure[user] if f[0] == category][0]
        except:
            pass
        #print(setups)
        return setups


class PresetsItem(QTreeWidgetItem):
    def __init__(self,list=[],category="",user="",setup=""):
        super().__init__(list)
        self.category = category
        self.user = user
        self.setup = setup

    def setPresetsCategory(self, category):
        self.category = category
    def getPresetsUser(self):
        return self.user