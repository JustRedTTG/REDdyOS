data, lookup, pe = None, None, None


def verify():
    return "module"


def init(dataV, lookupV):
    global data, lookup, pe
    data = dataV
    lookup = lookupV
    pe = lookup.get("PGE")
    return "EZimage"


lib = []


def place(core=-1, pos=(0, 0)):
    if core > -1:
        pe.display.blit(lib[core][2], pos)
    else:
        pe.display.blit(lib[len(lib) - 1][2], pos)


def get(core):
    return lib[core][2]


def image(file, size, pos=(0, 0), link="", display=True):
    if lookup.get("os").path.exists(file):
        imageClass = [file, size]
        i = 0
        exist = False
        while i < len(lib):
            if imageClass == [lib[i][0], lib[i][1]]:
                exist = True
                if display:
                    place(i, pos)
                else:
                    return i
            i += 1
        if not exist:
            Surface = pe.pygame.image.load(file).convert_alpha()
            Surface = pe.pygame.transform.scale(Surface, size)
            lib.append([file, size, Surface])
            if display:
                place(pos=pos)
            else:
                return len(lib) - 1
    elif link:
        lookup.get("downFile").download(link, file)
