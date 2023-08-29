import traceback

import data, lookup
import pygameextra as pe
import os
import time
import importlib.util
import math
import random
from PIL import Image, ImageDraw
import numpy
import _thread
import requests
import zipfile
import socket

data.m = {"PGE": pe, "os": os, "time": time, "importlib.util": importlib.util, "math": math,
          "random": random, "PIL.Image": Image, "PIL.ImageDraw": ImageDraw, "numpy": numpy,
          "_thread": _thread, "requests": requests, "zipfile": zipfile, "socket": socket}
commons = data.m.keys()
pe.init()

m = [''] * 20
lock = [''] * 20
for x in range(20):
    m[x] = random.randint(0, 61)
lock[x] = m[x]
i = len(m) - 1
i1 = 0
fk = ''
key = random.randint(0, 61)
# print("o,o key",key)
while i1 < len(m):
    m[i1] = int(m[i1]) + key
    while m[i1] > 61:
        m[i1] -= 61
    i1 += 1
i1 = 0
while i1 < len(m):
    m[i1] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"[m[i1]]
    i1 += 1
i1 = 0
fk = ''.join(m)
key *= math.pi


def decript(key, lock):
    key = int(key)
    i1 = 0
    d = []
    while i1 < len(m):
        for i in range(62):
            if "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"[i] == lock[i1]:
                break
        g = i - key
        while g < 0:
            g += 61
        d.append(int(g))
        i1 += 1
    i1 = 0
    while i1 < len(d):
        d[i1] = int(d[i1]) + key
        while d[i1] > 61:
            d[i1] -= 61
        i1 += 1
    i1 = 0
    while i1 < len(d):
        d[i1] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"[int(d[i1])]
        i1 += 1
    return ''.join(d)


