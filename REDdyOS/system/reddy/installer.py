data,lookup,os,pe,commons,framehost,FID,admin,file,zipF=None,None,None,None,None,None,None,None,None,None
def verify():
  return "app"
def init(dataV,lookupV,fileV):
  global data,lookup,os,commons,pe,framehost,FID,file,zipF
  data = dataV
  file = data.files+fileV
  lookup = lookupV
  class commonsV():
    icon = data.files + "reddy/icons/installer.png"
    window_size = (500,200)
    window_type = 0
    window_pos = data.common.window_pos
    title = "Installer"
  commons = commonsV
  os = lookup.get("os")
  pe = lookup.get("PGE")
  framehost = lookup.get("FHost")
  FID = framehost.setup("installer", commons)
  zipF=lookup.get("zipfile").ZipFile
  return "installer", 8, 2

ext=[]
def extract(fromP,toP):
    isThere = False
    with zipF(file, 'r') as zipObj:
        listOfFileNames = zipObj.namelist()
        for fileName in listOfFileNames:
            if fileName==fromP:
                zipObj.extract(fileName, toP)
                isThere=True
    ext.append(toP+fileName)
    return isThere
steps=0
ton=0
installinfo=None
installing=False
cleaning=False
def fix(path):
    path = path.replace("%APPDATA%",data.files+"data/Users/"+data.current_user+"/AppData")
    path = path.replace("%localAPPDATA%",data.files+"data/Users/local/AppData")
    return path
run=None
def addpackage(type,package,version):
    if type=="single":
        user=data.current_user
    else:
        user="local"
    try:
        dat = pe.load(data.files+"data/Users/"+user+"/packages.redinfo")
    except:
        dat = []
    ex=False
    x=0
    for i in dat:
        if i['package']==package:
            dat[i]['version']=version
            ex = True
            break
        x+=1
    if not ex:
        dat.append({'package':package,'version':version})
    pe.save(data.files+"data/Users/"+user+"/packages.redinfo",dat)
def ONEexit():
    data.operations.append("close installer")
def checkpackage(type,package,version=None):
    if type=="single":
        user=data.current_user
    else:
        user="local"
    try:
        dat = pe.load(data.files+"data/Users/"+user+"/packages.redinfo")
    except:
        dat = []
    ex=False
    for i in dat:
        if i['package']==package:
            if version!=None:
                if i['version'] == version:
                    ex = True
            else:
                ex=True
    return ex
additionals=[]
aton=0
ai=0
def install():
    global steps,ton,installing,run
    if not installing and ton < len(installinfo['install']):
        if steps == 2:
            try:
                require = installinfo['require']
                steps = 2.5
            except:
                steps = 3
                installing=True
        elif steps == 2.5:
            if lookup.get("downFile").check():
                for item in installinfo['require']:
                    if not checkpackage("user",item['package']) and not checkpackage("single",item['package']):
                        try:
                            link=item['link']
                        except:
                            lookup.get("downFile").downprotect("https://cpugames.000webhostapp.com/REDdyOS/pack.list",data.files+"data/temp/pack.list")
                            with open(data.files+"data/temp/pack.list") as f:
                                lib = f.readlines()
                                for i in lib:
                                    if i.split(" ")[0]==item:
                                        link = i.split(" ")[1]
                                f.close()
                        lookup.get("downFile").downprotect(link,data.files + "data/temp/"+item['package']+".redpack")

            else:
                steps=2.7

    elif ton < len(installinfo['install']):
        cur = installinfo['install'][ton]
        if cur['type']=="make_folder":
            try:
                os.makedirs(fix(cur['path']))
            except:
                pass
        elif cur['type']=="copy_file":
            if "%PACK%" in cur['from']:
                extract(cur['from'].replace("%PACK%/",""),fix(cur['to']))
        elif cur['type']=="shortcut":
            pe.save(data.files+"data/Users/"+data.current_user+"/Desktop/"+cur['name']+".redshort",fix(cur['to']),fix(cur['icon']))
        elif cur['type']=="login_run":
            with open(data.files + "data/Users/" + data.current_user +"/loggin.sys",'w') as f:
                f.write("run "+fix(cur['path']).replace(data.files,"")+'\n')
                f.close()
        elif cur['type']=="login_runadmin":
            with open(data.files + "data/Users/" + data.current_user +"/loggin.sys",'w') as f:
                f.write("runadmin "+fix(cur['path']).replace(data.files,"")+'\n')
                f.close()
        elif cur['type']=="run":
            run = fix(cur['path']).replace(data.files,"")
        ton+=1
        installing = True
        steps = 3
    else:
        installing=False
        addpackage(installinfo['install-type'], installinfo['package'], installinfo['version'])
        steps=4
def clean():
    global cleaning,steps,ton
    if ton < len(ext):
        try:
            os.remove(ext[ton])
        except:
            pass
        ton+=1
    else:
        cleaning=False
        steps=6
def runR():
    global run,steps
    data.operations.append("run "+run)
    data.operations.append("close installer")
