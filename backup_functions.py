# sudo ln -s /home/andrei/scripts/dotfiles /etc/skel/.config/dotfiles

import os
import tkinter as tk
from tkinter import messagebox
from distutils.dir_util import copy_tree
import configparser
from functions import files, addPath, deleteSelected, save, restore, showList

files()

config = configparser.ConfigParser()
cfg = config.read('settings.cfg')
window = tk.Tk()
window.title(".dotfiles backup")
window.resizable(True, True)
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# def center_window(w, h):
#     # get screen width and height
#     ws = window.winfo_screenwidth()
#     hs = window.winfo_screenheight()
#     # calculate position x, y
#     x = (ws/2) - (w/2)    
#     y = (hs/2) - (h/2)
#     window.geometry('%dx%d+%d+%d' % (w, h, x, y))


# center_window(700, 300)
window.geometry("100x200")
window.minsize(700, 300)

frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
frame.columnconfigure(0, weight=1)


bottomframe = tk.Frame(window, background='red')
bottomframe.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
bottomframe.columnconfigure(0, weight=1)
bottomframe.rowconfigure(1, weight=1)

addField = tk.Entry(frame, width=1000)
addField.grid(row = 0, column = 0, ipady=5)

addIcon = tk.PhotoImage(file = config.get('SETTINGS', 'addIcon')) 
addbutton = tk.Button(frame, text ="add", image = addIcon, compound=tk.LEFT, command = lambda:[backupFolder(), addPath(addField.get() + '\n')])
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