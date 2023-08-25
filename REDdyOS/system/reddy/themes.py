data,lookup,pe=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  return "DrawATheme"

def draw(red=None,red2=None,red3=None,red4=None,off=(0,0)):
  offx=off[0]
  offy=off[1]
  if red == None:
    red = data.red
  if red2 == None:
    red2 = data.red2
  if red3 == None:
    red3 = data.red3
  if red4 == None:
    red4 = data.red4
  full = int(data.display_rect.width / 3)
  half = int(data.display_rect.width / 4)
  smol = int(data.display_rect.width / 8)
  vsmol = int(data.display_rect.width / 20)
  if data.theme == 0:
    pe.draw.circle(red4,(data.display_rect.center[0]+offx,data.display_rect.center[1]+offy),full,0)
    pe.draw.circle(red3,(data.display_rect.center[0]+offx,data.display_rect.center[1]+offy),half,0)
    pe.draw.circle(red2,(data.display_rect.center[0]+offx,data.display_rect.center[1]+offy),smol,0)
    pe.draw.line(red,(0,data.display_rect.center[1]+offy),(data.display_rect.width+offx,data.display_rect.center[1]+offy),vsmol)
    pe.draw.line(red,(data.display_rect.center[0]+offx,0),(data.display_rect.center[0]+offx,data.display_rect.height+offy),vsmol)
  elif data.theme == 1:
    ic = data.display_rect.height/4
    y = offy
    pe.draw.rect(red,(offx,y,data.display_rect.width+offx,ic),0)
    y+=ic
    pe.draw.rect(red2,(offx,y,data.display_rect.width+offx,ic), 0)
    y+=ic
    pe.draw.rect(red3,(offx,y,data.display_rect.width+offx,ic), 0)
    y+=ic
    pe.draw.rect(red4,(offx,y,data.display_rect.width+offy,ic), 0)
    y+=ic
  #pe.draw.circle(pe.colors.black, (data.display_rect.center[0] + offx, data.display_rect.center[1] + offy), 5, 0)
  #pe.draw.rect(pe.colors.black, (offx, offy, data.display_rect.width, data.display_rect.height), 15)