def draw():
    global steps,installinfo,cleaning,ton
    framehost.draw(FID)
    framehost.screen(FID)
    if installing:
        lookup.get("_thread").start_new_thread(install,())
    elif cleaning:
        lookup.get("_thread").start_new_thread(clean, ())
    elif steps==4:
        ton=0
        cleaning=True
        steps+=1
    if steps==0:
        installI = data.files+"data/temp/install.redinfo"
        extract("install.redinfo",data.files+"data/temp/")
        installinfo=pe.load(installI)[0]
        steps+=1
    elif steps>0:
        if steps==1:
            commons.title="Installer - "+installinfo['name']
            extract("icon.png",data.files+"data/temp/")
            if checkpackage(installinfo['install-type'],installinfo['package'],installinfo['version']):
                steps+=0.5
            else:
                steps+=1
        elif steps>1 and steps<6:
            pe.fill.full(pe.color.white)
            if os.path.exists(data.files+"data/temp/icon.png",):
                lookup.get("EZimage").image(data.files+"data/temp/icon.png",(100,100),(5,5))
            else:
                lookup.get("EZimage").image(data.files + "reddy/icons/installation.png", (100, 100), (5, 5))
            if steps==2:
                pe.button.rect((500-155,200-40,150,35),(225,225,225),(200,200,200),Text=lookup.get("EZtext").size("Install",pe.color.black,(500-155,200-40,150,35)),action=install)
            elif steps==1.5:
                pe.button.rect((500 - 155, 200 - 40, 150, 35), (225, 225, 225), (200, 200, 200),Text=lookup.get("EZtext").size("Re-install", pe.color.black,(500 - 155, 200 - 40, 150, 35)), action=install)
            if steps!=2.5 and steps!=2.7:
                name = lookup.get("EZtext").size(installinfo['name'],pe.color.black,(110,5,500-115,25))
                package = lookup.get("EZtext").size(installinfo['package'],pe.color.black,(110,35,500-115,10),10)
                name.original_pos=(110,5)
                package.original_pos=(110,35)
                name.pos=(110,5)
                package.pos=(110,35)
                pe.text.display(lookup.get("EZtext").align.topleft(name))
                pe.text.display(lookup.get("EZtext").align.topleft(package))
            elif steps==2.5:
                detail = lookup.get("EZtext").size("additional packages, will be installed", pe.color.black, (110, 35, 500 - 115, 10), 10)
                detail.original_pos = (110, 35)
                detail.pos = (110, 35)
                pe.text.display(lookup.get("EZtext").align.center(detail))
                pe.button.rect((500 - 155, 200 - 40, 150, 35), (225, 225, 225), (200, 200, 200),Text=lookup.get("EZtext").size("OK", pe.color.black,(500 - 155, 200 - 40, 150, 35)), action=install)
                pe.button.rect((5, 200 - 40, 150, 35), (225, 225, 225), (200, 200, 200),Text=lookup.get("EZtext").size("Exit", pe.color.black,(500 - 155, 200 - 40, 150, 35)), action=ONEexit)
            elif steps==2.7:
                detail = lookup.get("EZtext").size("No Internet!", pe.color.red,(110, 35, 500 - 115, 10), 10)
                detail.original_pos = (110, 35)
                detail.pos = (110, 35)
                pe.text.display(lookup.get("EZtext").align.center(detail))
                pe.button.rect((500 - 155, 200 - 40, 150, 35), (225, 225, 225), (200, 200, 200),Text=lookup.get("EZtext").size("Exit", pe.color.black, (500 - 155, 200 - 40, 150, 35)),action=ONEexit)
            if steps==3:
                pe.slider.normal((0, 100, 500, 35, 20), (0, 255, 0), 0, len(installinfo['install']), ton, None, (0,255,0), 35,True, (255,255,255), 35)
            elif steps==5:
                pe.slider.normal((0, 100, 500, 35, 20), (0, 255, 0), 0, len(ext), ton, None, (0,255,0), 35,True, (255,255,255), 35)
        elif steps==6:
            try:
                os.remove(file)
            except:
                pass
            steps+=1
        elif steps==7:
            pe.fill.full(pe.color.white)
            if run!=None:
                if os.path.exists(data.files + "data/temp/icon.png", ):
                    lookup.get("EZimage").image(data.files + "data/temp/icon.png", (100, 100), (200, 5))
                else:
                    lookup.get("EZimage").image(data.files + "reddy/icons/installation.png", (100, 100), (200, 5))
                name = lookup.get("EZtext").size(installinfo['name'], pe.color.black, (0, 110, 500, 25))
                package = lookup.get("EZtext").size(installinfo['package'], pe.color.black, (0, 140, 500, 10),10)
                pe.text.display(name)
                pe.text.display(package)
                pe.button.rect((500 - 155, 200 - 40, 150, 35), (225, 225, 225), (200, 200, 200),Text=lookup.get("EZtext").size("Run", pe.color.black,(500 - 155, 200 - 40, 150, 35)), action=runR)
            else:
                steps+=1
        elif steps==8:
            data.operations.append("close installer")
            steps+=1






    framehost.exit(FID)