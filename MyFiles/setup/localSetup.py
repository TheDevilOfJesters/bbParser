import os
from pathlib import Path
from setup.jsonread import changeJson


def setup_local_folder(my_vars):
    install_dir = str(my_vars['installDir'])
    if install_dir.lower() == "default":
        install_dir = str(Path.home())
        changeJson(install_dir, "installDir")
    else:
        install_dir = install_dir

    print(install_dir)
    create_root(install_dir, my_vars)


def create_root(install_dir, my_vars):
    root_name = str(my_vars['rootName'])
    root_path = install_dir + "\\" + root_name
    if os.path.exists(root_path):
        print("Root Already exists")
    else:
        os.mkdir(root_path)


def create_folder(new_folder_name, my_vars):
    if ":" in new_folder_name:
        folder_name = clean_name_section(new_folder_name, "(", "head")
        folder_name = clean_name_section(folder_name, ": ", "tail")
        path = str(my_vars["installDir"]) + "\\" + str(my_vars["rootName"])
        folder_name = path + "\\" + folder_name
        if os.path.exists(folder_name):
            print(folder_name + "Already exists")
        else:
            os.mkdir(folder_name)


def clean_name_section(folder_name, remove, return_type):
    head, sep, tail = folder_name.partition(remove)
    if return_type == "head":
        folder_name = head
    elif return_type == "sep":
        folder_name = sep
    else:
        folder_name = tail
    return folder_name
