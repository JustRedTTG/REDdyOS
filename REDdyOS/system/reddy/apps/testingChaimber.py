data, lookup, os, pe, commons, framehost, FID, admin = None, None, None, None, None, None, None, None


def verify():
    return "app"


def init(dataV, lookupV):
    global data, lookup, os, commons, pe, framehost, FID
    data = dataV
    lookup = lookupV
    commons = {
        'icon': data.files + "reddy/icons/tch.png",
        'window_size': (500, 500),
        'window_type': 1,
        'window_pos': data.common.window_pos,
        'title': "Testing Chaimber!"
    }
    os = lookup.get("os")
    pe = lookup.get("PGE")
    framehost = lookup.get("FHost")
    FID = framehost.setup("tch", commons)
    return "tch", 8, 2


def reboot():
    global admin
    data.operations.append("screen 0")
    for m in data.m:
        if admin != None:
            admin.stop(m[0])
        else:
            data.operations.append("stop " + m[0])
        data.operations.append("begin " + m[0])
    for app in data.apps:
        if admin != None:
            admin.close(app[0])
        else:
            data.operations.append("close " + app[0])
    data.operations.append("screen 2")
    data.operations.append("run reddy/apps/testingChaimber_resetinfo.py")


def getadmin():
    lookup.get("adminmng").getadmin("tch")


def hackadmin():
    am = lookup.get("adminmng")
    am.admin = 'tch'
    am.acceptapp(5 / lookup.get("math").pi)


ctext = None
show = False


def admincall(adminV):
    global admin
    admin = adminV


enable = True


def kill():
    global enable
    enable = False


def draw():
    if enable:
        global ctext, show, admin
        framehost.draw(FID)
        framehost.screen(FID)
        mouse = lookup.get("mouse")
        pe.fill.full(pe.colors.white)
        pe.draw.circle(pe.colors.red, mouse.pos(), 5, 0)
        pe.draw.circle(pe.colors.green, mouse.Wpos(), 5, 0)
        pe.button.rect((0, 0, 50, 50), pe.colors.red, pe.colors.blue, action=reboot)
        pe.button.rect((100, 0, 50, 50), pe.colors.red, pe.colors.blue, action=kill)
        if not lookup.get("adminmng").check("tch"):
            if not "tch" in lookup.get("adminmng").decline:
                pe.button.rect((50, 0, 50, 50), pe.colors.red, pe.colors.blue, action=getadmin)
                # pe.button.rect((75, 50, 25, 25), pe.colors.red, pe.colors.purple, action=hackadmin)
            else:
                pe.draw.rect(pe.colors.black, (60, 10, 30, 30), 0)
        elif admin == None:
            pe.draw.rect(pe.colors.yellow, (60, 10, 30, 30), 0)
        else:
            pe.draw.rect(pe.colors.green, (60, 10, 30, 30), 0)
        if not show:
            ctext = lookup.get("EZtext").textbox.single(ctext, pe.colors.red, (0, 100, 200, 25))
            if lookup.get("key").enter():
                show = True
        else:
            pe.text.display(lookup.get("EZtext").size(ctext['text'], pe.colors.black, (0, 100, 200, 25)))
        framehost.exit(FID)
        admin = None
