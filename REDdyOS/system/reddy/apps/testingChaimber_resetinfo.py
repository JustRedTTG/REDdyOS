data,lookup,pe,commons,framehost,FID=None,None,None,None,None,None
def verify():
  return "app"
def init(dataV,lookupV):
  global data,lookup,commons,pe,framehost,FID
  data = dataV
  lookup = lookupV
  class commonsV():
    icon = data.files + "reddy/icons/tch.png"
    window_size = (500,100)
    window_type = 0
    window_pos = (data.display_rect.width/2-250,data.display_rect.height/2-50)
    title = "Testing Chaimber!"
  commons = commonsV
  pe = lookup.get("PGE")
  framehost = lookup.get("FHost")
  FID = framehost.setup("tchINFO", commons)
  return "tchINFO", 8, 2
calls = 0
def draw():
  global calls
  framehost.draw(FID)
  framehost.screen(FID)
  pe.fill.full(pe.colors.white)
  pe.text.display(pe.text.make("The System modules were restarted!", 'freesansbold.ttf', 25, pe.math.center((0,0,500,100)), (pe.colors.black, None)))
  framehost.exit(FID)
  calls+=1
  if calls >= 100:
    framehost.close(FID)
    data.operations.append("run reddy/apps/testingChaimber.py")