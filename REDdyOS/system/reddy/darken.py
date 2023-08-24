data,lookup=None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup
  data = dataV
  lookup = lookupV
  return "darken"

def darken(color, d):
  color=list(color)
  color[0]-=d
  color[1]-=d
  color[2]-=d
  if color[0]<0:
    color[0] = 0
  if color[1]<0:
    color[1] = 0
  if color[2]<0:
    color[2] = 0
  return tuple(color)