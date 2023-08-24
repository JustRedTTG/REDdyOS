data,lookup,pe,icon=None,None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe,icon
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  icon = data.files+"reddy/icons/mouse/standby.png"
  return "mouse"
#

off = None
iconoff = (0,0)
def seticon(i,c=False):
  global icon,iconoff
  icon = i
  if c:
    iconoff=(-10,-10)

def removeoff():
  global off
  off = pe.mouse.off
  pe.mouse.off = (0, 0)
def addoff():
  global off
  pe.mouse.off = off
def pos():
  removeoff()
  p = pe.mouse.pos()
  addoff()
  return p
def x():
  return pos()[0]
def y():
  return pos()[1]
#
def Wpos():
  return pe.mouse.pos()
def Wx():
  return Wpos()[0]
def Wy():
  return Wpos()[1]
#
def left():
  return pe.mouse.clicked()[0]
def middle():
  return pe.mouse.clicked()[1]
def right():
  return pe.mouse.clicked()[2]
cursor_enable=True
def getapp(appN):
  if appN == "NONE" or appN == "":
    return
  global mod2
  for x in mod2:
    if x[0] == appN:
      return x[3]
  pe.error("App error!")
def call():
  try:
    off = getapp(data.focus).commons.window_pos
    off = (off[0],off[1]+20)
  except:
    off = (0,0)
  pe.mouse.off = (off[0]*-1,off[1]*-1)
def endcall():
  global icon,iconoff,cursor_enable
  p = pos()
  p = (p[0]+iconoff[0],p[1]+iconoff[1])
  pe.pygame.mouse.set_visible(False)
  if cursor_enable:
    lookup.get("EZimage").image(icon, (20,20), p)
  else:
    cursor_enable = True
  icon = data.files+"reddy/icons/mouse/standby.png"
  iconoff = (0,0)
