data,lookup,pe,icons=None,None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe,icons
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  class icons:
    path = data.files + "reddy/icons/EZ/drags/"
    Hpager = path + "Hpager.png"
    Vpager = path + "Vpager.png"
    sizer = path + "sizer.png"
  return "EZdrag"

drags = []
drag = None
lastM = False

class horizontal:
  #PAGER
  def pager(rect,background,arrows):
    class Pager:
      def setup(self):
        self.back = background
        self.arrow = arrows
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.ID = 0
        if len(drags) > 0:
          f = True
          while f:
            g = False
            for i in drags:
              if i != None:
                if i[0] >= self.ID:
                  self.ID=i[0]+1
                  g=True

              g=True
            f=g
        self.type = 0
        return self
    return Pager.setup(Pager)
  def drag_pager(p):
    global drag, lastM
    p.rect = (p.x - p.width / 2, p.y - p.height / 2, p.width, p.height)
    mouse = lookup.get("mouse")
    if mouse.Wx() > p.rect[0] and mouse.Wx() < p.rect[0] + p.rect[2] and mouse.Wy() > p.rect[1] and mouse.Wy() < p.rect[1] + p.rect[3]:
      mouse.seticon(icons.Hpager,True)
      if not lastM and drag == None and mouse.left():
        pos = mouse.pos()
        pos = list(pos)
        x = 0
        y = 0
        while pos[0] > p.x:
          pos[0] -= 1
          x += 1
        while pos[1] > p.y:
          pos[1] -= 1
          y += 1

        drag = [p, x, y, p.type, "pager"]
    return p.x
  def draw_pager(p):
    p.rect = (p.x - p.width / 2, p.y - p.height / 2, p.width, p.height)
    pe.draw.rect(p.back, p.rect, 0)
    pe.draw.line(p.arrow, (p.x, p.y - p.height / 2), (p.x, p.y + p.height / 2), 2)

class vertical:
  #PAGER
  def pager(rect,background,arrows):
    class Pager:
      def setup(self):
        self.back = background
        self.arrow = arrows
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.ID = 0
        if len(drags) > 0:
          f = True
          while f:
            g = False
            for i in drags:
              if i != None:
                if i[0] >= self.ID:
                  self.ID=i[0]+1
                  g=True

              g=True
            f=g
        self.type = 1
        return self
    return Pager.setup(Pager)
  def drag_pager(p):
    global drag,lastM
    p.rect = (p.x - p.width / 2, p.y - p.height / 2, p.width, p.height)
    mouse = lookup.get("mouse")
    if mouse.Wx() > p.rect[0] and mouse.Wx() < p.rect[0] + p.rect[2] and mouse.Wy() > p.rect[1] and mouse.Wy() < p.rect[1] + p.rect[3]:
      mouse.seticon(icons.Vpager,True)
      if not lastM and drag == None and mouse.left():
        pos = mouse.Wpos()
        pos = list(pos)
        x = 0
        y = 0
        while pos[0] > p.x:
          pos[0] -= 1
          x += 1
        while pos[1] > p.y:
          pos[1] -= 1
          y += 1

        drag = [p, x, y, p.type, "pager"]
    return p.y
  def draw_pager(p):
    p.rect = (p.x - p.width / 2, p.y - p.height / 2, p.width, p.height)
    pe.draw.rect(p.back, p.rect, 0)
    pe.draw.line(p.arrow, (p.x - p.width / 2,p.y), (p.x + p.width / 2,p.y), 2)

class central:
  def sizer(pos, block, background):
    class Sizer:
      def setup(self):
        self.block = block
        self.back = background
        self.x = pos[0]-5
        self.y = pos[1]-5
        self.width = 10
        self.height = 10
        self.ID = 0
        if len(drags) > 0:
          f = True
          while f:
            g = False
            for i in drags:
              if i != None:
                if i[0] >= self.ID:
                  self.ID=i[0]+1
                  g=True

              g=True
            f=g
        self.type = 2
        return self
    return Sizer.setup(Sizer)
  def drag_sizer(s):
    global drag, lastM
    s.rect = (s.x - s.width / 2, s.y - s.height / 2, s.width, s.height)
    mouse = lookup.get("mouse")
    mouse.remove_offset()
    if mouse.Wx() > s.rect[0] and mouse.Wx() < s.rect[0] + s.rect[2] and mouse.Wy() > s.rect[1] and mouse.Wy() < s.rect[1] + s.rect[3]:
      mouse.seticon(icons.sizer,True)
      if not lastM and drag == None and mouse.left():
        pos = mouse.Wpos()
        pos = list(pos)
        x = 0
        y = 0
        while pos[0] > s.x:
          pos[0] -= 1
          x += 1
        while pos[1] > s.y:
          pos[1] -= 1
          y += 1

        drag = [s, x, y, s.type, "sizer"]
    mouse.add_offset()
    return (s.x,s.y)
  def draw_sizer(s):
    s.rect = (s.x - s.width / 2, s.y - s.height / 2, s.width, s.height)
    pe.draw.rect(pe.colors.white,s.rect,3)
    pe.draw.rect(pe.colors.black,s.rect,2)
    pe.draw.rect(s.back,s.rect,0)

def call():
  global drag
  mouse = lookup.get("mouse")
  mouse.remove_offset()
  if lastM and not mouse.left():
    drag = None
  if drag != None:
    if drag[4] == "pager":
      if drag[3] == 0:
        mouse.seticon(icons.Hpager, True)
        drag[0].x = mouse.x() - drag[1]
      elif drag[3] == 1:
        mouse.seticon(icons.Vpager, True)
        drag[0].y = mouse.y() - drag[2]
    if drag[4] == "sizer":
      mouse.seticon(icons.sizer, True)
      drag[0].x = mouse.Wx() - drag[1]
      drag[0].y = mouse.Wy() - drag[2]

      if drag[0].x < drag[0].block[0][0]:
        drag[0].x = drag[0].block[0][0]
      if drag[0].y < drag[0].block[0][1]:
        drag[0].y = drag[0].block[0][1]

      if drag[0].x > drag[0].block[1][0]:
        drag[0].x = drag[0].block[1][0]
      if drag[0].y > drag[0].block[1][1]:
        drag[0].y = drag[0].block[1][1]
  mouse.add_offset()

def endcall():
  global lastM
  mouse = lookup.get("mouse")
  lastM = mouse.left()