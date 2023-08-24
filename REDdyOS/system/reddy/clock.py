data,lookup,time=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,time
  data = dataV
  lookup = lookupV
  time = lookup.get("time")
  return "clock"


def second():
  return time.strftime("%S", time.localtime())
def minute():
  return time.strftime("%M", time.localtime())
def hour():
  return time.strftime("%H", time.localtime())
