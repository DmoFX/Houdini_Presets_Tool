import sys,os,json,io
from PySide2.QtWidgets import QTreeWidgetItem
try:
    import hou, toolutils
except:
    pass

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
                if os.path.isdir(self.dir_path+"/"+user+"/"+category):
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
        return ["yrudakov","zyong"]
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
    def isSetupUnigue(self,user_in,category_in,setup_in):
        # print(self.data_structure[user_in])
        #print(self.getCategories(2))
        # print(self.getSetups(user_in,category_in))
        result = False
        setups = self.getSetups(user_in,category_in)
        if len(setups) == 0:
            result = True
        else:
            for setup in setups:
                if setup == setup_in:
                    # print(setup)
                    result = False
                    break
                else:
                    result = True
        # print(result)
        return result
    def writeSetupAsCode(self,setup_path,node_path,setup_description):
        if os.path.isdir(setup_path) is False:
            os.makedirs(setup_path)
        file_path = setup_path+"/setup.cmd"
        print("witeSetupAsCode: ",file_path,"\n  node: ",node_path)
        cmd = "opscript -G -r " + node_path + " > " + file_path
        # print("witeSetupAsCode: ",cmd)
        hou.hscript(cmd)
        # Modify cmd file to wrap it into subnet

        # Write addiditional data into info.json
        print("-----------------  witeSetupAsCode ----------:  ")
        # In case you pass multiple nodes "/obj/geo/sphere /obj/geo/grid", take only first to get their parents
        if node_path.find(" ") > 0:
            node_path = node_path.split(" ")[0]
        list = self.__getParentsList(node_path)

        dic = {"node_path": node_path, "description": setup_description,"list":list,"type":hou.node(node_path).type().name()}
        with open(setup_path+"/info.json",'w') as f:
            json.dump(dic,f)
    def readSetupAsCode(self,setup_path):
        # Read data from json file
        with open(setup_path+"/info.json") as f:
            data = json.load(f)
        print("------------- readSetupAsCode ------------: \n",data)
        node_path = data["node_path"]
        setup_description = data["description"]
        list = data["list"]
        # Recreate original parents based on node_path if they don't exist yet.
        is_exist = self.__createParentNodes(node_path,list)
        # Replace parent nodes name if parent node is already exist.
        if is_exist is True:
            self.__replaceParentNodes(node_path,list,setup_path,data["type"])
        else:
            # Read nodes from file.
            print("....... create setup if empty ..........")
            file_path = setup_path + "/setup.cmd"
            rcmd = "cmdread " + file_path
            hou.hscript(rcmd)
        # Set current Viewport and Network View to the setup
        self.__setCurrentView(node_path)
        return setup_description
    # def __createSubnet(self,node_path,list):
    #     exist = 0
    #     for n in parent.children():
    #         if (n.type() == hou.nodeType(hou.objNodeTypeCategory(), "geo")):
    #             if n.name() == "circle_object1":
    #             exist = 1

    def __createParentNodes(self,node_path,list):
        # Go over parents tuple data and create nodes if they don't exist yet.
        is_exist = False
        for data in list:
            is_exist = False
            path = data[0]
            print("---------------", path, "----------")
            try:
                p = hou.node(path).name()
                is_exist = True
                print("try: ", is_exist)
            except:
                is_exist = False
                print("except: ", is_exist)
                pass
            if is_exist is False:
                path = data[0].strip(data[2])
                n = hou.node(path).createNode(data[1], data[2])
        return is_exist
    def __replaceParentNodes(self,node_path,list,setup_path,type):
        print("------------- replaceParentNodes ------------: \n")
        num = len(list) - 1
        parent_node = list[num][0]
        print("Old parent:", parent_node)
        # tmp_parent_node = parent_node + "/__setup_unique__"
        tmp_parent_node = parent_node + "/{}_unique__".format(list[num][2])
        print("New parent:",tmp_parent_node)
        print(setup_path + "/setup.cmd")
        # Create new parent Node.

        node = hou.node(parent_node).createNode(type,"{}_unique__".format(list[num][2]))
        node.setColor(hou.Color(0.384, 0.184, 0.329))
        print(node.path())
        # Read and modify cmd file. Create a new one with new parent node to be sure it's empty.
        with open(setup_path + "/setup.cmd") as f:
            txt = f.read()
        # print(txt)
        txt = txt.replace("opcf " + parent_node, "opcf " + tmp_parent_node)
        # print(txt)
        with open(setup_path + "/setup_unique.cmd", 'w') as f:
            f.write(txt)

        file_path = setup_path + "/setup_unique.cmd"
        rcmd = "cmdread " + file_path
        hou.hscript(rcmd)


    def __getParentsList(self,node_path):
        # n = hou.node(node_path)
        path = node_path
        list = []
        while path > "/":
            n = hou.node(path)
            list.append((n.parent().path(), n.parent().type().name(), n.parent().name()))
            path = n.parent().path()
            # print(path)
        # Remove / and /obj paths
        print(list)
        # list.pop()
        list.pop()
        list.reverse()
        print(list)
        return list
    def __setCurrentView(self,node_path):
        n = hou.node(node_path)
        # print(n)
        scene_viewer = toolutils.sceneViewer()
        scene_viewer.cd(n.parent().path())
        network_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        network_editor.cd(n.parent().path())
        # print("NE: ", n.parent().path(), network_editor, "  SV:  ", scene_viewer)
        n.setDisplayFlag(1)
        n.setCurrent(True)
        # scene_viewer.setCurrentNode(n)





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