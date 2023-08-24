data,lookup,pe=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  return "key"
all=[False,False]
def getall():
  global all
  if data.events == None:
    data.events = pe.event.get()
  for pe.event.c in data.events:
    if pe.event.key_UP(32):
      all[0] = False
    elif pe.event.key_DOWN(32):
      all[0] = True
    if pe.event.key_UP(pe.pygame.K_RETURN):
      all[1] = False
    elif pe.event.key_DOWN(pe.pygame.K_RETURN):
      all[1] = True


def space():
  getall()
  return all[0]
def enter():
  getall()
  return all[1]