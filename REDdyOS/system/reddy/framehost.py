data, lookup, pe, mouse, ezd, ezt, ezr = None, None, None, None, None, None, None


def verify():
    return "module"


def init(dataV, lookupV):
    global data, lookup, pe, mouse, ezd, ezt, ezr
    data = dataV
    lookup = lookupV
    pe = lookup.get("PGE")
    mouse = lookup.get("mouse")
    ezd = lookup.get("EZdrag")
    ezt = lookup.get("EZtext")
    ezr = lookup.get("EZround")
    return "FHost"


drag = False
lastM = False
LINE_WIDTH = 2
TOP_HEIGHT = 25
TOTAL_HEIGHT = LINE_WIDTH + TOP_HEIGHT
BORDER_RADIUS = 10

rem = None


# def clickOut():
#     global lastM
#     for app in apps:
#         rect = (
#             self.commons['window_pos'][0], self.commons['window_pos'][1] - TOP_HEIGHT, self.commons['window_size'][0] + 2,
#             self.commons['window_size'][1] + TOTAL_HEIGHT)
#         mouse = lookup.get("mouse")
#         if mouse.y() < data.display_rect.height - 35 and data.focus != "home":
#             if mouse.x() > rect[0] and mouse.x() < rect[0] + rect[2] and mouse.y() > rect[1] and mouse.y() < rect[1] + \
#                     rect[3]:
#
#                 if data.focus != app[0] and not lastM:
#                     data.operations.append("focus " + app[0])
#
#                 return False
#             else:
#                 return True
#         else:
#             return False


def remove():
    pass


def beforeendcall():
    global lastM, appsThis, appsRAN
    lastM = mouse.left()
    # for app in appsRAN:
    #  if not app in appsThis:
    #    draw(app)
    #    pos = apps[app][1].window_pos
    #    pe.display.blit(apps[app][3], (pos[0], pos[1] + TOP_HEIGHT))
    appsThis = []


class Frame:
    def __init__(self, name, commons):
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
        except AttributeError:
            return
        try:
            pe.display.context(rem)
        except:
            raise AttributeError("framehost couldn't change the display back")
        pos = self.commons['window_pos']
        # pe.display.blit(self.surface, (pos[0], pos[1] + TOP_HEIGHT + LINE_WIDTH))
        pe.pygame.gfxdraw.textured_polygon(
            pe.display.display_reference.surface,
            ezr.round_rect(
                (pos[0], pos[1] + TOTAL_HEIGHT, *self.commons['window_size']),
                BORDER_RADIUS, top_left=False, top_right=False
            ), self.surface.surface, pos[0], (pos[1] + TOTAL_HEIGHT) * -1)
        mouse.remove_offset()
        if not drag:
            if self.commons['window_type'] == 1:
                ezd.central.draw_sizer(self.central_sizer)
                # ezd.horizontal.draw_pager(apps[ID][6])
                # ezd.vertical.draw_pager(apps[ID][7])

    def draw_frame(self):
        global drag, lastM
        mouse.remove_offset()
        if data.focus == self.name:  # rect fill
            pe.draw.polygon(
                data.red3 if data.focus == self.name else data.red4,
                ezr.round_rect((self.commons['window_pos'][0],
                                self.commons['window_pos'][1],
                                self.commons['window_size'][0],
                                TOP_HEIGHT),
                               BORDER_RADIUS, bottom_left=False, bottom_right=False), 0)

        x_button_rect = (self.commons['window_pos'][0] + self.commons['window_size'][0] - TOP_HEIGHT,
                         self.commons['window_pos'][1], TOP_HEIGHT, TOP_HEIGHT)

        # X button
        if drag or lastM:
            pe.draw.rect(pe.colors.red, x_button_rect, 0)
        else:
            pe.button.rect(x_button_rect, pe.colors.red, pe.colors.pink, action=self.close)
        mouse.add_offset()
        self.surface = pe.Surface(self.commons['window_size'])
        pe.draw.line(pe.colors.black, (self.commons['window_pos'][0], self.commons['window_pos'][1] + TOP_HEIGHT),
                     (self.commons['window_pos'][0] + self.commons['window_size'][0] - LINE_WIDTH,
                      self.commons['window_pos'][1] + TOP_HEIGHT), LINE_WIDTH)

    def draw_frame_outline(self):
        rect = (*self.commons['window_pos'], self.commons['window_size'][0],
                self.commons['window_size'][1] + TOTAL_HEIGHT)
        pe.draw.polygon(pe.colors.black, ezr.round_rect(rect, BORDER_RADIUS), LINE_WIDTH // 2)

    def draw(self):
        # print("framehost draw",ID)
        global drag, lastM
        try:
            off = self.commons['window_pos']
            off = (off[0], off[1] + TOP_HEIGHT)
        except KeyError:
            off = (0, 0)
        if not drag and self.commons['window_type'] == 1:
            mouse.remove_offset()
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

            self.window_size = (s[0] - p[0], s[1] - TOP_HEIGHT - p[1])
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
                self.window_pos = (mouse.x() - x, mouse.y() - y)
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
        ezt.cram(title, pe.colors.black, (
            self.commons['window_pos'][0], self.commons['window_pos'][1], self.commons['window_size'][0] - TOP_HEIGHT,
            TOP_HEIGHT), padding=5).display()

    @property
    def window_pos(self):
        return self.commons['window_pos']

    @window_pos.setter
    def window_pos(self, value):
        self.commons['window_pos'] = value

    @property
    def window_size(self):
        return self.commons['window_size']

    @window_size.setter
    def window_size(self, value):
        self.commons['window_size'] = value

    def close(self):
        data.operations.append(f"close {self.name} *Frame-Host*")

    def __enter__(self):
        self.draw()
        self.screen()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit()
        self.draw_frame_outline()
