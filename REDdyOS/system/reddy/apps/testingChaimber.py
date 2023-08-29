data, lookup, os, pe, commons, framehost, frame, admin = None, None, None, None, None, None, None, None


def verify():
    return "app"


def init(dataV, lookupV):
    global data, lookup, os, commons, pe, framehost, frame
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
    frame = framehost.Frame("tch", commons)
    return "tch", 8, 2


def reboot():
    global admin
    data.operations.append("screen 0")
    for module_name in list(data.m.keys()):
        if admin != None:
            admin.stop(module_name)
        else:
            data.operations.append(f"stop {module_name}")
        data.operations.append(f"begin {module_name}")
    for appname in list(data.apps.keys()):
        if admin != None:
            admin.close(appname)
        else:
            data.operations.append(f"close {appname}")
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
    if not enable: return
    with frame:
        global ctext, show, admin
        pe.fill.full(pe.colors.white)
        mouse = lookup.get("mouse")

        mouse_position = mouse.pos()
        mouse_window_position = mouse.Wpos()


        pe.draw.line(pe.colors.red, (0, mouse_position[1]), (frame.window_size[0], mouse_position[1]), 5, 0)
        pe.draw.line(pe.colors.red, (mouse_position[0], 0), (mouse_position[0], frame.window_size[1]), 5, 0)

        pe.draw.line(pe.colors.green, (0, mouse_window_position[1]), (frame.window_size[0], mouse_window_position[1]), 5, 0)
        pe.draw.line(pe.colors.green, (mouse_window_position[0], 0), (mouse_window_position[0], frame.window_size[1]), 5, 0)

        pe.button.rect((0, 0, 50, 50), pe.colors.red, pe.colors.aqua, action=reboot)
        pe.button.rect((100, 0, 50, 50), pe.colors.red, pe.colors.aqua, action=kill)
        if not lookup.get("adminmng").check("tch"):
            if not "tch" in lookup.get("adminmng").decline:
                pe.button.rect((50, 0, 50, 50), pe.colors.red, pe.colors.aqua, action=getadmin)
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
            lookup.get("EZtext").size(ctext['text'], pe.colors.black, (0, 100, 200, 25)).display()
        admin = None
