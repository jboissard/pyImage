#see: http://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
from PIL import Image, ImageChops
import sys


outfile = r'/srv/frontend/nexyspublic/assets/img/portfolio/genlots.jpg'


try:
  infile = sys.argv[1]
except Exception, e:
  print "add input file via comd line"
  raise


print infile

im = Image.open(infile)


print im.size

size = (640, 467)

offset_tuple = (0,467-456)

im.thumbnail(size, Image.ANTIALIAS)




final_thumb = Image.new(mode='RGBA',size=size,color=(255,255,255,0))
final_thumb.paste(im, offset_tuple)
final_thumb.save(outfile, "JPEG")