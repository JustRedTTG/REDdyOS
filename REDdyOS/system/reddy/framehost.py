data, lookup, pe = None, None, None


def verify():
    return "module"


def init(dataV, lookupV):
    global data, lookup, pe
    data = dataV
    lookup = lookupV
    pe = lookup.get("PGE")
    return "FHost"


drag = False
lastM = False
LINE_WIDTH = 2
TOP_HEIGHT = 20
TOTAL_HEIGHT = LINE_WIDTH + TOP_HEIGHT


def close(name: str):
    data.operations.append(f"close {name} *Frame-Host*")
    [apps.pop(ID) for ID, app in apps.items() if self.name == name]


rem = None


def clickOut():
    global lastM
    for app in apps:
        rect = (
            self.commons['window_pos'][0], self.commons['window_pos'][1] - TOP_HEIGHT, self.commons['window_size'][0] + 2,
            self.commons['window_size'][1] + TOTAL_HEIGHT)
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
    #    pe.display.blit.rect(apps[app][3], (pos[0], pos[1] + TOP_HEIGHT))
    appsThis = []


class Frame:
    def __init__(self, name, commons):
        ezd = lookup.get("EZdrag")
        adminmng = lookup.get("adminmng")
        position = commons['window_pos']
        size = commons['window_size']
        self.name = name  # 0
        self.commons = commons  # 1
        self.drag_position = None  # 2
        self.surface = None  # 3
        self.central_sizer = ezd.central.sizer(
            (position[0] + size[0] - 1, position[1] + size[1] + TOP_HEIGHT - 1),
            [(position[0] + 150, position[1] + 150), None], pe.colors.gray)  # 4
        self.bottom_right_corner = (position[0] + size[0] - 1, position[1] + size[1] + TOP_HEIGHT - 1)  # 5
        self.horizontal_pager = ezd.horizontal.pager(
            (position[0] + size[0] - 11, position[1] + size[1] / 2 + TOP_HEIGHT, 10, size[1]),
            pe.colors.gray, pe.colors.black)  # 6
        self.vertical_pager = ezd.vertical.pager(
            (position[0] + size[0] / 2, position[1] + size[1] + TOP_HEIGHT - 1, size[0], 10),
            pe.colors.gray, pe.colors.black)  # 7

    def __getattr__(self, item):
        try:
            return self.commons[item]
        except KeyError:
            raise AttributeError(f"frame commons doesn't have such item")

    def screen(self):
        global rem
        try:
            rem = pe.display.display_reference
            data.resetDis = rem
            pe.display.context(self.surface)
        except:
            rem = pe.display.display_reference

    def exit(self):
        global rem
        try:
            self.surface = pe.display.display_reference
        except KeyError:
            raise LookupError(f"framehost couldn't find `{ID}`")
        try:
            pe.display.context(rem)
        except:
            raise AttributeError("framehost couldn't change the display back")
        pos = self.commons['window_pos']
        pe.display.blit(self.surface, (pos[0], pos[1] + TOP_HEIGHT + LINE_WIDTH))
        lookup.get("mouse").remove_offset()
        if not drag:
            ezd = lookup.get("EZdrag")
            if self.commons['window_type'] == 1:
                ezd.central.draw_sizer(self.central_sizer)
                # ezd.horizontal.draw_pager(apps[ID][6])
                # ezd.vertical.draw_pager(apps[ID][7])

    def draw_frame(self):
        global drag, lastM
        mouse = lookup.get("mouse")
        mouse.remove_offset()
        if data.focus == self.name:  # rect fill
            pe.draw.rect(data.red3, (
                self.commons['window_pos'][0], self.commons['window_pos'][1], self.commons['window_size'][0],
                TOP_HEIGHT),
                         0)
        else:
            pe.draw.rect(data.red4, (
                self.commons['window_pos'][0], self.commons['window_pos'][1], self.commons['window_size'][0],
                TOP_HEIGHT),
                         0)

        # X button
        if drag or lastM:
            pe.draw.rect(pe.colors.red,
                         (self.commons['window_pos'][0] + self.commons['window_size'][0] - 35,
                          self.commons['window_pos'][1], 35, TOP_HEIGHT), 0)
        else:
            pe.button.rect((self.commons['window_pos'][0] + self.commons['window_size'][0] - 35,
                            self.commons['window_pos'][1], 35, TOP_HEIGHT),
                           pe.colors.red, pe.colors.pink, action=close, data=self.name)
        mouse.add_offset()
        self.surface = pe.Surface(self.commons['window_size'])
        pe.draw.line(pe.colors.black, (self.commons['window_pos'][0], self.commons['window_pos'][1] + TOP_HEIGHT),
                     (self.commons['window_pos'][0] + self.commons['window_size'][0] - LINE_WIDTH,
                      self.commons['window_pos'][1] + TOP_HEIGHT), LINE_WIDTH)

    def draw_frame_outline(self):
        pe.draw.rect(pe.colors.black,
                     (*self.commons['window_pos'], self.commons['window_size'][0],
                      self.commons['window_size'][1] + TOTAL_HEIGHT),
                     LINE_WIDTH // 2)

    def draw(self):
        # print("framehost draw",ID)
        global drag, lastM
        mouse = lookup.get("mouse")
        try:
            off = self.commons['window_pos']
            off = (off[0], off[1] + TOP_HEIGHT)
        except KeyError:
            off = (0, 0)
        if not drag and self.commons['window_type'] == 1:
            lookup.get("mouse").remove_offset()
            ezd = lookup.get("EZdrag")
            s1 = ezd.central.drag_sizer(self.central_sizer)
            # s2 = (ezd.horizontal.pager(app[6]),ezd.vertical.pager(app[7]))
            x = s1[0]
            y = s1[1]
            s = (x, y)
            p = self.commons['window_pos']
            self.central_sizer.x = x
            self.central_sizer.y = y
            self.horizontal_pager.x = x
            self.horizontal_pager.y = y / 2
            self.vertical_pager.x = x / 2
            self.vertical_pager.y = y

            self.commons['window_size'] = (s[0] - p[0], s[1] - TOP_HEIGHT - p[1])
        mouse.set_offset((off[0] * -1, off[1] * -1))
        if True:
            rect = pe.rect.Rect(
                self.commons['window_pos'][0], self.commons['window_pos'][1], self.commons['window_size'][0] - 35,
                TOP_HEIGHT)
            if not drag:
                pos = mouse.pos()
                pos = list(pos)
                x = 0
                y = 0
                while pos[0] > self.commons['window_pos'][0]:
                    pos[0] -= 1
                    x += 1
                while pos[1] > self.commons['window_pos'][1]:
                    pos[1] -= 1
                    y += 1
                pos = tuple(pos)
                if rect.collidepoint(mouse.pos()) and mouse.left() and not lastM:
                    self.drag_position = (x, y)
                    data.operations.append(f"focus {self.name} *Frame-Host*")
                    drag = True
            if not drag and self.drag_position is not None:
                self.drag_position = None
            if drag and self.drag_position is not None:
                x = self.drag_position[0]
                y = self.drag_position[1]
                self.commons['window_pos'] = (mouse.x() - x, mouse.y() - y)
                p = self.commons['window_pos']
                s = self.commons['window_size']
                self.central_sizer.x = p[0] + s[0] - 1
                self.central_sizer.y = p[1] + s[1] + TOP_HEIGHT - 1
                self.central_sizer.block = [(p[0] + 150, p[1] + 150), None]
            if drag and not mouse.left():
                drag = False
        try:
            title = self.commons['title']
        except KeyError:
            title = self.name
        self.draw_frame()
        lookup.get("EZtext").cram(title, pe.colors.black, (
            self.commons['window_pos'][0], self.commons['window_pos'][1], self.commons['window_size'][0] - 35,
            TOP_HEIGHT)).display()

    def __enter__(self):
        self.draw()
        self.screen()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit()
        self.draw_frame_outline()