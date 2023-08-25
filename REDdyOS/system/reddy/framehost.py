data,lookup,pe=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe
  data=dataV
  lookup=lookupV
  pe=lookup.get("PGE")
  return "FHost"
apps=[]
def setup(name,commons):
  ezd = lookup.get("EZdrag")
  p = commons.window_pos
  s = commons.window_size
  apps.append([name,
               commons,
               None,
               None,
               ezd.central.sizer((p[0]+s[0]-1,p[1]+s[1]+20-1),[(p[0]+150,p[1]+150),None],pe.colors.gray),
               (p[0] + s[0] - 1, p[1] + s[1] + 20 - 1),
               ezd.horizontal.pager((p[0] + s[0] - 11, p[1] + s[1]/2 + 20,10,s[1]),pe.colors.gray,pe.colors.black),
               ezd.vertical.pager((p[0] + s[0]/2,p[1]+s[1]+20-1,s[0],10),pe.colors.gray,pe.colors.black)
               ])
  return len(apps)-1

drag=False
lastM = False
def close(ID=None):
  data.operations.append("close "+apps[ID][0]+" *Frame-Host*")
  del apps[ID]
rem = None
appsRAN=[]
appsThis=[]
def screen(ID):
  global rem,appsRAN,appsThis
  try:
    rem = pe.display_a
    data.resetDis = rem
    pe.display.set(apps[ID][3])
    appsThis.append(ID)
    if ID not in appsRAN:
      appsRAN.append(ID)
  except:
    rem = pe.display_a
def exit(ID):
  global rem
  try:
    apps[ID][3]=pe.display_a
  except:
    return
  try:
    pe.display.set(rem)
  except:
    pe.error("couldn't change the display back")
  pos = apps[ID][1].window_pos
  pe.display.blit.rect(apps[ID][3],(pos[0],pos[1]+20))
  lookup.get("mouse").removeoff()
  if not drag:
    ezd = lookup.get("EZdrag")
    if apps[ID][1].window_type == 1:
      ezd.central.draw_sizer(apps[ID][4])
      #ezd.horizontal.draw_pager(apps[ID][6])
      #ezd.vertical.draw_pager(apps[ID][7])
def draw_frame(app,ID):
  global drag, lastM
  if True:
    mouse = lookup.get("mouse")
    mouse.removeoff()
    if data.focus == app[0]: # rect fill
      pe.draw.rect(data.red3,(app[1].window_pos[0],app[1].window_pos[1],app[1].window_size[0],20),0)
    else:
      pe.draw.rect(data.red4, (app[1].window_pos[0], app[1].window_pos[1], app[1].window_size[0], 20), 0)

    # X button
    if drag or lastM:
      pe.draw.rect(pe.colors.red, (app[1].window_pos[0] + app[1].window_size[0] - 35, app[1].window_pos[1], 35, 20), 0)
    else:
      pe.button.rect((app[1].window_pos[0] + app[1].window_size[0] - 35, app[1].window_pos[1], 35, 20), pe.colors.red,pe.colors.pink, action=close, data=ID)
    mouse.addoff()
    try:
      apps[ID]
    except:
      if rem != None:
        pe.display.set(rem)
      return
    apps[ID][3] = pe.pygame.Surface(app[1].window_size)
    buldge=3
    pe.draw.rect(pe.colors.black,(app[1].window_pos[0],app[1].window_pos[1],app[1].window_size[0],app[1].window_size[1]+20),buldge)
    pe.draw.line(pe.colors.black,(app[1].window_pos[0],app[1].window_pos[1]+20),(app[1].window_pos[0]+app[1].window_size[0],app[1].window_pos[1]+20),buldge)

def draw(ID):
  #print("framehost draw",ID)
  global drag,lastM
  try:
    app = apps[ID]
  except:
    return
  mouse = lookup.get("mouse")
  try:
    off = lookup.getapp(app[0]).commons.window_pos
    off = (off[0],off[1]+20)
  except:
    off = (0,0)
  if not drag and apps[ID][1].window_type == 1:
    lookup.get("mouse").removeoff()
    ezd = lookup.get("EZdrag")
    s1 = ezd.central.drag_sizer(apps[ID][4])
    #s2 = (ezd.horizontal.pager(apps[ID][6]),ezd.vertical.pager(apps[ID][7]))
    x = s1[0]
    y = s1[1]
    s = (x,y)
    p = apps[ID][1].window_pos
    apps[ID][4].x = x
    apps[ID][4].y = y
    apps[ID][6].x = x
    apps[ID][6].y = y/2
    apps[ID][7].x = x/2
    apps[ID][7].y = y


    apps[ID][1].window_size = (s[0] - p[0], s[1] - 20 - p[1])
  pe.mouse.off = (off[0]*-1,off[1]*-1)
  if True:
    rect = (app[1].window_pos[0], app[1].window_pos[1], app[1].window_size[0]-35, 20)
    if not drag:
      pos = mouse.pos()
      pos = list(pos)
      x = 0
      y = 0
      while pos[0] > app[1].window_pos[0]:
        pos[0]-=1
        x+=1
      while pos[1] > app[1].window_pos[1]:
        pos[1]-=1
        y+=1
      pos=tuple(pos)
      if mouse.x() > rect[0] and mouse.x() < rect[0] + rect[2] and mouse.y() > rect[1] and mouse.y() < rect[1] + rect[3] and mouse.left() and not lastM:
        apps[ID][2] = (x,y)
        data.operations.append("focus "+app[0]+" *Frame-Host*")
        drag = True
    if not drag and app[2] != None:
      apps[ID][2] = None
    if drag and app[2] != None:
      x=app[2][0]
      y=app[2][1]
      apps[ID][1].window_pos = (mouse.x()-x,mouse.y()-y)
      p = apps[ID][1].window_pos
      s = apps[ID][1].window_size
      apps[ID][4].x = p[0]+s[0]-1
      apps[ID][4].y = p[1]+s[1]+20-1
      apps[ID][4].block = [(p[0]+150,p[1]+150),None]
    if drag and not mouse.left():
      drag = False
  try:
    title = apps[ID][1].title
  except:
    title = app[0]
  draw_frame(app, ID)
  try:
    apps[ID]
  except:
    return
  pe.text.display(lookup.get("EZtext").cram(title,pe.colors.black,(apps[ID][1].window_pos[0],apps[ID][1].window_pos[1],apps[ID][1].window_size[0]-35,20)))
def clickOut():
  global lastM
  for app in apps:
    rect = (app[1].window_pos[0],app[1].window_pos[1]-20,app[1].window_size[0]+2,app[1].window_size[1]+22)
    mouse = lookup.get("mouse")
    if mouse.y() < data.display_rect.height-35 and data.focus != "home":
      if mouse.x() > rect[0] and mouse.x() < rect[0]+rect[2] and mouse.y() > rect[1] and mouse.y() < rect[1]+rect[3]:

        if data.focus != app[0] and not lastM:
          data.operations.append("focus "+app[0])

        return False
      else:
        return True
    else:
      return False
def remove():
  i = 0
  while i < len(apps):
    if apps[i] == app:
      del apps[i]
      return
    else:
      pass
    i += 1
def beforeendcall():
  global lastM,appsThis,appsRAN
  lastM = lookup.get("mouse").left()
  #for app in appsRAN:
  #  if not app in appsThis:
  #    draw(app)
  #    pos = apps[app][1].window_pos
  #    pe.display.blit.rect(apps[app][3], (pos[0], pos[1] + 20))
  appsThis=[]
