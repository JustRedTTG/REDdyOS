data,lookup,pe=None,None,None
def verify():
  return "app"
def init(dataV,lookupV):
  global data,lookup,pe
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  return "desktop",0,2
freeze=False
lastM=False
grid = []
def makegrid():
  global grid
  grid=[]
  x,y=5,5
  while y+90<data.mS[1]:
    while x+70<data.mS[0]:
      grid.append([(x,y,70,90),None])
      x += 75
    y += 95
    x=5
  return grid
def drawApps():
  grid = makegrid()
  im=lookup.get("iconmng")
  for it in lookup.get("os").listdir(data.files+"data/Users/"+data.current_user+"/Desktop/"):
    good = True
    if lookup.get("os").path.isfile(data.files+"data/Users/"+data.current_user+"/Desktop/"+it):
      for g in grid:
        if good and g[1]==None:
          im.drawIcon(g[0],data.files+"data/Users/"+data.current_user+"/Desktop/"+it,icon=im.commonIcons(it))
          g[1]=data.files+"data/Users/"+data.current_user+"/Desktop/"+it
          good=False
def draw():
  global freeze,lastM
  lookup.get("DrawATheme").draw()
  mouse = lookup.get("mouse")
  fh = lookup.get("FHost")
  if mouse.left() and fh.clickOut() and not freeze and not lastM:
    data.operations.append("focus NONE")
  elif freeze:
    if not mouse.left() and not mouse.middle() and not mouse.right():
      freeze = False
  drawApps()
  lastM=mouse.left()