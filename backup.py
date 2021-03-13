import os, sys
import tkinter as tk
from tkinter import messagebox
from distutils.dir_util import copy_tree
import configparser
from images_base64 import getImage, addIcon, removeIcon, saveIcon, restoreIcon

def files():
    settingsFile = os.path.exists('settings.cfg')
    locationsFile = os.path.exists('locations')
    if settingsFile == False or locationsFile == False:
        settingsFile = open("settings.cfg", "w+")
        settingsFile.write('[SETTINGS]\n')
        settingsFile.write('location = ~/.dotfiles\n')
        settingsFile.write('addIcon = add.png\n')
        settingsFile.write('removeIcon = remove.png\n')
        settingsFile.write('saveIcon = save.png\n')
        settingsFile.write('restoreIcon = restore.png\n')
        locationsFile = open("locations", "w+")
        locationsFile.write('~/.bashrc\n')
        locationsFile.write('~/.profile\n')
        settingsFile.close()
        locationsFile.close()
files()

def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'

config = configparser.ConfigParser()
cfg = config.read('settings.cfg')
window = tk.Tk()
window.title(".dotfiles backup")
window.resizable(True, True)
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)


window.geometry("700x300")
window.minsize(700, 300)

frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
frame.columnconfigure(0, weight=1)


bottomframe = tk.Frame(window, background='red')
bottomframe.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
bottomframe.columnconfigure(0, weight=1)
bottomframe.rowconfigure(1, weight=1)

list=[]

with open("locations", "r") as file:
    list = file.readlines()
    listbox_widget = tk.Listbox(bottomframe, listvariable=list, selectbackground='#ff2400', selectmode=tk.MULTIPLE)
    listbox_widget.grid(row=1, column=0, sticky='nsew')

def addPath(text):
    if os.path.exists(os.path.expanduser(text.rstrip())):
        if checkPath(text) is not False:
            with open("locations", "a") as file:
                file.writelines(text)
                list.append(text)
            listbox_widget.insert('end', text.rstrip())
            addField.delete(0, 'end')
    else:
        messagebox.showerror('Error', 'The path you have provided is not a valid location')

def checkPath(text):
    with open("locations", "r") as file:
        list = file.readlines()
        for line in list:
            if os.path.expanduser(line.rstrip()) == os.path.expanduser(text.rstrip()):
                messagebox.showerror('Error', 'The path you have provided is already in the list')
                return False
            else:
                if os.path.expanduser(text.rstrip()).startswith(os.path.expanduser(line.rstrip())):
                    messagebox.showerror('Error', 'The path you have provided is the child of another entry')
                    return False
                if os.path.expanduser(line.rstrip()).startswith(os.path.expanduser(text.rstrip())):
                    messagebox.showerror('Error', 'The path you have provided is the parent of another entry')
                    return False
    return True

def save():
    backup_location = os.path.expanduser(config.get('SETTINGS', 'location'))
    backupFolder()
    for path in list:
        sanitised_path = os.path.expanduser(path.rstrip())
        os.system("cp -ar --parents " + sanitised_path + " " + backup_location + "/")

def backupFolder():
    backupFolder = os.path.expanduser(config.get('SETTINGS', 'location').rstrip())
    if os.path.exists(backupFolder) == False:
        os.makedirs(backupFolder)

def restore():
    backup_location = os.path.expanduser(config.get('SETTINGS', 'location'))
    home = os.path.expanduser("~")
    for path in list:
        sanitised_path = os.path.expanduser(path.rstrip())
        os.system("cp -r " + backup_location + sanitised_path + " " + home)

def deleteSelected(toDelete):
    for line in toDelete[::-1]:
        listbox_widget.delete(line)
        os.system("sed -i '" + str(line+1) + "d' locations")

def showList():
    for path in list:
        listbox_widget.insert('end', path.rstrip())
        listbox_widget.grid(row=1, column=0, sticky='nsew')
        #listbox_widget.rowconfigure(0, weight=1)

addField = tk.Entry(frame, width=1000)
addField.grid(row = 0, column = 0, ipady=5)

addIcon = tk.PhotoImage(data = addIcon) 
addbutton = tk.Button(frame, text ="add", image = addIcon, compound=tk.LEFT, command = lambda:[addPath(addField.get() + '\n')])
addbutton.grid(row = 0, column = 1)

removeIcon = tk.PhotoImage(data = removeIcon) 
removeButton = tk.Button(frame, text ="remove selected", image = removeIcon, compound=tk.LEFT, command = lambda:[deleteSelected(listbox_widget.curselection())])
removeButton.grid(row = 0, column = 2)

saveIcon = tk.PhotoImage(data = saveIcon) 
saveButton = tk.Button(frame, text ="save", image = saveIcon, compound=tk.LEFT, command = lambda:[save()])
saveButton.grid(row = 0, column = 3)

restoreIcon = tk.PhotoImage(data = restoreIcon) 
restoreButton = tk.Button(frame, text ="restore", image = restoreIcon, compound=tk.LEFT, command = lambda:[restore()])
restoreButton.grid(row = 0, column = 4)


showList()

window.mainloop()