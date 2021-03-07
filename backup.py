# sudo ln -s /home/andrei/scripts/dotfiles /etc/skel/.config/dotfiles

import os
import tkinter as tk
import configparser


config = configparser.ConfigParser()
#list = config.read('backup.cfg')
window = tk.Tk()
window.title(".dotfiles backup")
window.geometry("700x700")


file = open("locations", "r")
list = file.readlines()
listbox_widget = tk.Listbox(window, listvariable=list)

def addPath(text):
    file = open("locations", "a")
    file.writelines(text)
    listbox_widget.insert('end', text.rstrip())
    print(text)

# def refresh():
# 	listbox_widget.delete(0, tk.END)
# 	for path in list:
# 	    listbox_widget.insert(tk.END, path)


addField = tk.Entry(window)
addField.pack()

addbutton = tk.Button(window, text ="add", command = lambda:[addPath(addField.get() + '\n')])
addbutton.pack()

for path in list:
    listbox_widget.insert('end', path.rstrip())
    listbox_widget.pack()
    # greeting = tk.Label(frame, text=path)
    # greeting.pack()


# for setting in list:
#     paths = config.get('LIST', 'paths')
#     greeting = tk.Label(text=paths)
#     greeting.pack()

window.mainloop()