# sudo ln -s /home/andrei/scripts/dotfiles /etc/skel/.config/dotfiles

import os
import tkinter as tk
import configparser

config = configparser.ConfigParser()
list = config.read('backup.cfg')


window = tk.Tk()
window.title(".dotfiles backup")
window.geometry("700x700")

def addPath():
    file = open("locations", "a")
    file.write('test\n')
    print('test1')

def refresh():
    greeting.update()


addField = tk.Entry(window)
addField.pack()

addbutton = tk.Button(window, text ="add", command = lambda:[addPath(), refresh()])
addbutton.pack()

frame = tk.Frame(list, width=100, height=50).pack()

file = open("locations", "r")
list = file.readlines()

for path in list:
    greeting = tk.Label(frame, text=path)
    greeting.pack()


# for setting in list:
#     paths = config.get('LIST', 'paths')
#     greeting = tk.Label(text=paths)
#     greeting.pack()

window.mainloop()