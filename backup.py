# sudo ln -s /home/andrei/scripts/dotfiles /etc/skel/.config/dotfiles

import os
import tkinter as tk
from tkinter import messagebox
from distutils.dir_util import copy_tree
import configparser


config = configparser.ConfigParser()
cfg = config.read('settings.cfg')
window = tk.Tk()
window.title(".dotfiles backup")
window.resizable(True, True)
window.columnconfigure(0, weight=1)

def center_window(w, h):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(700, 300)

frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky='nsew')
frame.columnconfigure(0, weight=1)


bottomframe = tk.Frame(window)
bottomframe.grid(row=1, column=0, columnspan=6, sticky='nsew')
bottomframe.columnconfigure(0, weight=1)

list=[]

with open("locations", "r") as file:
    list = file.readlines()
    listbox_widget = tk.Listbox(bottomframe, listvariable=list, selectbackground='#ff2400', selectmode=tk.MULTIPLE)

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
    for path in list:
        sanitised_path = os.path.expanduser(path.rstrip())
        os.system("cp -ar --parents " + sanitised_path + " " + backup_location + "/")

def restore():
    backup_location = os.path.expanduser(config.get('SETTINGS', 'location'))
    home = os.path.expanduser("~")
    for path in list:
        sanitised_path = os.path.expanduser(path.rstrip())
        os.system("cp -r " + backup_location + sanitised_path + " " + home)

def showList():
    for path in list:
        listbox_widget.insert('end', path.rstrip())
        listbox_widget.grid(row=1, column=0, sticky='nsew')

def deleteSelected(toDelete):
    for line in toDelete[::-1]:
        listbox_widget.delete(line)
        os.system("sed -i '" + str(line+1) + "d' locations")


addField = tk.Entry(frame, width=100)
addField.grid(row = 0, column = 0, ipady=5)

addIcon = tk.PhotoImage(file = config.get('SETTINGS', 'addIcon')) 
addbutton = tk.Button(frame, text ="add", image = addIcon, compound=tk.LEFT, command = lambda:[addPath(addField.get() + '\n')])
addbutton.grid(row = 0, column = 1)

removeIcon = tk.PhotoImage(file = config.get('SETTINGS', 'removeIcon')) 
removeButton = tk.Button(frame, text ="remove selected", image = removeIcon, compound=tk.LEFT, command = lambda:[deleteSelected(listbox_widget.curselection())])
removeButton.grid(row = 0, column = 2)

saveIcon = tk.PhotoImage(file = config.get('SETTINGS', 'saveIcon')) 
saveButton = tk.Button(frame, text ="save", image = saveIcon, compound=tk.LEFT, command = lambda:[save()])
saveButton.grid(row = 0, column = 3)

restoreIcon = tk.PhotoImage(file = config.get('SETTINGS', 'restoreIcon')) 
restoreButton = tk.Button(frame, text ="restore", image = restoreIcon, compound=tk.LEFT, command = lambda:[restore()])
restoreButton.grid(row = 0, column = 4)


showList()

window.mainloop()