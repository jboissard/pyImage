#see: http://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
from PIL import Image, ImageChops
import sys

outfile = r'/Users/Johan/Desktop/out.jpg'

try:
  infile = sys.argv[1]
except Exception, e:
  print "add input file via comd line"
  raise


im = Image.open(infile)
rgb_im = im.convert('RGBA')

pixels = rgb_im.load()



def tint(c1, c2):
  return (c1[0]*c2[0]/255, c1[1]*c2[1]/255, c1[2]*c2[2]/255)





tcol = (0, 0, 255)


width, height = rgb_im.size
for x in range(width):
    for y in range(height):

        r,g,b,a = pixels[x,y]


        if a>0:
          (r2, g2, b2) = tint((r,g,b), tcol)

          #print str(r)+" "+str(g)+" "+str(b)+" "+str(a)+"\t"+str(r2)+" "+str(g2)+" "+str(b2)
          pixels[x,y] = (r2, g2, b2, a)




rgb_im.crop((0, 0, width-35, height)).save(outfile)