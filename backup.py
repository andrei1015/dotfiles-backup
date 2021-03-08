# sudo ln -s /home/andrei/scripts/dotfiles /etc/skel/.config/dotfiles

import os
import tkinter as tk
from tkinter import messagebox 
import configparser


config = configparser.ConfigParser()
# list = config.read('backup.cfg')
window = tk.Tk()
window.title(".dotfiles backup")
window.resizable(True, False)
window.geometry("700x600")

frame = tk.Frame(window)
frame.pack()

bottomframe = tk.Frame(window)
bottomframe.pack( side = tk.BOTTOM, fill = tk.BOTH)

list=[]

with open("locations", "r") as file:
    list = file.readlines()
    listbox_widget = tk.Listbox(bottomframe, listvariable=list, selectbackground='#ff2400', selectmode=tk.MULTIPLE, height=600)

def addPath(text):
    # text = convertPath(text)
    # print(text)
    print("textu e:"+text) #logging

    if os.path.exists(os.path.expanduser(text.rstrip())):
        if checkPath(text) is not False:
            print("E BUN") #logging
            with open("locations", "a") as file:
                file.writelines(text)
                list.append(text)
            listbox_widget.insert('end', text.rstrip())
            addField.delete(0, 'end')
            # print(listbox_widget.curselection())
        else:
            print("NU E BUN") #logging
    else:
        print("NU E PATH") #logging
        messagebox.showerror('Error', 'The path you have provided is not a valid location')

def checkPath(text):
    with open("locations", "r") as file:
        list = file.readlines()
        for line in list:
            if os.path.expanduser(line.rstrip()) == os.path.expanduser(text.rstrip()):
                print("duplicat") #logging
                messagebox.showerror('Error', 'The path you have provided is already in the list')
                return False
            else:
                #copil
                if os.path.expanduser(text.rstrip()).startswith(os.path.expanduser(line.rstrip())):
                    print("asta-i copil") #logging
                    messagebox.showerror('Error', 'The path you have provided is the child of another entry')
                    return False
                #parinte
                if os.path.expanduser(line.rstrip()).startswith(os.path.expanduser(text.rstrip())):
                    messagebox.showerror('Error', 'The path you have provided is the parent of another entry')
                    print("asta-i parinte") #logging
                    return False
    return True

# def convertPath(text):
#     if os.path.isdir(text.rstrip()):
#         return "dir"
#         # if not text.endswith(os.path.sep):
#         #     text = text.rstrip() + os.path.sep
#         #     return text
#     else:
#         return text

# def deletePath(text):
#     file = open("locations", "a")
#     file.writelines(text)
#     listbox_widget.insert('end', text.rstrip())
#     addField.delete(0, 'end')
#     print(listbox_widget.curselection())

def showList():
    for path in list:
        listbox_widget.insert('end', path.rstrip())
        listbox_widget.pack(side = tk.BOTTOM, fill = tk.BOTH)

def deleteSelected(toDelete):
    for line in toDelete[::-1]:
        listbox_widget.delete(line)
        os.system("sed -i '" + str(line+1) + "d' locations")
        # print(line)
        

# def refresh():
# 	listbox_widget.delete(0, tk.END)
# 	for path in list:
# 	    listbox_widget.insert(tk.END, path)


addField = tk.Entry(frame)
addField.pack(side = tk.LEFT)
addbutton = tk.Button(frame, text ="add", command = lambda:[addPath(addField.get() + '\n')])
addbutton.pack(side = tk.LEFT)
removeButton = tk.Button(frame, text ="remove selected", command = lambda:[deleteSelected(listbox_widget.curselection())])
removeButton.pack(side = tk.LEFT)
syncButton = tk.Button(frame, text ="sync")
syncButton.pack(side = tk.LEFT)
restoreButton = tk.Button(frame, text ="restore")
restoreButton.pack(side = tk.LEFT)

showList()


# for setting in list:
#     paths = config.get('LIST', 'paths')
#     greeting = tk.Label(text=paths)
#     greeting.pack()

window.mainloop()