data,lookup,timeT,nameT=None,None,None,None
def verify():
  return "app"
localSettings=None
def getS(username):
  global localSettings
  um = lookup.get("usrmng")
  sm = lookup.get("stgmng")
  settings = sm.get(um.load.user(username).settings)
  localSettings = settings
  return settings
def setTheme(settings):
  data.theme = settings.theme
  data.red = settings.red
  data.red2 = settings.red2
  data.red3 = settings.red3
  data.red4 = settings.red4

def init(dataV,lookupV):
  global data,lookup,timeT,nameT
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  timeT = pe.text.make('--:--', 'freesansbold.ttf', int(data.mS[0]/20), pe.math.center((0, data.center[1], data.center[0]/2, data.mS[1]/2)),(pe.color.black, None))
  nameT = pe.text.make('', 'freesansbold.ttf', int(data.mS[0]/20),data.center,(pe.color.black, None))
  tm = lookup.get("tokenmng")
  tm.load()
  settings = getS(tm.current_user)
  setTheme(settings)
  return "lockscreen",10,1
admin=None
def admincall(a):
  global admin
  admin=a
locked = True
d=0
text = None

def openUP():
  global locked,text
  locked = False
  lookup.get("usrmng").load.users()
  lookup.get("tokenmng").load()
  pe = lookup.get("PGE")
  ezt = lookup.get("EZtext")
  if localSettings.lock == 0:
    text = ezt.fit("Login", pe.color.black, (data.center[0] - int(data.mS[0] / 10 / 2), data.center[1] + int(data.mS[0] / 20 / 2), int(data.mS[0] / 10),int(data.mS[0] / 35)))

def unlock(code=""):
  tm = lookup.get("tokenmng")
  um = lookup.get("usrmng")
  user = um.load.user(tm.current_user)
  if localSettings.lock == 0:
    data.current_user = user.name
    data.operations.append("screen 2 *LockScreen*")
    data.operations.append("run reddy/taskbar.py *LockScreen*")
    data.operations.append("run reddy/iconmng.py *LockScreen*")
    data.operations.append("run reddy/desktop.py *LockScreen*")
    data.operations.append("run reddy/home.py *LockScreen*")
    data.operations.append('focus NONE *LockScreen*')
    data.operations.append("close lockscreen *LockScreen*")
    data.operations.append("run reddy/framehost.py *LockScreen*")
    if lookup.get("os").path.exists(data.files+"data/Users/"+user.name+"/loggin.sys"):
      with open(data.files+"data/Users/"+user.name+"/loggin.sys") as f:
        f.seek(0)
        v = f.readlines()
        f.close()
      for iv in v:
        if not "runadmin" in iv:
          data.operations.append(iv.replace("\n","")+" *LockScreen*")
        elif iv.split(" ")[0] == "runadmin":
          admin.runadmin(iv.replace("\n","").replace("runadmin ",""),"*LockScreen*")
def draw():
  global d,locked,text
  pe = lookup.get("PGE")
  if d<data.mS[1]/4 and not locked:
    d+=10
  elif d<data.mS[1]/2 and not locked:
    d+=20
  elif d<data.mS[1] and not locked:
    d+=30
  red = data.red
  red2 = data.red2
  red3 = data.red3
  red4 = data.red4
  pe.fill.full(red)
  lookup.get("DrawATheme").draw(red,red2,red3,red4)
  if locked:
    clock = lookup.get("clock")
    keyM = lookup.get("key")
    mouseM = lookup.get("mouse")
    timeT.text = str(clock.hour())+":"+str(clock.minute())
    timeT.original_pos = pe.math.center((0, data.center[1], data.center[0]/2, data.mS[1]/2))
    timeT.fontsize = int(data.mS[0]/20)
    timeT.init(timeT)
    pe.text.display(timeT)
    if keyM.space() or mouseM.left() or mouseM.right() or mouseM.middle():
      openUP()
  elif d<data.mS[1]:
    clock = lookup.get("clock")
    timeT.text = str(clock.hour()) + ":" + str(clock.minute())
    timeT.original_pos = pe.math.center((0, data.center[1]-d, data.center[0] / 2, data.mS[1] / 2-d))
    timeT.fontsize = int(data.mS[0] / 20)
    timeT.init(timeT)

    rect = (0,data.mS[1]-d,data.mS[0],data.mS[1])
    s = pe.pygame.Surface((rect[2], rect[3]))
    s.set_alpha((d/50)*(data.mS[1]/100))
    s.fill((0, 0, 0))
    pe.display.blit.rect(s, (rect[0], rect[1]))

    pe.text.display(timeT)
  else:
    um = lookup.get("usrmng")
    tm = lookup.get("tokenmng")

    rect = (0, 0,data.mS[0],data.mS[1])
    s = pe.pygame.Surface((rect[2], rect[3]))
    s.set_alpha(100)
    s.fill((0, 0, 0))
    pe.display.blit.rect(s, (rect[0], rect[1]))

    #pe.draw.circle(pe.color.white,(data.center[0],data.center[1]-int(data.mS[1] / 4)),int(data.mS[0] / 12),0)
    user = um.load.user(tm.current_user)
    if localSettings.pfp != "NONE":
      lookup.get("EZimage").image(lookup.get("circlepfp").username(user.name), (int(data.mS[0] / 6), int(data.mS[0] / 6)), (data.center[0]-int(data.mS[0] / 12), data.center[1]-int(data.mS[1] / 4)-int(data.mS[0] / 12)))
    else:
      lookup.get("EZimage").image(data.files + "reddy/icons/account.png", (int(data.mS[0] / 6), int(data.mS[0] / 6)), (data.center[0] - int(data.mS[0] / 12), data.center[1] - int(data.mS[1] / 4) - int(data.mS[0] / 12)))
    nameT.text = user.name
    nameT.original_pos = data.center
    nameT.init(nameT)
    nameT.fontsize = int(data.mS[0] / 20)
    pe.text.display(nameT)
    if localSettings.lock == 0:
      pe.button.rect((data.center[0]-int(data.mS[0] / 10/2),data.center[1]+int(data.mS[0] / 20/2),int(data.mS[0] / 10),int(data.mS[0] / 35)),(200,200,200),(100,100,100),text,action=unlock)
