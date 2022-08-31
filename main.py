# Python Project - QR Code Generator Version 1
# Build By - Ayush Gupta


import qrcode
import image
import random

# List of colors
col_list = ["#FA9494", "#7FB77E", "#7FBCD2", "#F94892", "#554994", "#FAD9A1"]
val = random.randint(0, len(col_list) - 1)

# Using Qr code module
qr = qrcode.QRCode(version=10, box_size=6, border=2, )

# Making it interactive
print("________QR CODE GENERATOR__________")
print("-----------------------------------")

# Input of the data from the user
data = str(input("Enter the text/website : "))


qr.add_data(data)
qr.make(fit=True)

# Using Random values in order to get random color of QR codes
img = qr.make_image(fill_color=col_list[val], back_color="white")

# Name of the image file to save as
img.save("test1.png")
try:
    print("QR CODE HAS SUCCESSFULLY BUILD")
except:
    print("Invalid Data")
