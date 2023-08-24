data,lookup,pe,y,commons,os,apps=None,None,None,None,None,None,[]
def verify():
  return "app"
def init(dataV,lookupV):
  global data,lookup,pe,y,commons
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  class commonsV():
    icon = data.files + "reddy/icons/home.png"
  os = lookup.get("os")
  links = os.listdir(data.userDir()+"start/")
  i = 0
  while i<len(links)-1:
    if not ".redlink" in links[i]:
      del links[i]
      i=0
    i+=1
  for link in links:
    f = open(data.userDir()+"start/"+link)
    f.seek(0)
    read = f.read().splitlines()
    apps.append([link.replace(".redlink",""),read[0],data.files+read[1].replace("%USER%",data.current_user)])
    f.close()
  commons = commonsV
  y = data.mS[1] - 35
  return "home",9,2

def start(app):
  data.operations.append("run "+app)
  lookup.getapp("desktop").freeze = True

def drawApps(y):
  global apps
  ay=5
  for app in apps:
    pe.button.rect((5,ay+y,75,75),(0,0,0,0),(0,0,0,50),action=start,data=app[1])
    lookup.get("EZimage").image(app[2], (75, 75), (5, ay+y))
    ay+=75

def draw():
  global y
  size = data.mS[1]/1.5
  if data.focus == "home":
    mouse = lookup.get("mouse")
    if mouse.y() > data.mS[1]-size-35 and mouse.x() < data.mS[0]/3:
      if y>data.mS[1]-size-35:
        if (y-(data.mS[1]-size-35)/2)>data.mS[1]-size-35:
          y-=(data.mS[1]-size-35)/2
        else:
          y-=10
      else:
        y = data.mS[1]-size-35
    else:
      data.focus = ""
    lookup.getapp("tskBAR").locked = True
    pe.draw.rect(pe.color.black,(0,data.mS[1]-size-35,data.mS[0]/3,size+35),1)
    pe.draw.rect((0,0,0,100),(0,y,data.mS[0]/3,size+35),0)
    drawApps(y)
  else:
    y = data.mS[1] - 35
    lookup.getapp("tskBAR").locked = False