from matplotlib.pyplot import box

def flipY(coords):
    if len(coords) == 9:
        y1 = abs(coords[5] - 1)
        y2 = abs(coords[6] - 1)
        y3 = abs(coords[7] - 1)
        y4 = abs(coords[8] - 1)
        return (coords[0], coords[1], coords[2], coords[3], coords[4],
                y1, y2, y3, y4)

    y1 = abs(coords[2] - 1)
    return (coords[0], coords[1], y1, coords[3], coords[4])


def convert_to_4(coords):
    x = coords[1]
    y = coords[5]
    sz_x = abs(coords[1] - coords[2])
    sz_y = abs(coords[5] - coords[7])
    return (coords[0], x, y, sz_x, sz_y)


def convert_to_8(coords):
    x = coords[1]
    y = coords[2]
    sz_x = coords[3]
    sz_y = coords[4]
    return (coords[0],  # number
            x, x + sz_x, x, x + sz_x,  # x
            y, y, y + sz_y, y + sz_y)  # y
