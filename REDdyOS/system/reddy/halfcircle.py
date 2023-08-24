data,lookup,pe=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  return "hcircle"

def bottom(color, pos, r, w):
  tsx = pe.math.tsx.make(pos,r)
  rotation = 90
  tp = []
  while rotation != 90+180:
    tp.append(pe.math.tsx.get(tsx,rotation))
    rotation+=1
  pe.draw.polygon(color,*tp,width=w)
def tom(color, pos, r, w):
  tsx = pe.math.tsx.make(pos,r)
  rotation = -90
  tp = []
  while rotation != 90:
    tp.append(pe.math.tsx.get(tsx,rotation))
    rotation+=1
  pe.draw.polygon(color,*tp,width=w)