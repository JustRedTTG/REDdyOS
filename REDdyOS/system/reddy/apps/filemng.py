data,lookup,os,pe,commons,framehost,fhID,iconSize,pager=None,None,None,None,None,None,None,None,None
def verify():
  return "app"
def init(dataV,lookupV):
  global data,lookup,os,commons,pe,framehost,fhID,iconSize,pager
  data = dataV
  lookup = lookupV
  class commonsV():
    icon = data.files + "reddy/icons/filemng.png"
    window_size = (500,300)
    window_type = 1
    window_pos = data.common.window_pos
    title = "File Manager"
  commons = commonsV
  iconSize = int((commons.window_size[0] - 100) / 4)
  os = lookup.get("os")
  pe = lookup.get("PGE")

  ezd = lookup.get("EZdrag")
  pager = ezd.horizontal.pager((95,commons.window_size[1]/2,10,25),pe.color.gray,pe.color.black)

  framehost = lookup.get("FHost")
  fhID = framehost.setup("filemng",commons)
  return "filemng", 8, 2

drawerX = 100

def calc(x,y,iconS,rowlimit):
  if x+iconS*2 > commons.window_size[0]:
    y+= iconS+20
    x = drawerX+5
  else:
    x+=iconS
  return x,y,iconS,rowlimit

rowLimit = 4

def draw():
  global rowLimit,iconSize,calc,pager,drawerX
  framehost.draw(fhID)
  framehost.screen(fhID)

  sS = pe.display.get.size()
  pe.fill.full(pe.color.verydarkgray)
  pager.y = commons.window_size[1]/2
  ezd = lookup.get("EZdrag")

  drawerX = ezd.horizontal.drag_pager(pager)+5
  pe.draw.line(data.red, (drawerX - 5, 0), (drawerX - 5, sS[1]), 2)
  ezd.horizontal.draw_pager(pager)

  im = lookup.get("iconmng")

  x,y=drawerX+5,0

  files = ["shin.exe","shin","shin.exe","shin","shin","shin","shin"]
  c=0
  icons=[]
  for file in files:
    icons.append(im.drawIcon((x,y,iconSize,iconSize+20),str(c),commons.window_pos,im.commonIcons(file)))
    x,y,iconSize,rowLimit = calc(x,y,iconSize,rowLimit)
    c+=1
  if data.focus == "filemng":
    im.selecter((commons.window_pos[0]+drawerX,commons.window_pos[1],commons.window_size[0]-drawerX,max(commons.window_size[1],y)),icons)
  framehost.exit(fhID)