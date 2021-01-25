import os, sys
from PIL import Image

size = 1500, 1500

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".bordered.jpg"
    print (outfile)
    if infile != outfile:
        try:
            
            # resize
            basewidth = 1300
            img = Image.open(infile)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)

            # add border
            old_size = img.size
            new_size = (1500, 1500)
            new_im = Image.new("RGB", new_size, (255, 255, 255))
            new_im.paste(img, (int((new_size[0]-old_size[0])/2),
                               int((new_size[1]-old_size[1])/2)))

            # new_im.show()
            img.save(outfile)

        except IOError:
            print("cannot create bordered image for '%s'" % infile)