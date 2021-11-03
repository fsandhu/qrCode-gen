import sys
import tkinter as tk
import qrcode as qr
from PIL import Image

qrCode = qr.make("welcome")
qrCode.save("qr.png")


def gen_code():
    text = ent_val.get()
    qrCode = qr.make(text)
    qrCode.save("qrUpdate.png")
    ent_val.delete(0, tk.END)
    qrImg1 = tk.PhotoImage(file="qrUpdate.png")
    display.configure(image=qrImg1)
    display.image = qrImg1
    return


window = tk.Tk()
window.title("QR Code Generator")

lbl_insert = tk.Label(text="Enter text or weblink: ")
lbl_insert.pack()
ent_val = tk.Entry(width=40, bg="white", fg="black", text="Enter text/weblink")
ent_val.pack()
qrImg = tk.PhotoImage(file="qr.png")
display = tk.Label(image=qrImg)
btn = tk.Button(text="Generate QR", command=gen_code())
btn.pack()
display.pack(side=tk.BOTTOM)

window.mainloop()
