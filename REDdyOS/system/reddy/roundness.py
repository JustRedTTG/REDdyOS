import functools

data, lookup, pe = None, None, None


def verify():
    return "module"


def init(dataV, lookupV):
    global data, lookup, pe
    data = dataV
    lookup = lookupV
    pe = lookup.get("PGE")
    return "EZround"


def generate_roundness_offsets(I, x, y, radius):
    tsx = pe.TSX((radius * x, radius * y), radius)
    steps = (I[1] - I[0]) // 10
    return tuple([tsx[rotation] for rotation in range(I[0], I[1] + 1, steps)])


@functools.lru_cache
def get_roundness_map(radius):
    return [generate_roundness_offsets(rotation_pair, *xy, radius) for rotation_pair, xy in
            zip(((180, 270), (270, 360), (0, 90), (90, 180)), ((1, 1), (-1, 1), (-1, -1), (1, -1)))]


@functools.lru_cache
def round_rect(rect, radius, top_left=True, top_right=True, bottom_left=True, bottom_right=True):
    points = (
        (rect[0], rect[1]),
        (rect[0] + rect[2], rect[1]),
        (rect[0] + rect[2], rect[1] + rect[3]),
        (rect[0], rect[1] + rect[3]),
    )
    map_enabled_boolean = (
        top_left, top_right, bottom_right, bottom_left
    )
    output = []

    for point, mapping, should_map in zip(points, get_roundness_map(radius), map_enabled_boolean):
        if not should_map:
            output.append(point)
            continue
        for offset in mapping:
            output.append((point[0] + offset[0], point[1] + offset[1]))
    return tuple(output)
