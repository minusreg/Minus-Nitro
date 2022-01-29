import tkinter as tk
from turtle import width
from PIL import Image
from PIL import ImageTk
import pyperclip

from tkinter import *


root = tk.Tk()
root.title("Minus Nitro")
root.geometry("650x75")
root.resizable(width=False, height=False)

hug1 = ImageTk.PhotoImage(file='./MinusNitro/images/hug1.png')

def hug1copy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953124009168916/hug1.png")

hug1b = Button(root,  image=hug1, command=hug1copy, borderwidth=0)
hug1b.pack(side=tk.LEFT)

hehe = ImageTk.PhotoImage(file="./MinusNitro/images/hehe.png")
def hehecopy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953123782672444/hehe.png")
heheb = Button(root,  image=hehe, command=hehecopy, borderwidth=0)
heheb.pack(side=tk.LEFT)

peak1 = ImageTk.PhotoImage(file="./MinusNitro/images/peak1.png")
def peak1copy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953124508287026/peak1.png")
peak1b = Button(root,  image=peak1, command=peak1copy, borderwidth=0)
peak1b.pack(side=tk.LEFT)

yep = ImageTk.PhotoImage(file="./MinusNitro/images/yep.png")
def yepcopy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953125347156028/yep.png")
yepb = Button(root,  image=yep, command=yepcopy, borderwidth=0)
yepb.pack(side=tk.LEFT)

trolley = ImageTk.PhotoImage(file="./MinusNitro/images/trolley.png")
def trolleycopy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953125087105024/trolley.png")
trolleyb = Button(root,  image=trolley, command=trolleycopy, borderwidth=0)
trolleyb.pack(side=tk.LEFT)

kekw = ImageTk.PhotoImage(file="./MinusNitro/images/kekw.png")
def kekwcopy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953124294373436/kekw.png")
kekwb = Button(root,  image=kekw, command=kekwcopy, borderwidth=0)
kekwb.pack(side=tk.LEFT)

sadge = ImageTk.PhotoImage(file="./MinusNitro/images/sadge.png")
def sadgecopy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953124889985034/sadge.png")
sadgeb = Button(root,  image=sadge, command=sadgecopy, borderwidth=0)
sadgeb.pack(side=tk.LEFT)

pog = ImageTk.PhotoImage(file="./MinusNitro/images/pog.png")
def pogcopy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953124713820190/pog.png")
pogb = Button(root,  image=pog, command=pogcopy, borderwidth=0)
pogb.pack(side=tk.LEFT)

copium = ImageTk.PhotoImage(file="./MinusNitro/images/copium.png")
def copiumcopy():
    pyperclip.copy("https://cdn.discordapp.com/attachments/796158544784523285/936953123598131200/copium.png")
copiumb = Button(root,  image=copium, command=copiumcopy, borderwidth=0)
copiumb.pack(side=tk.LEFT)

mainloop()