data, lookup, os = None, None, None


def verify():
    return "module"


def init(dataV, lookupV):
    global data, lookup, os
    data = dataV
    lookup = lookupV
    os = lookup.get("os")
    return "tokenmng"


current_user = "Unknown"
token = None


def load():
    global token
    f = open(data.files + "data/last token.token")
    f.seek(0)
    token = f.read().splitlines()
    f.close()
    global current_user
    for x in token:
        x = x.split(" ")
        if x[0] == "user":
            current_user = x[1]
