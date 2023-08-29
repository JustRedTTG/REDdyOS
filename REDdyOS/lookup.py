import pygameextra as pe
import data
import __main__ as main

library = {
    "darken": "reddy/darken.py",
    "clock": "reddy/clock.py",
    "key": "reddy/key.py",
    "mouse": "reddy/mouse.py",
    "tokenmng": "reddy/tokenmng.py",
    "tstr": "reddy/tuplestring.py",
    "stgmng": "reddy/stgmng.py",
    "usrmng": "reddy/usrmng.py",
    "iconmng": "reddy/iconmng.py",
    "adminmng": "reddy/adminmng.py",
    "DrawATheme": "reddy/themes.py",
    "FHost": "reddy/framehost.py",
    "hcircle": "reddy/halfcircle.py",
    "tskBAR": "reddy/taskbar.py",
    "settings": "reddy/apps/settings.py",
    "circlepfp": "reddy/circlepfp.py",
    "lighten": "reddy/lighten.py",
    "downFile": "reddy/downFile.py",
    "alpha": "reddy/alpha.py",

    "EZimage": "reddy/easyImage.py",
    "EZtext": "reddy/easytext.py",
    "EZround": "reddy/roundness.py",
    "EZdrag": "reddy/easydrags.py",
}


def get(moduleN):
    # print("LOOKUP get module",moduleN)
    module = data.m.get(moduleN)
    if module is not None:
        return module
    module_file = library.get(moduleN)
    if module_file:
        main.run(data.files + module_file, "*LookUP*")
        return get(moduleN)
    pe.fill.full(data.red)
    pe.display.update()
    print(f"couldn't find module {moduleN}")
    exit()


def getapp(appN):
    if appN == "NONE" or appN == "":
        return
    app = data.apps.get(appN)
    if app is not None:
        return app
    app_file = library.get(appN)
    if app_file:
        main.run(data.files + app_file, "*LookUP*")
        return getapp(appN)
    pe.fill.full(data.red)
    pe.display.update()
    print(f"couldn't find app {appN}")
    exit()
