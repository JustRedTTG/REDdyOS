data,lookup,os,pe,commons=None,None,None,None,None
def verify():
  return "app"
def init(dataV,lookupV):
  global data,lookup,os,commons,pe,framehost,FID
  data = dataV
  data.operations.append("screen 4")
  lookup = lookupV
  class commonsV():
    icon = data.files + "reddy/icons/settings.png"
    window_size = (650,500)
    window_type = 1
    window_pos = data.common.window_pos
    title = "Settings"
  commons = commonsV
  os = lookup.get("os")
  pe = lookup.get("PGE")
  return "settings", 9, 4
def close():
  data.operations.append("screen 2")
  data.operations.append("close settings")
screen=0
ticks=0
cubeyP=(0,0)
cubeyT=False
def title():
  pe.draw.rect(data.red4,(0,0,data.display_rect.width-40,25),0)
  pe.draw.rect(data.red4,(0,20,data.display_rect.width,5),0)
def option(o):
  global screen
  screen=2+o
def options():
  y=30
  l = data.files+"reddy/icons/settings/"
  pe.button.rect((0,y,250,40),data.red,data.red2,action=option,data=1)
  lookup.get("EZimage").image(l+"theme.png", (250, 40), (0, y))
  y+=40
  pe.button.rect((0, y, 250, 40), data.red, data.red2, action=option, data=2)
  lookup.get("EZimage").image(l + "users.png", (250, 40), (0, y))
def settheme(id):
  stgmng = lookup.get("stgmng")
  stgmng.change(data.current_user,"theme",str(id))
  data.theme=id
colorsRed= [(255,50,50),(50,255,50),(50,50,255),(255,255,50),(255,50,255),(50,255,255),(100,100,100)]
colorsRed2=[(255,100,100),(100,255,100),(100,100,255),(255,255,100),(255,100,255),(100,255,255),(150,150,150)]
colorsRed3=[(255,150,150),(150,255,150),(150,150,255),(255,255,150),(255,150,255),(150,255,255),(200,200,200)]
colorsRed4=[(255,200,200),(200,255,200),(200,200,255),(255,255,200),(255,200,255),(200,255,255),(255,255,255)]
def setcolors(id):
  stgmng = lookup.get("stgmng")
  tstr = lookup.get("tstr").strt
  data.red = colorsRed[id]
  data.red2 = colorsRed2[id]
  data.red3 = colorsRed3[id]
  data.red4 = colorsRed4[id]
  stgmng.change(data.current_user, "red", tstr(colorsRed[id]))
  stgmng.change(data.current_user, "red2", tstr(colorsRed2[id]))
  stgmng.change(data.current_user, "red3", tstr(colorsRed3[id]))
  stgmng.change(data.current_user, "red4", tstr(colorsRed4[id]))
def setpfp(image):
  stgmng = lookup.get("stgmng")
  stgmng.change(data.current_user, "pfp", image)
