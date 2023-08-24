data,lookup=None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup
  data = dataV
  lookup = lookupV
  return "lighten"

def lighten(color, d):
  color=list(color)
  color[0]+=d
  color[1]+=d
  color[2]+=d
  if color[0]>255:
    color[0] = 255
  if color[1]>255:
    color[1] = 255
  if color[2]>255:
    color[2] = 255
  return tuple(color)