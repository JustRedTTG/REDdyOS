data,lookup,pe,mouse,y,Max,Min=None,None,None,None,None,None,None
def verify():
  return "app"
def init(dataV,lookupV):
  global data,lookup,pe,mouse,y,Max,Min
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  mouse = lookup.get("mouse")
  y = data.mS[1] - 5
  Max = data.mS[1] - 35
  Min = y
  return "tskBAR",10,2

def changefocus(app):
  data.operations.append("focus "+app)
locked = False
def draw():
  global y,Max,Min
  try:
    if mouse.y()>=y:
      if y>Max:
        y-=2
    elif not locked:
      if y<Min:
        y+=2
    pe.draw.rect(pe.color.gray,(0,y,data.mS[0],data.mS[1]-y),0)
    x = 0
    for app in data.apps:
      try:
        background = app[3].commons.background
      except:
        background = False
      if app[0] != "desktop" and app[0] != "tskBAR" and not background:
        if data.focus != app[0]:
          pe.button.rect((x,y,35,35),pe.color.darkgray,pe.color.verydarkgray,action=changefocus,data=app[0])
        else:
          pe.draw.rect(data.red3, (x,y,35,35),0)
        if y!=Min:
          try:
            icon = app[3].commons.icon
            pe.image.display(pe.image(icon, (35, 35), (x, y)))
          except:
            pe.draw.rect(pe.color.white, (x+5,y+10,25,15),0)
            pe.draw.rect(pe.color.verydarkgray, (x+5,y+10,25,5),0)
            pe.draw.circle(pe.color.red, (x+27,y+12),2,0)

            pe.draw.circle(pe.color.blue, (x+10,y+20),3,0)
            pe.draw.circle(pe.color.blue, (x+17,y+20),3,0)
            pe.draw.circle(pe.color.blue, (x+24,y+20),3,0)
        x+=40
  except:
    pass