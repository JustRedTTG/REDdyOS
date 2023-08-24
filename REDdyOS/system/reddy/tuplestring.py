data,lookup=None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup
  data = dataV
  lookup = lookupV
  return "tstr"

def tstr(s):
  s = s.replace("(","").replace(")","").replace(" ","")
  t = tuple(s.split(","))
  if len(t) == 2:
    t = (int(t[0]),int(t[1]))
  elif len(t) == 3:
    t = (int(t[0]), int(t[1]),int(t[2]))
  elif len(t) == 4:
    t = (int(t[0]), int(t[1]),int(t[2]),int(t[3]))
  elif len(t) == 5:
    t = (int(t[0]), int(t[1]),int(t[2]),int(t[3]),int(t[4]))
  elif len(t) == 6:
    t = (int(t[0]), int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]))
  return t
def strt(t):
  s = "("
  for i in t:
    s+=str(int(i))+","
  s=s[:-1]+")"
  return s