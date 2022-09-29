from distutils import extension
import tkinter
import shutil
import easygui
import imageio

from tkinter import filedialog
from tkinter import *
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
  extension=os.path.splittext(fileToBeRenamed)[1]
  newName = input('What do you wish to rename this file to?')
  path = os.path.join(path1, newName+extension)
  print(path)
  os.rename(fileToBeRenamed,path)
  mb.showinfo('File renamed!')



def moveFile():
  fileSource = openNewWindow()
  fileDestination = filedialog.askdirectory()
  if fileSource==fileDestination: 
    mb.showinfo('Confirmation' , 'Source location and destination are the same.')
  else:
    shutil.move(fileSource, fileDestination)
    mb.showinfo('File Moved')

