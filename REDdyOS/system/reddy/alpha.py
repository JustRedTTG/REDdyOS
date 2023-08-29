data,lookup,pe=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe
  data = dataV
  lookup = lookupV
  pe=lookup.get("PGE")
  return "alpha"

def alpha(color,aplha,rect):
  s = pe.Surface((rect[2], rect[3]))
  s.set_alpha(aplha)
  s.fill(color)
  pe.display.blit.rect(s, (rect[0], rect[1]))