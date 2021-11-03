__author__ = "Fateh Sandhu"
__email__ = "fatehkaran@huskers.unl.edu"


"""
Takes in a weblink or text and converts it into qrCode using a GUI
Built using Tkinter library.

"""

import sys
import tkinter as tk
import qrcode as qr
from PIL import Image
from tkinter import messagebox

qrCode = qr.make("welcome")
qrCode.save("qr.png")


# define function that updates qrCode when <generateQR> button is clicked.
def gen_code():
    text = ent_val.get()
    qrCode = qr.make(text)
    qrCode.save("qrUpdate.png")
    ent_val.delete(0, tk.END)
    qrImg1 = tk.PhotoImage(file="qrUpdate.png")
    display.configure(image=qrImg1)
    display.image = qrImg1


window = tk.Tk()
window.title("QR Code Generator")

lbl_insert = tk.Label(text="Enter text or weblink: ")
lbl_insert.pack()
ent_val = tk.Entry(lbl_insert, width=30, bg="white", fg="black", text="Enter text/weblink")
ent_val.pack()
qrImg = tk.PhotoImage(file="qr.png")
display = tk.Label(image=qrImg)
display.pack(side=tk.BOTTOM)

btn = tk.Button(text="Generate QR", command=gen_code)
btn.pack()

window.mainloop()