lastM=False
def draw():
  global cubeyP,cubeyT,ticks,screen,lastM
  lookup.get("mouse").remove_offset()
  if screen > 1:
    data.mS = (data.display_rect.width-250,data.display_rect.height-25)
    data.display_rect.center = pe.math.center((0,0,data.display_rect.width,data.display_rect.height))
    #data.display_rect.center = (data.display_rect.center[0],data.display_rect.center[1]-25)
    lookup.get("DrawATheme").draw(off=(250,25))
    rect = (250, 25, data.display_rect.width, data.display_rect.height)
    s = pe.Surface((rect[2], rect[3]))
    s.set_alpha(100)
    s.fill((0, 0, 0))
    pe.display.blit(s, (rect[0], rect[1]))
  #pe.draw.rect(pe.colors.pink,(250,25,data.display_rect.width,data.display_rect.height),15)
  data.mS = pe.display.get.size()
  data.display_rect.center = (data.display_rect.width / 2, data.display_rect.height / 2)
  pe.button.rect((data.display_rect.width-40,0,40,20),pe.colors.red,pe.colors.pink,action=close)
  if screen == 0:
    cubeyP = (data.display_rect.center[0]-200,data.display_rect.center[1])
    screen=1
  elif screen == 1:
    pe.fill.full(pe.colors.white)
    if ticks<35:
      if cubeyT:
        cubeyP = (cubeyP[0]-20,cubeyP[1])
      else:
        cubeyP = (cubeyP[0] + 20, cubeyP[1])
      if cubeyT and cubeyP[0] < data.display_rect.center[0]-200:
        cubeyT = False
      elif cubeyP[0] > data.display_rect.center[0]+200:
        cubeyT = True
      pe.draw.rect(pe.colors.red,(cubeyP[0]-50,cubeyP[1]-50,100,100),0)
      pe.draw.line(pe.colors.black, (cubeyP[0]-40,cubeyP[1]-40),(cubeyP[0]-30,cubeyP[1]-20),10)
      pe.draw.line(pe.colors.black, (cubeyP[0]-40,cubeyP[1]),(cubeyP[0]-30,cubeyP[1]-20),10)

      pe.draw.line(pe.colors.black, (cubeyP[0]+40,cubeyP[1]-40),(cubeyP[0]+30,cubeyP[1]-20),10)
      pe.draw.line(pe.colors.black, (cubeyP[0]+40,cubeyP[1]),(cubeyP[0]+30,cubeyP[1]-20),10)
      ticks+=1
    else:
      screen = 2
  elif screen > 1:
    pe.draw.rect(data.red,(0,0,250,data.display_rect.height),0)
    pe.draw.line(data.red4,(250,0),(250,data.display_rect.height),5)
    title()
    options()
    pe.Layer[0][0] = (250, 25)
    if screen == 3:
      #
      full = int(175 / 3)
      half = int(175 / 4)
      smol = int(175 / 8)
      vsmol = int(175 / 10)
      center = (int(175 / 2), 50)
      #
      screenS = pe.display.display_reference

      pe.button.rect((250+5,25+5,185,110),pe.colors.white,(200,200,200),action=settheme,data=0)
      pe.button.rect((250+25+175,25+5,185,110),pe.colors.white,(200,200,200),action=settheme,data=1)

      # THEME 1
      smallT = pe.Surface((175,100))
      pe.display.context(smallT)
      pe.fill.full(data.red)
      pe.draw.circle(data.red4, center, full, 0)
      pe.draw.circle(data.red3, center, half, 0)
      pe.draw.circle(data.red2, center, smol, 0)
      pe.draw.line(data.red, (0, center[1]), (175, center[1]), vsmol)
      pe.draw.line(data.red, (center[0], 0), (center[0], 100), vsmol)
      #
      # THEME 2
      smallT2 = pe.Surface((175, 100))
      pe.display.context(smallT2)
      pe.fill.full(data.red)
      ic = 25
      y = 0
      pe.draw.rect(data.red, (0, y, data.display_rect.width, ic), 0)
      y += ic
      pe.draw.rect(data.red2, (0, y, data.display_rect.width, ic), 0)
      y += ic
      pe.draw.rect(data.red3, (0, y, data.display_rect.width, ic), 0)
      y += ic
      pe.draw.rect(data.red4, (0, y, data.display_rect.width, ic), 0)
      #
      pe.display.context(screenS)
      pe.display.blit(smallT,(250+10,25+10))
      pe.display.blit(smallT2,(250+175+30,25+10))
      x=255
      pe.button.rect((x,205,50,50),pe.colors.white,(200,200,200),action=setcolors,data=0)
      pe.draw.rect(pe.colors.red,(x+5,210,40,40),0)
      x += 55
      pe.button.rect((x, 205, 50, 50), pe.colors.white, (200, 200, 200),action=setcolors,data=1)
      pe.draw.rect(pe.colors.green, (x + 5, 210, 40, 40), 0)
      x += 55
      pe.button.rect((x, 205, 50, 50), pe.colors.white, (200, 200, 200),action=setcolors,data=2)
      pe.draw.rect(pe.colors.blue, (x + 5, 210, 40, 40), 0)
      x += 55
      pe.button.rect((x, 205, 50, 50), pe.colors.white, (200, 200, 200),action=setcolors,data=3)
      pe.draw.rect((255,255,0), (x+5, 210, 40, 40), 0)
      x += 55
      pe.button.rect((x, 205, 50, 50), pe.colors.white, (200, 200, 200),action=setcolors,data=4)
      pe.draw.rect((255, 0, 255), (x + 5, 210, 40, 40), 0)
      x += 55
      pe.button.rect((x, 205, 50, 50), pe.colors.white, (200, 200, 200),action=setcolors,data=5)
      pe.draw.rect((0, 255, 255), (x + 5, 210, 40, 40), 0)
      x += 55
      pe.button.rect((x, 205, 50, 50), pe.colors.black, (200, 200, 200),action=setcolors,data=6)
      pe.draw.rect(pe.colors.white, (x + 5, 210, 40, 40), 0)
    elif screen >= 4 < 5:
      ezt=lookup.get("EZtext")
      circlepfp = lookup.get("circlepfp")
      sm = lookup.get("stgmng")
      um = lookup.get("usrmng")
      settings = sm.get(um.load.user(data.current_user).settings)
      pe.draw.ellipse(pe.colors.white,(260, 35,200,200))
      tsx = pe.math.tsx.make((360,135),100)
      if settings.pfp != "NONE":
        lookup.get("EZimage").image(circlepfp.username(data.current_user), (200, 200), (260, 35))
      else:
        lookup.get("EZimage").image(data.files + "reddy/icons/account.png",(200,200),(260,35))
      pos = pe.math.tsx.get(tsx,135)
      button = pe.pygame.Rect((pos[0]-22,pos[1]-22,44,44))
      mouse = lookup.get("mouse")
      cursor = pe.pygame.Rect((mouse.x()-2,mouse.y()-2,4,4))
      if button.colliderect(cursor):
        pe.draw.circle(data.red4, pos, 22, 0)
        if mouse.left() and not lastM:
          screen=4.1
      else:
        pe.draw.circle(data.red,pos,22,0)
      if screen == 4.1:
        pe.draw.circle(data.red2, pos, 22, 0)
        pe.draw.rect(data.red2,(pos[0],pos[1]-100,400,200),0)
        pe.button.rect((pos[0]+360,pos[1]-100,40,25),pe.colors.red,pe.colors.pink,action=option,data=2)
        defaults = lookup.get("os").listdir(data.files+"reddy/default")
        x,y=pos[0]+10,pos[1]-90
        for image in defaults:
          pe.button.rect((x-5,y-5,60,60),data.red2,data.red4,action=setpfp,data="reddy/default/"+image)
          lookup.get("EZimage").image(data.files + "reddy/default/"+image, (50, 50), (x, y))
          if x+45+40<pos[0]+400:
            x+=60
          else:
            x = pos[0]+10
            y+=60
    pe.Layer[0][0] = (0, 0)
  lastM = lookup.get("mouse").left()
