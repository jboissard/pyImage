
from PIL import Image, ImageChops
import requests


def getQrFromUrl(img):
  url = 'http://www.qrcode-monkey.de/download-qrcode.php?png=temp/qrcodeb210e9139b92d700bc0b55c0d7341103.png'

  f = open(img, 'wb')
  f.write(requests.get(url).content)


# properly opens PNG
# http://stackoverflow.com/questions/9166400/convert-rgba-png-to-rgb-with-pil
# http://stackoverflow.com/questions/7911451/pil-convert-png-or-gif-with-transparency-to-jpg-without
def formatImage(path):
  im = Image.open(path).convert('RGBA')
  r = Image.new('RGBA', im.size, (255,255,255))
  r = Image.alpha_composite(r, im)
  return r

# resizes image
# param w: width
# param h: height
# http://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
def resize(img, w, h):
  return img.resize((w, h), Image.ANTIALIAS)


# open logo
logo = formatImage("logo.png")






# prepare canvas `r`
rsize = (1101, 1101)
r  = Image.new('RGBA',rsize,(255,255,255,255))

# QR
qrpath = "qrcode2.png"
getQrFromUrl(qrpath)
qr = formatImage(qrpath)
qrsize = 100
qrmargin = 20
qr_x = rsize[0] - qrmargin - qrsize
qr_y = rsize[1] - qrmargin - qrsize

qrmini = resize(qr, qrsize, qrsize)
r.paste(qrmini, (qr_x, qr_y), qrmini)
# End QR

#see: http://stackoverflow.com/questions/5324647/how-to-merge-a-transparent-png-image-with-another-image-using-pil
r.paste(logo, (0,0), logo)
#r.show()
r.save('out.png')