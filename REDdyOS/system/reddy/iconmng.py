data,lookup,os,pe=None,None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,os,pe,commons
  data = dataV
  lookup = lookupV
  os = lookup.get("os")
  pe = lookup.get("PGE")
  return "iconmng"

drag = None
lastM = False
counterpos = (0,0)

selects = []
double=[False,10]
doubleC = False
def commonIcons(file):
  if "." in file:
    dot = file.split(".")
    ext = dot[len(dot)-1]
    if os.path.exists(data.files+"reddy/icons/ext/"+ext+".png"):
      return data.files+"reddy/icons/ext/"+ext+".png"
    else:
      return data.files + "reddy/icons/ext/file.png"
  else:
    return data.files+"reddy/icons/ext/file.png"
  return None

def drawIcon(rect,file,window_pos=(0,0),icon=None):
  global double,doubleC
  mouse = lookup.get("mouse")
  if mouse.x()-window_pos[0] > rect[0] and mouse.x()-window_pos[0] < rect[0] + rect[2] and mouse.y()-window_pos[1]-20 > rect[1] and mouse.y()-window_pos[1]-20 < rect[1] + rect[3] and mouse.left() and not double[0] and not lastM:
    double=[True,10,rect]
  elif double[1]>0:
    if mouse.left() and not lastM:
      doubleC = True
    else:
      double[1]-=1
  elif double[1]<=0:
    double=[False,10]
  s = pe.Surface((rect[2], rect[3]))
  if file in selects:
    s.set_alpha(150)
    s.fill((255, 255, 255))
  elif mouse.x()-window_pos[0] > rect[0] and mouse.x()-window_pos[0] < rect[0] + rect[2] and mouse.y()-window_pos[1]-20 > rect[1] and mouse.y()-window_pos[1]-20 < rect[1] + rect[3]:
    s.set_alpha(100)
    s.fill((255, 255, 255))
  else:
    s.set_alpha(0)
    s.fill((255, 255, 255))
  pe.display.blit(s, (rect[0], rect[1]))
  textRect = (rect[0],rect[1]+rect[3]-20,rect[2],20)
  iconSize = rect[3]-20
  iconPos = (rect[0]+rect[2]/2-iconSize/2,rect[1])
  sm = lookup.get("stgmng")
  um = lookup.get("usrmng")
  s = sm.get(um.load.user(data.current_user).settings)
  showExt = False
  write = True
  for d in s.custom:
    x = d.split(" ")
    if x[0] == "iconmng:":
      if x[1] == "ShowExt":
        write = False
        if x[2] == "True":
          showExt = True
        else:
          showExt = False
  if write:
    sm.add(data.current_user,"iconmng: ShowExt False")
  ezt = lookup.get("EZtext")
  fln = os.path.basename(file)
  if not showExt and "." in fln:
    flns = fln.split(".")
    ext = flns[len(flns)-1]
    del flns[len(flns)-1]
    t = ""
    for x in flns:
      t = t+x+"."
    fln = t[0:len(t)-1]
  else:
    flns = fln.split(".")
    ext = flns[len(flns) - 1]
  if ext == "redshort":
    file,icon = pe.load(file)
    ext="py"
  if ext == "py":
    normal = False
    try:
      util = lookup.get("importlib.util")
      spec = util.spec_from_file_location("try", os.path.realpath(file))
      m = util.module_from_spec(spec)
      spec.loader.exec_module(m)
      if m.verify() == "app":
        try:
          m.init(data,lookup,False)
        except:
          m.init(data, lookup)
        try:
          fln = m.commons.name
        except:
          try:
            fln=m.commons.title
          except:
            pass
        try:
          if lookup.get("os").path.exists(m.commons.icon):
            lookup.get("EZimage").image(m.commons.icon, (iconSize, iconSize), iconPos)
          else:
            normal=True
        except:
          normal=True
        if double[0]:
          if not mouse.x()-window_pos[0] > double[2][0] and mouse.x()-window_pos[0] < double[2][0] + double[2][2] and mouse.y()-window_pos[1]-20 > double[2][1] and mouse.y()-window_pos[1]-20 < double[2][1] + double[2][3]:
            doubleC = False
            double = [False, 0]
          elif mouse.x()-window_pos[0] > double[2][0] and mouse.x()-window_pos[0] < double[2][0] + double[2][2] and mouse.y()-window_pos[1]-20 > double[2][1] and mouse.y()-window_pos[1]-20 < double[2][1] + double[2][3] and doubleC:
            data.operations.append("run "+file.replace(data.files,""))
            doubleC=False
            double=[False,0]
      else:
        normal = True
    except:
      normal=True
  elif ext == "redpack":
    normal=True
    if double[0]:
      if not mouse.x() - window_pos[0] > double[2][0] and mouse.x() - window_pos[0] < double[2][0] + double[2][2] and mouse.y() - window_pos[1] - 20 > double[2][1] and mouse.y() - window_pos[1] - 20 < double[2][1] + double[2][3]:
        doubleC = False
        double = [False, 0]
      elif mouse.x() - window_pos[0] > double[2][0] and mouse.x() - window_pos[0] < double[2][0] + double[2][2] and mouse.y() - window_pos[1] - 20 > double[2][1] and mouse.y() - window_pos[1] - 20 < double[2][1] + double[2][3] and doubleC:
        data.operations.append("install " + file.replace(data.files, ""))
        doubleC = False
        double = [False, 0]
  else:
    normal = True
  if normal:
    if icon != None and lookup.get("os").path.exists(icon):
      lookup.get("EZimage").image(icon, (iconSize, iconSize), iconPos)
    else:
      pe.draw.rect(pe.colors.white, (iconPos[0], iconPos[1], iconSize, iconSize), 0)
  pe.text.display(ezt.cram(fln,data.red4,textRect))
  return [rect,file,window_pos,icon]

def endcall():
  global lastM,selecting
  mouse = lookup.get("mouse")
  lastM = mouse.left()
  if not lastM:
    selecting = False

selecting = False
Sstart=(0,0)
def selecter(rect,icons):
  global selecting,Sstart
  mouse = lookup.get("mouse")
  if not lastM and mouse.left() and not selecting:
    selecting = True
    Sstart = mouse.pos()
  elif selecting:
    pass