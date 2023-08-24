data,lookup=None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup
  data = dataV
  lookup = lookupV
  return "downFile"
def check():
  if lookup.get("socket").gethostbyname(lookup.get("socket").gethostname()) == "127.0.0.1":
    return False
  else:
    return True
def downprotect(link,file):
  requests = lookup.get("requests")
  response = requests.get(link)

  file = open(file, "wb")
  file.write(response.content)
  file.close()
def download(link,file):
  lookup.get("_thread").start_new_thread(downprotect,(link,file))
def checkdownload(link,file):
  if check():
    if not lookup.get("os").path.exists(file):
      download(link,file)
    return True
  else:
    return False