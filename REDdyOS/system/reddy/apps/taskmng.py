data,lookup,pe,commons,framehost,FID=None,None,None,None,None,None
def verify():
  return "app"
def init(dataV,lookupV):
  global data,lookup,commons,pe,framehost,FID
  data = dataV
  lookup = lookupV
  class commonsV():
    icon = data.files + "reddy/icons/taskmng.png"
    window_size = (500,500)
    window_type = 1
    window_pos = data.common.window_pos
    title = "Task manager"
  commons = commonsV
  pe = lookup.get("PGE")
  framehost = lookup.get("FHost")
  FID = framehost.setup("taskmng", commons)
  return "taskmng", 8, 2
page = 0
def setpage(p):
  global page
  page = p
def close(name):
  data.operations.append("close "+name)
def stop(name):
  data.operations.append("stop "+name)
def draw():
  framehost.draw(FID)
  framehost.screen(FID)

  pe.fill.full((225,225,225))
  ezt = lookup.get("EZtext")
  pe.draw.line(pe.color.black,(0,20),(commons.window_size[0],20),2)
  if page != 0:
    pe.button.rect((0,0,50,20),(255,255,255),(200,200,200),Text=ezt.size("apps",pe.color.black,(0,0,50,20),10),action=setpage, data=0)
  else:
    pe.draw.rect((200,200,200),(0,0,50,20),0)
    pe.text.display(ezt.size("apps",pe.color.black,(0,0,50,20),10))
  if page != 1:
    pe.button.rect((50,0,50,20),(255,255,255),(200,200,200),Text=ezt.size("modules",pe.color.black,(50,0,50,20),10),action=setpage, data=1)
  else:
    pe.draw.rect((200,200,200),(50,0,50,20),0)
    pe.text.display(ezt.size("modules",pe.color.black,(50,0,50,20),10))


  y=22
  if page == 0:
    for app in data.apps:
      name = app[0]
      pe.text.display(ezt.align.topleft(ezt.size(name,pe.color.black,(0,y,0,10),7)))
      pe.button.rect((commons.window_size[0]-100,y,100,10),pe.color.red,pe.color.pink,action=close,data=name)
      y+=12
  elif page == 1:
    for m in data.m:
      name = m[0]
      pe.text.display(ezt.align.topleft(ezt.size(name,pe.color.black,(0,y,0,10),7)))
      pe.button.rect((commons.window_size[0]-100,y,100,10),pe.color.red,pe.color.pink,action=stop,data=name)
      y+=12
  framehost.exit(FID)