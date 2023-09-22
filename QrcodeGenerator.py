# IMPORT
import qrcode

text = input("Qrcode Text: ")

# MAKE QRCODE
img = qrcode.make(f"{text}")
type(img)
# SAVEIMAGE

img.save(f"{text}.png")