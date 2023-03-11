from turtle import fillcolor
import qrcode as qr
import PIL # PIL == PILLOW
from PIL import Image
# inp = input("Enter any text: ")
# img = qr.make(inp)
# img.save("qrcode.png")




#  If you Want to Edit the Color, size etc of QRcode, then:

ar = qr.QRCode(version =1, error_correction= qr.constants.ERROR_CORRECT_H, box_size = 10, border = 4)
ar.add_data("Hello")
ar.make(fit = True)
img = ar.make_image(fill_color = "white", back_color = 'black')
img.save("NewQrcode.jpeg")