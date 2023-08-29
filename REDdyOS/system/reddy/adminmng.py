data, lookup, pe, usrmng, f, key = None, None, None, None, None, None


def verify():
    return "module"


def init(dataV, lookupV, fV="NOKEY123", keyV=0):
    global data, lookup, pe, usrmng, f, key
    data = dataV
    lookup = lookupV
    f = fV
    key = keyV
    pe = lookup.get("PGE")
    usrmng = lookup.get("usrmng")
    return "adminmng"


admin = None
decline = []


def check(appname):
    try:
        return data.apps[appname]['admin'] is not None
    except KeyError:
        return False


lastS = 2


def getadmin(appname):
    global admin, decline, lastS
    if not appname in decline:
        lastS = data.screen
        data.operations.append("screen 3")
        admin = appname


def declineapp(appname):
    global decline, admin
    if admin != None and appname != "":
        decline.append(appname)
        data.operations.append("screen " + str(lastS))
        admin = None
    elif appname == "":
        data.operations.append("screen " + str(lastS))
        admin = None


def generate_id(name):
    random = lookup.get("random")
    return name.join(chr(random.randint(97, 122)) for _ in range(10))


def generate_number(name):
    ID = generate_id(name)
    return sum(ord(letter) for letter in ID)


def acceptapp(key):
    global admin, f
    if admin is None: return

    data.operations.append("screen " + str(lastS))
    data.apps[admin]['admin_key'] = generate_number(admin)
    data.apps[admin]['admin'] = [f, (key * (data.apps[admin]['admin_key'] + 1)) / lookup.get("math").pi]

    admin = None


def call():
    global admin, f, key
    if data.screen == 3:
        if admin != None:
            lookup.get("mouse").remove_offset()
            lookup.get("DrawATheme").draw()
            ezr = lookup.get("EZround")
            pe.fill.transparency((0, 0, 0), 200)
            popup_rect = (data.display_rect.width / 2 - 225, data.display_rect.height / 2 - 125, 450, 250)
            pe.draw.polygon((255, 255, 255, 200), ezr.round_rect(popup_rect, 10), 0)
            try:
                icon = lookup.getapp(admin).commons['icon']
            except KeyError:
                icon = data.files + "reddy/icons/admin.png"
            lookup.get("EZimage").image(icon, (150, 150),
                                        (data.display_rect.width / 2 - 225, data.display_rect.height / 2 - 125))
            ezt = lookup.get("EZtext")
            try:
                title = lookup.getapp(admin).commons['title']
            except KeyError:
                title = admin
            ezt.cram(title, pe.colors.black,
                     (data.display_rect.width / 2 - 75, data.display_rect.height / 2 - 100, 300, 25)).display()
            ezt.fit("Wants admin privileges", pe.colors.black,
                    (data.display_rect.width / 2 - 75, data.display_rect.height / 2 - 75, 300, 25)).display()
            pe.button.rect((data.display_rect.width / 2 - 225, data.display_rect.height / 2 + 90, 225, 35),
                           pe.colors.red, (255, 50, 50), action=declineapp, data=admin)
            pe.button.rect((data.display_rect.width / 2 + 225 - 35, data.display_rect.height / 2 - 125, 35, 35),
                           pe.colors.red, (255, 50, 50), action=declineapp, data="")
            pe.button.rect((data.display_rect.width / 2, data.display_rect.height / 2 + 90, 225, 35), pe.colors.green,
                           (50, 255, 50), action=acceptapp, data=key / lookup.get("math").pi)
        else:
            data.operations.append("screen " + str(lastS))
    else:
        admin = None


def admincall(admin):
    class SecuredAdminMangerClassREDdyOS:
        @staticmethod
        def call(): call()

        @staticmethod
        def check(appname): return check(appname)

        @staticmethod
        def getadmin(appname): getadmin(appname)

        @staticmethod
        def generate_id(name): return generate_id(name)

        @staticmethod
        def generate_number(name): return generate_number(name)

        @property
        def decline(self): return decline

        @property
        def admin(self): return admin

        @admin.setter
        def admin(self, value):
            global admin
            admin = value

    admin.change_module('adminmng', SecuredAdminMangerClassREDdyOS())
