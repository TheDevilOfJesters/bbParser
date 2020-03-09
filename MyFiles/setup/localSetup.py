import os
from os import path
from pathlib import Path
from setup.jsonread import json_read
from setup.jsonread import changeJson

def setupLocalFolder(myVars):
    installDir = str(myVars['installDir'])
    if installDir.lower() == "default":
        installDir = str(Path.home())
        changeJson(installDir, "installDir")
    else:
        installDir = installDir

    print(installDir)
    createRoot(installDir, myVars)

def createRoot(installDir, vars):
    rootname = str(vars['rootName'])
    Path = installDir + "\\" + rootname
    if(os.path.exists(Path)):
        print("Root Already exists")
    else:
        os.mkdir(Path)

def createFolder(folderNames, myvars):
    if(":" in folderNames):
        folderName = cleanNameSection(folderNames, "(", "head")
        folderName = cleanNameSection(folderName, ": ", "tail")
        path = str(myvars["installDir"]) + "\\"+ str(myvars["rootName"])
        newFolder = path + "\\" + folderName
        if (os.path.exists(newFolder)):
            print(folderName + "Already exists")
        else:
            os.mkdir(newFolder)

def cleanNameSection(folderName, remove,  returnT):
    head, sep, tail = folderName.partition(remove)
    if returnT == "head":
        foldernames = head
    elif returnT == "sep":
        foldernames = sep
    else:
        foldernames = tail
    return foldernames