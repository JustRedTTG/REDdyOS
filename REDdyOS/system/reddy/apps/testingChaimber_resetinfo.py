data, lookup, pe, commons, framehost, frame = None, None, None, None, None, None


def verify():
    return "app"


def init(dataV, lookupV):
    global data, lookup, commons, pe, framehost, frame
    data = dataV
    lookup = lookupV
    commons = {
        'icon': data.files + "reddy/icons/tch.png",
        'window_size': (500, 100),
        'window_type': 0,
        'window_pos': (data.display_rect.width // 2 - 250, data.display_rect.height // 2 - 50),
        'title': "Testing Chaimber!"
    }
    pe = lookup.get("PGE")
    framehost = lookup.get("FHost")
    frame = framehost.Frame("tchINFO", commons)
    return "tchINFO", 8, 2


calls = 0


def draw():
    global calls
    with frame:
        pe.fill.full(pe.colors.white)
        pe.text.Text("The System modules were restarted!", 'freesansbold.ttf', 25, pe.math.center((0, 0, 500, 100)),
                     (pe.colors.black, None)).display()

    calls += 1
    if calls >= 100:
        frame.close()
        data.operations.append("run reddy/apps/testingChaimber.py")
