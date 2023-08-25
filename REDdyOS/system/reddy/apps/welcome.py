# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.9

(data, lookup) = (None, None)
commons = None
pe = None
(framehost, FID) = (None, None)
time = None
admin = None


class color:
    background = (200, 150, 150)
    weback = (255, 255, 255, 200)


text = None


def verify():
    return 'app'


def newCommon():
    class commonsV:
        __qualname__ = 'newCommon.<locals>.commonsV'
        icon = data.files + 'reddy/icons/home.png'
        window_size = (700, 525)
        window_type = 0
        window_pos = (
        data.display_rect.width - int(window_size[0] / 2), data.display_rect.height - int(window_size[1] / 2))
        title = '~Welcome~'
        name = 'Welcome!'

    return commonsV


def init(dataV, lookupV, allow=(True,)):
    global data, lookup, commons, pe, time, framehost, FID, text
    data = dataV
    lookup = lookupV
    commons = newCommon()
    if allow:
        pe = lookup.get('PGE')
        time = lookup.get('time')
        framehost = lookup.get('FHost')
        FID = framehost.setup('welcome', commons)
        data.killNoApps = True
        ezt = lookup.get('EZtext')

        # textV = ezt('textV')
        # text = textV
    return 'welcome', 10, 1


def admincall(am):
    global admin
    admin = am


cycle = 0
cycleROT = 0
cycleSTOP = [
    False,
    0]
cycleWAY = True
screen = 0


def getTSXcube(TSX, ROT):
    ROT += 45
    points = []
    for x in range(4):
        points.append(pe.math.tsx.get(TSX, ROT))
        ROT += 90
    return points


def cycler():
    global cycleROT, cycleWAY, cycleROT, cycleWAY, cycle, cycle
    max = 20
    perstop = 4
    speed = 10
    if not cycleSTOP[0]:
        if cycle >= perstop and cycleROT <= 0:
            cycleSTOP[0] = True
            cycleSTOP[1] = time.time()
        elif cycleWAY:
            cycleROT -= speed
            if cycleROT <= -max:
                cycleWAY = False

        cycleROT += speed
        if cycleROT >= max:
            cycleWAY = True
            cycle += 1
        elif time.time() - cycleSTOP[1] > 1:
            cycleSTOP[0] = False
            cycle = 0


def makeBox(rect):
    pe.draw.rect(pe.color.lightgray, rect, 0)
    pe.draw.line(pe.color.gray, (rect[0], rect[1]), (rect[0], rect[1] + rect[3]), 2)
    pe.draw.line(pe.color.gray, (rect[0], rect[1]), (rect[0] + rect[2], rect[1]), 2)
    pe.draw.line(pe.color.white, (rect[0] + rect[2], rect[1] + rect[3]), (rect[0] + rect[2], rect[1]), 2)
    pe.draw.line(pe.color.white, (rect[0] + rect[2], rect[1] + rect[3]), (rect[0], rect[1] + rect[3]), 2)


def draw():
    pe.fill.full(color.background)
    framehost.draw(FID)
    framehost.screen(FID)
    pe.fill.full(color.background)
    framehost.exit(FID)
    # cycleTSX = pe.math.tsx.make((commons.window_pos[0] + 75, commons.window_pos[1] + 100), 35)
