from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def openNewWindow():
    read: easygui.fileopenbox()
    return read


def openFile():
    string = openNewWindow()
    try:
        os.startfile(string)
    except:
        mbshowinfo('confirmation', 'File Not Found')


def copyFile():
    fileSource = openNewWindow()
    fileDestination = filedialog.askdirectory()
    shutil.copy(fileSource, fileDestination)
    mb.showinfo('File Copied')


def deleteFile():
    del_file = openNewWindow()
    if os.path.exist(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('File Deleted')


def renameFile():
    fileToBeRenamed = openNewWindow()
    path1 = os.path.dirname(fileToBeRenamed)
    extension = os.path.splittext(fileToBeRenamed)[1]
    newName = input('What do you wish to rename this file to?')
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(fileToBeRenamed, path)
    mb.showinfo('File renamed!')


def moveFile():
    fileSource = openNewWindow()
    fileDestination = filedialog.askdirectory()
    if fileSource == fileDestination:
        mb.showinfo('Confirmation',
                    'Source location and destination are the same.')
    else:
        shutil.move(fileSource, fileDestination)
        mb.showinfo('File Moved')


def makeFolder():
    newFolderPath = filedialog.filedialog.askdirectory()
    print('Enter name of new folder')

    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)

    os.mkdir(path)
    mb.showinfo('Folder Created')


def deleteFolder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    # POSSIBLY REMOVE STEP. 2.8 IN GUIDE
    mb.showinfo('The folder', delFolder, 'was removed')


def listFolderFiles():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print('Files in', folderList, 'folder are:')
    while (i < len(sortlist)):
        print(sortlist[i]+'\n')
        i += 1


root = Tk()
# creating a canvas to insert image
canv = Canvas(root, width=500, height=420, bg='white')
canv.grid(row=0, column=2)
# creating label and buttons to perform operations
Label(root, text="TechVidvan File Manager", font=(
    "Helvetica", 16), fg="blue").grid(row=5, column=2)
Button(root, text="Open a File", command=openFile).grid(row=15, column=2)
Button(root, text="Copy a File", command=copyFile).grid(row=25, column=2)
Button(root, text="Delete a File", command=deleteFile).grid(row=35, column=2)
Button(root, text="Rename a File", command=renameFile).grid(row=45, column=2)
Button(root, text="Move a File", command=moveFile).grid(row=55, column=2)
Button(root, text="Make a Folder", command=makeFolder).grid(row=75, column=2)
Button(root, text="Remove a Folder",
       command=deleteFolder).grid(row=65, column=2)
Button(root, text="List all Files in Directory",
       command=listFolderFiles).grid(row=85, column=2)
root.mainloop()
