data,lookup,os=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,os
  data = dataV
  lookup = lookupV
  os = lookup.get("os")
  return "usrmng"

usernames = []

class load():
  def users():
    f = open(data.files+"data/Users/user info.redi")
    f.seek(0)
    global usernames
    usernames = f.read().splitlines()
    f.close()
  def user(nameV):
    class User:
      def setup(self):
        self.name = nameV
        self.path = data.files+"data/Users/"+nameV+"/"
        f = open(self.path+"settings.sys")
        f.seek(0)
        self.settings = f.read().splitlines()
        f.close()
        return self
    return User.setup(User)