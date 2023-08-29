import pygameextra as pe

m: dict
apps: dict = {}
screen = 0
theme = 0
events = None
files = ""
display_rect: pe.pygame.Rect
centerTSX: pe.TSX = None
operations = []
focus = ""
current_user = ""
red = (255, 50, 50)
red2 = (255, 100, 100)
red3 = (255, 150, 150)
red4 = (255, 200, 200)
fps = 150
resetDis = None


def userDir():
    return files + "data/Users/" + current_user + "/"


class common():
    window_pos = (50, 50)


killNoApps = False
version = "1.1"
