from tkinter import *
import cv2
from tkinter import filedialog
import os
import steganography as st

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    img1 = cv2.imread(openfn(), 0)
    img2 = cv2.imread(openfn(), 0)
    img3=st.merge(img1,img2)
    cv2.imshow('image', img3)

def demerge_img():
    img1 = cv2.imread(openfn(), 0)
    img=st.unmerge(img1)
    cv2.imshow('image', img)

btn = Button(root, text='Upload cover and secret image', command=open_img).pack()
btn = Button(root, text='Demerge image', command=demerge_img).pack()
root.mainloop()