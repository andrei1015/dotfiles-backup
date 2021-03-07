# sudo ln -s /home/andrei/scripts/dotfiles /etc/skel/.config/dotfiles

import os
import tkinter as tk
import configparser


config = configparser.ConfigParser()
#list = config.read('backup.cfg')
window = tk.Tk()
window.title(".dotfiles backup")
window.resizable(False, False)
window.geometry("700x700")

file = open("locations", "r")
list = file.readlines()
listbox_widget = tk.Listbox(window, listvariable=list, selectbackground='#ff2400', selectmode=tk.MULTIPLE)

def addPath(text):
    file = open("locations", "a")
    file.writelines(text)
    listbox_widget.insert('end', text.rstrip())
    addField.delete(0, 'end')
    print(listbox_widget.curselection())

def deletePath(text):
    file = open("locations", "a")
    file.writelines(text)
    listbox_widget.insert('end', text.rstrip())
    addField.delete(0, 'end')
    print(listbox_widget.curselection())

def showList():
    for path in list:
        listbox_widget.insert('end', path.rstrip())
        listbox_widget.grid(row = 1, column = 5, columnspan = 4)

def deleteSelected(toDelete):
    for line in toDelete[::-1]:
        listbox_widget.delete(line)
        os.system("sed -i '" + str(line+1) + "d' locations")
        print(line)
        

# def refresh():
# 	listbox_widget.delete(0, tk.END)
# 	for path in list:
# 	    listbox_widget.insert(tk.END, path)


addField = tk.Entry(window).grid(row = 0, column = 0, padx=100, pady=100, ipady=30, sticky = 'nsew')

addButton = tk.Button(window, text ="add", command = lambda:[addPath(addField.get() + '\n')]).grid(row = 1, column = 1)

removeButton = tk.Button(window, text ="remvoe", command = lambda:[deleteSelected(listbox_widget.curselection())]).grid(row = 1, column = 1)

showList()


# for setting in list:
#     paths = config.get('LIST', 'paths')
#     greeting = tk.Label(text=paths)
#     greeting.pack()

window.mainloop()