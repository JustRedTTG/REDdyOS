data,lookup,pe,numpy,Image,ImageDraw=None,None,None,None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe,Image,ImageDraw,numpy
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  numpy = lookup.get("numpy")
  Image = lookup.get("PIL.Image")
  ImageDraw = lookup.get("PIL.ImageDraw")
  return "circlepfp"

def username(username):
    sm = lookup.get("stgmng")
    um = lookup.get("usrmng")
    settings = sm.get(um.load.user(username).settings)
    pfp = settings.pfp
    if pfp != "NONE":
        #
        img = Image.open(data.files+pfp).convert("RGB")
        numpyImage = numpy.array(img)
        h, w = img.size
        # Create same size alpha layer with circle
        alpha = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, h, w], 0, 360, fill=255)

        # Convert alpha Image to numpy array
        numpyAlpha = numpy.array(alpha)

        # Add alpha layer to RGB
        numpyImage = numpy.dstack((numpyImage, numpyAlpha))

        # Save with alpha
        Image.fromarray(numpyImage).save(data.files+"data/temp/pfptemp.png")
        return data.files+"data/temp/pfptemp.png"
    else:
        return False