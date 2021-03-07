# sudo ln -s /home/andrei/scripts/dotfiles /etc/skel/.config/dotfiles

import os
import tkinter as tk
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

file = open("locations", "r")
list = file.readlines()
listbox_widget = tk.Listbox(bottomframe, listvariable=list, selectbackground='#ff2400', selectmode=tk.MULTIPLE, height=600)

def addPath(text):
    file = open("locations", "a")
    file.writelines(text)
    listbox_widget.insert('end', text.rstrip())
    addField.delete(0, 'end')
    # print(listbox_widget.curselection())

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
removeButton = tk.Button(frame, text ="remove", command = lambda:[deleteSelected(listbox_widget.curselection())])
removeButton.pack(side = tk.LEFT)

showList()


# for setting in list:
#     paths = config.get('LIST', 'paths')
#     greeting = tk.Label(text=paths)
#     greeting.pack()

window.mainloop()