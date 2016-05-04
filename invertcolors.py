OLD_PATH = r'/Users/Johan/Desktop/logo.png'
NEW_PATH = r'/srv/frontend/nexyspublic/assets/img/logo2.png'

R_OLD, G_OLD, B_OLD = (255, 255, 255)
R_NEW, G_NEW, B_NEW = (0, 174, 239)

from PIL import Image
im = Image.open(OLD_PATH)
rgb_im = im.convert('RGBA')

pixels = rgb_im.load()


def toHex(r,g,b):
  return '#%02x%02x%02x' % (r, g, b)


print toHex(255,255,255) # returns #ffffff;
print toHex(0,0,0) # returns #000000;


def invert(r,g,b):
  return (255-r, 255-g, 255-b)


print invert(0,0,0)


width, height = rgb_im.size
for x in range(width):
    for y in range(height):

        r,g,b,a = pixels[x,y]


        if a>0:
          (r2, g2, b2) = invert(r,g,b)

          #print str(r)+" "+str(g)+" "+str(b)+" "+str(a)+"\t"+str(r2)+" "+str(g2)+" "+str(b2)
          pixels[x,y] = (r2, g2, b2, a)




rgb_im.crop((0, 0, width-35, height)).save(NEW_PATH)