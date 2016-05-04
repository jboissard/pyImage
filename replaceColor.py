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
im = im.convert('RGBA')


threshold = 90

pixels = im.load()

def tint(c1, c2):
  return (c1[0]*c2[0]/255, c1[1]*c2[1]/255, c1[2]*c2[2]/255)




def replace(c,r, n):
  d = (c[0] - r[0], c[1] - r[1], c[2] - r[2])
  e = (abs(d[0]), abs(d[1]), abs(d[2]))

  #se = e[0]*e[1]*e[2]
  se = sum(e)

  if se < threshold:
    f = (n[0]-d[0], n[1]-d[1], n[2]-d[2])
    print f
    return f
  else:
    return c

tcol = (200,250,255) # target color
ncol = (200, 200, 200) # new color


width, height = im.size
for x in range(width):
    for y in range(height):

        r,g,b,a = pixels[x,y]


        if a>0:
          (r2, g2, b2) = replace((r,g,b), tcol, ncol)

          #print str(r)+" "+str(g)+" "+str(b)+" "+str(a)+"\t"+str(r2)+" "+str(g2)+" "+str(b2)
          pixels[x,y] = (r2, g2, b2, a)




im.crop((0, 0, width-35, height)).save(outfile)