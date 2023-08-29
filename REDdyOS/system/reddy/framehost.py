data, lookup, pe = None, None, None


def verify():
    return "module"


def init(dataV, lookupV):
    global data, lookup, pe
    data = dataV
    lookup = lookupV
    pe = lookup.get("PGE")
    return "FHost"


apps = {}





def setup(name, commons):
    ezd = lookup.get("EZdrag")
    adminmng = lookup.get("adminmng")
    position = commons['window_pos']
    size = commons['window_size']
    ID = adminmng.generate_id(name)
    apps[ID] = {
        'name': name,  # 0
        'commons': commons,  # 1
        'drag_position': None,  # 2
        'surface': None,  # 3
        'central_sizer': ezd.central.sizer((position[0] + size[0] - 1, position[1] + size[1] + 20 - 1),
                                           [(position[0] + 150, position[1] + 150), None], pe.colors.gray),  # 4
        'bottom_right_corner': (position[0] + size[0] - 1, position[1] + size[1] + 20 - 1),  # 5
        'horizontal_pager': ezd.horizontal.pager(
            (position[0] + size[0] - 11, position[1] + size[1] / 2 + 20, 10, size[1]),
            pe.colors.gray, pe.colors.black),  # 6
        'vertical_pager': ezd.vertical.pager((position[0] + size[0] / 2, position[1] + size[1] + 20 - 1, size[0], 10),
                                             pe.colors.gray, pe.colors.black)  # 7
    }
    return ID


drag = False
lastM = False


def close(name: str):
    data.operations.append(f"close {name} *Frame-Host*")
    [apps.pop(ID) for ID, app in apps.items() if app['name'] == name]


rem = None
appsRAN = []
appsThis = []


def screen(ID):
    global rem, appsRAN, appsThis
    try:
        rem = pe.display.display_reference
        data.resetDis = rem
        pe.display.context(apps[ID]['surface'])
        appsThis.append(ID)
        if ID not in appsRAN:
            appsRAN.append(ID)
    except:
        rem = pe.display.display_reference


def exit(ID):
    global rem
    try:
        apps[ID]['surface'] = pe.display.display_reference
    except KeyError:
        raise LookupError(f"framehost couldn't find `{ID}`")
    try:
        pe.display.context(rem)
    except:
        raise AttributeError("framehost couldn't change the display back")
    pos = apps[ID]['commons']['window_pos']
    pe.display.blit(apps[ID]['surface'], (pos[0], pos[1] + 20))
    lookup.get("mouse").remove_offset()
    if not drag:
        ezd = lookup.get("EZdrag")
        if apps[ID]['commons']['window_type'] == 1:
            ezd.central.draw_sizer(apps[ID]['central_sizer'])
            # ezd.horizontal.draw_pager(apps[ID][6])
            # ezd.vertical.draw_pager(apps[ID][7])


def draw_frame(app, ID):
    global drag, lastM
    if True:
        mouse = lookup.get("mouse")
        mouse.remove_offset()
        if data.focus == app['name']:  # rect fill
            pe.draw.rect(data.red3, (app['commons']['window_pos'][0], app['commons']['window_pos'][1], app['commons']['window_size'][0], 20), 0)
        else:
            pe.draw.rect(data.red4, (app['commons']['window_pos'][0], app['commons']['window_pos'][1], app['commons']['window_size'][0], 20), 0)

        # X button
        if drag or lastM:
            pe.draw.rect(pe.colors.red,
                         (app['commons']['window_pos'][0] + app['commons']['window_size'][0] - 35, app['commons']['window_pos'][1], 35, 20), 0)
        else:
            pe.button.rect((app['commons']['window_pos'][0] + app['commons']['window_size'][0] - 35, app['commons']['window_pos'][1], 35, 20),
                           pe.colors.red, pe.colors.pink, action=close, data=ID)
        mouse.add_offset()
        apps[ID]['surface'] = pe.Surface(app['commons']['window_size'])
        buldge = 2
        pe.draw.rect(pe.colors.black,
                     (*app['commons']['window_pos'], app['commons']['window_size'][0], app['commons']['window_size'][1] + 20),
                     buldge)
        pe.draw.line(pe.colors.black, (app['commons']['window_pos'][0], app['commons']['window_pos'][1] + 20),
                     (app['commons']['window_pos'][0] + app['commons']['window_size'][0], app['commons']['window_pos'][1] + 20), buldge)


