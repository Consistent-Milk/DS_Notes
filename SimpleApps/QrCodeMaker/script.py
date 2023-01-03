# qrcode is a third party library that
# allows us to easily make QR Codes from a particular string

import os
import qrcode as qr

# Check to see what the current working directory is
# it will output the root path of this repo in the local machine
print(os.getcwd())

qr_img = qr.make("https://github.com/Consistent-Milk/DS_Notes")

# Navigate to the current directory starting from 'cwd'
# and save the image in the same directory of the script
qr_img.save("./SimpleApps/QrCodeMaker/Notes.png")