def gMS():
    global data
    data.display_rect = pe.display.display_reference.rect
    data.centerTSX = pe.TSX(data.display_rect.center, data.display_rect.width // 25)


pe.display.make((0, 0), "REDdyOS", 2)
gMS()
data.files = str(os.path.realpath(__file__)).replace("start.pyw", 'system/')
print(data.files)
f = open(data.files + "startup.sys")
f.seek(0)
startup = f.read().splitlines()
startupI = 0
log = True
logall = False
crashlog = True


def open_module(spath: str):
    spec = importlib.util.spec_from_file_location(os.path.basename(spath).replace(".py", ""), os.path.realpath(spath))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module_type = module.verify()
    return module, module_type


def add_app(name, priority, screen, module, admin: bool = False):
    data.apps[name] = {
        "priority": priority, "screen": screen, "module": module, "focus": 0, "admin": None
    }
    if admin:
        lookup.get("adminmng").admin = name
        lookup.get("adminmng").acceptapp(key / math.pi)


def run(spath, user="", dataV=None):
    global data, lookup, fk, key
    module, module_type = open_module(spath)
    if module_type == "module":
        name = module.init(data, lookup)
        if name == "adminmng":
            module.init(data, lookup, fk, key)
        data.m[name] = module
        if log:
            print("run module", name, user)
    elif module_type == "app":
        if dataV == None:
            moduledata = module.init(data, lookup)
        else:
            moduledata = module.init(data, lookup, dataV)
        name = moduledata[0]
        for app in data.apps:
            if app[0] == name:
                return
        priority = moduledata[1]
        screen = moduledata[2]
        add_app(name, priority, screen, module)
        data.focus = name
        if logall:
            print("run app", name, user)


def run_admin(spath, user=""):
    module, type = open_module(spath)
    global data, lookup, fk, key
    if type == "app":
        name, priority, screen = module.init(data, lookup)
        for app_name, _ in data.apps.items():
            if app_name == name:
                return
        add_app(name, priority, screen, module, admin=True)
        data.focus = name
        if logall:
            print("[admin] run app", name, user)


class adminoper:
    @staticmethod
    def close(app):
        if app != "":
            if logall:
                print("[admin] close app", app)
            i = 0
            while i < len(data.apps):
                if data.apps[i][0] == app:
                    del data.apps[i]
                    data.focus = ""
                    lookup.get("framehost").remove(app)
                    return
                else:
                    pass
                i += 1

    @staticmethod
    def stop(app):
        global commons
        if app != "" and not app in commons:
            if logall:
                print("[admin] stop module", app)
            i = 0
            while i < len(data.m):
                if data.m[i][0] == app:
                    del data.m[i]
                    return
                else:
                    pass
                i += 1

    @staticmethod
    def change_app(appname, new):
        try:
            app = data.apps[appname]

            app['module'] = new
            data.focus = ""

            if logall:
                print("[admin] change app", appname)
        except KeyError:
            raise LookupError(f"Couldn't find app name {appname}")

    @staticmethod
    def change_module(modulename, new):
        try:
            data.m[modulename] = new

            if logall:
                print("[admin] change module", modulename)
        except KeyError:
            raise LookupError(f"Couldn't find module {modulename}")

    @staticmethod
    def runadmin(spath, user=""):
        run_admin(data.files + spath, user)

    @staticmethod
    def runclass(module, name, screen, priority):
        module.init(data, lookup)
        add_app(name, priority, screen, module)

    @staticmethod
    def runadminclass(module, name, screen, priority):

        module.init(data, lookup)
        add_app(name, priority, screen, module, admin=True)


def runall(target_screen):
    global data, fk, adminoper

    # TODO: might only need this when switching focus or opening a new app, not every frame
    for app_name, app in data.apps.items():
        if app_name == data.focus:
            app['focus'] = 0
        else:
            app['focus'] += 1
    atr = [item for item in data.apps.items() if item[1]['screen'] == target_screen]
    all_priorities = []
    highest_focus = 0
    for _, app in atr:
        highest_focus = max(app['focus'], highest_focus)
        all_priorities.append(app['focus'])
    all_priorities = sorted(all_priorities)
    fsort = []
    if len(all_priorities) > 0:
        for i in range(len(all_priorities)):
            fsort.extend([item for item in atr if item[1]['focus'] == all_priorities[i]])
    psort = [[], [], [], [], [], [], [], [], [], [], []]
    for item in fsort:
        try:
            psort[item[1]['priority']].append(item)
        except IndexError:
            pass
    for prioritized_apps in psort:  # Per priority
        for name, app in prioritized_apps:  # Per app in priority
            if app["admin"] is not None and app['admin_key'] is not None:
                ll = ((app['admin'][1] * math.pi) / (app['admin_key'] + 1))
                if decript(ll, app['admin'][0]) == fk:
                    app['module'].admincall(adminoper)
            if not crashlog:
                try:
                    if logall and app['module'].draw is None:
                        print(f"DRAW call to {name}")
                    app[3].draw()
                except:
                    data.operations.append(f"close {name}")
            else:
                if logall:
                    print(f"DRAW call to {name}")
                app['module'].draw()


def runallm():
    for name, module in data.m.items():
        try:
            if name == 'adminmng' and data.screen != 0:
                module.admincall(adminoper)
                print(f"ADMINMNG granted")
            module.call()
            if logall:
                print(f"module call to {name}")
        except AttributeError:
            pass
        except:
            if crashlog:
                traceback.print_exc()


def endallm():
    global data
    for m in data.m:
        try:
            if logall and m[1].beforeendcall != None:
                print("module before end call to", m[0])
            m[1].beforeendcall()
        except:
            pass
    for m in data.m:
        try:
            if logall and m[1].endcall != None:
                print("module end call to", m[0])
            m[1].endcall()
        except:
            pass


def closeApp(app, user=""):
    try:
        del data.apps[app]
        data.focus = ""
        if logall:
            print("close app", app, user)

    except KeyError:
        pass


def closeModule(app, user=""):
    if app != "" and not app in commons:
        if logall:
            print("stop module", app, user)
        i = 0
        while i < len(data.m):
            if data.m[i][0] == app:
                # print("located at",i)
                del data.m[i]
                return
            else:
                # print("not at", i, data.m[i][0])
                pass
            i += 1
        # pe.error("couldn't stop the module")


def oper(x):
    x = x.split(" ")
    if x[0] == "run":
        try:
            run(data.files + x[1], x[2])
        except:
            run(data.files + x[1])
    if x[0] == "install":
        run(data.files + "reddy/installer.py", dataV=x[1])
    elif x[0] == "screen":
        data.screen = int(x[1])
    elif x[0] == "close":
        if x[1] == "tskBAR" or x[1] == "desktop" or x[1] == "home":
            if logall:
                print("attempt to close important app", x)
        else:
            try:
                closeApp(x[1], x[2])
            except:
                closeApp(x[1])
    elif x[0] == "stop":
        try:
            closeModule(x[1], x[2])
        except:
            closeModule(x[1])
    elif x[0] == "focus":
        data.focus = x[1]


def boot_animation(color):
    points = [data.centerTSX[rotation] for rotation in (0, 90, 180, 270)]
    eye_points = [pe.math.lerp_legacy(
        data.display_rect.center,
        data.centerTSX[rotation + 45],
        data.display_rect.width / 65)
        for rotation in [0, 180]]
    pe.draw.polygon(color, points)
    for eye_point in eye_points:
        pe.draw.circle(pe.colors.black, eye_point, data.display_rect.width / 120, 0)


pe.display.make(pe.display.get_max(), "REDdyOS", 1)

# section Main loop
while True:
    gMS()
    data.events = pe.event.get()
    if data.resetDis != None:
        pe.display.context(data.resetDis)
        data.resetDis = None
    if data.screen != 0:
        if logall:
            print("==RUNNING OPERATIONS==")
        for x in data.operations:
            oper(x)
        if logall:
            print("===end of call===")
        if logall:
            print("===start of call===")
        data.operations = []
    if len(data.apps) < 1 and data.killNoApps:
        exit()
    for pe.event.c in data.events:
        if pe.event.quitCheck():
            if data.focus != "":
                data.operations.append("close " + data.focus)
            else:
                exit()
    pe.fill.full(data.red)
    runallm()
    if data.screen == 0:
        pe.fill.full((20, 20, 20))

        try:
            if startup[startupI] == "boot":
                data.centerTSX.offset = int(data.centerTSX.offset)
                if int(data.centerTSX.offset / 45) - data.centerTSX.offset / 45 != 0:
                    boot_animation(data.red)
                    data.centerTSX.offset += 1
                else:
                    boot_animation(data.red)
                    pe.display.update()
                    time.sleep(1)
                    startupI += 1
            elif startup[startupI].split(" ")[0] == "screen":
                data.screen = int(startup[startupI].split(" ")[1])
                startupI += 1
            elif startup[startupI].split(" ")[0] == "run":
                boot_animation(data.red)
                data.centerTSX.offset += 1.5
                run(data.files + startup[startupI].split(" ")[1], "*STARTUP*")
                startupI += 1
            elif startup[startupI].split(" ")[0] == "runadmin":
                boot_animation(pe.colors.aqua)
                data.centerTSX.offset += 1.5
                run_admin(data.files + startup[startupI].split(" ")[1], "[admin] *STARTUP*")
                startupI += 1
            else:
                boot_animation(data.red)
                data.centerTSX.offset += 1.5
                startupI += 1
        except Exception as e:
            if len(data.operations) > 0:
                oper(data.operations[0])
                del data.operations[0]
            traceback.print_exc()
    elif data.screen == 1:
        runall(1)
    elif data.screen == 2:
        runall(2)
    elif data.screen == 3:
        runall(3)
    elif data.screen == 4:
        runall(4)
    endallm()
    pe.display.update()
    pe.time.tick(data.fps)
    data.fps = 150
    data.events = None