def draw(ID):
    # print("framehost draw",ID)
    global drag, lastM
    try:
        app = apps[ID]
    except KeyError:
        raise LookupError(f"framehost couldn't find `{ID}`")
    mouse = lookup.get("mouse")
    try:
        off = app['commons']['window_pos']
        off = (off[0], off[1] + 20)
    except:
        off = (0, 0)
    if not drag and app['commons']['window_type'] == 1:
        lookup.get("mouse").remove_offset()
        ezd = lookup.get("EZdrag")
        s1 = ezd.central.drag_sizer(app['central_sizer'])
        # s2 = (ezd.horizontal.pager(app[6]),ezd.vertical.pager(app[7]))
        x = s1[0]
        y = s1[1]
        s = (x, y)
        p = app['commons']['window_pos']
        app['central_sizer'].x = x
        app['central_sizer'].y = y
        app['horizontal_pager'].x = x
        app['horizontal_pager'].y = y / 2
        app['vertical_pager'].x = x / 2
        app['vertical_pager'].y = y

        app['commons']['window_size'] = (s[0] - p[0], s[1] - 20 - p[1])
    mouse.set_offset((off[0] * -1, off[1] * -1))
    if True:
        rect = (app['commons']['window_pos'][0], app['commons']['window_pos'][1], app['commons']['window_size'][0] - 35, 20)
        if not drag:
            pos = mouse.pos()
            pos = list(pos)
            x = 0
            y = 0
            while pos[0] > app['commons']['window_pos'][0]:
                pos[0] -= 1
                x += 1
            while pos[1] > app['commons']['window_pos'][1]:
                pos[1] -= 1
                y += 1
            pos = tuple(pos)
            if mouse.x() > rect[0] and mouse.x() < rect[0] + rect[2] and mouse.y() > rect[1] and mouse.y() < rect[1] + \
                    rect[3] and mouse.left() and not lastM:
                app['drag_position'] = (x, y)
                data.operations.append(f"focus {app['name']} *Frame-Host*")
                drag = True
        if not drag and app['drag_position'] != None:
            app['drag_position'] = None
        if drag and app['drag_position'] != None:
            x = app['drag_position'][0]
            y = app['drag_position'][1]
            app['commons']['window_pos'] = (mouse.x() - x, mouse.y() - y)
            p = app['commons']['window_pos']
            s = app['commons']['window_size']
            app['central_sizer'].x = p[0] + s[0] - 1
            app['central_sizer'].y = p[1] + s[1] + 20 - 1
            app['central_sizer'].block = [(p[0] + 150, p[1] + 150), None]
        if drag and not mouse.left():
            drag = False
    try:
        title = app['commons']['title']
    except KeyError:
        title = app['name']
    draw_frame(app, ID)
    lookup.get("EZtext").cram(title, pe.colors.black, (
        app['commons']['window_pos'][0], app['commons']['window_pos'][1], app['commons']['window_size'][0] - 35, 20)).display()


def clickOut():
    global lastM
    for app in apps:
        rect = (app['commons']['window_pos'][0], app['commons']['window_pos'][1] - 20, app['commons']['window_size'][0] + 2, app['commons']['window_size'][1] + 22)
        mouse = lookup.get("mouse")
        if mouse.y() < data.display_rect.height - 35 and data.focus != "home":
            if mouse.x() > rect[0] and mouse.x() < rect[0] + rect[2] and mouse.y() > rect[1] and mouse.y() < rect[1] + \
                    rect[3]:

                if data.focus != app[0] and not lastM:
                    data.operations.append("focus " + app[0])

                return False
            else:
                return True
        else:
            return False


def remove():
    pass


def beforeendcall():
    global lastM, appsThis, appsRAN
    lastM = lookup.get("mouse").left()
    # for app in appsRAN:
    #  if not app in appsThis:
    #    draw(app)
    #    pos = apps[app][1].window_pos
    #    pe.display.blit.rect(apps[app][3], (pos[0], pos[1] + 20))
    appsThis = []
