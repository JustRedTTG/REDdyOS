data,lookup,tstr=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,tstr
  data = dataV
  lookup = lookupV
  tstr = lookup.get("tstr").tstr
  return "stgmng"

def get(data):
  class Settings():
    def setup(self):
      self.custom = []
      for d in data:
        x = d.split(" ")
        if x[0] == "theme":
          self.theme = int(x[1])
        elif x[0] == "red":
          self.red = tstr(x[1])
        elif x[0] == "red2":
          self.red2 = tstr(x[1])
        elif x[0] == "red3":
          self.red3 = tstr(x[1])
        elif x[0] == "red4":
          self.red4 = tstr(x[1])
        elif x[0] == "pfp":
          self.pfp = x[1]
        elif x[0] == "lock":
          self.lock = int(x[1])
        elif x[0] == "admin":
          if int(x[1]) == 1:
            self.admin = True
          else:
            self.admin = False
        else:
          self.custom.append(d)
      return self
  return Settings.setup(Settings)

def add(user,line):
  um = lookup.get("usrmng")
  user = um.load.user(user)
  f = open(user.path + "settings.sys")
  f.seek(0)
  data = f.read()
  f.close()
  data+="\n"+line
  f = open(user.path + "settings.sys","w+")
  f.seek(0)
  f.write(data)
  f.close()

def change(user, header, dataV):
  um = lookup.get("usrmng")
  user = um.load.user(user)
  f = open(user.path + "settings.sys","r")
  f.seek(0)
  data = f.read().splitlines()
  i=0
  while i<len(data):
    if data[i].split(" ")[0] == header:
      data[i] = header+" "+dataV
    i+=1
  text=""
  for d in data:
    text+=d+'\n'
  f = open(user.path + "settings.sys", "w+")
  f.seek(0)
  f.write(text)
  f.close()