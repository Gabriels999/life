import random


def generate_random():
    value = random.randint(0,1)
    if value == 1:
        return "*"
    return "."


def mount_board():
    board = ""
    size = 4
    for _ in range(size):
        for _ in range(size):
            board+= generate_random()
        board+="\n"
    return board


def is_neighbors(a, b, pos):
    res = []
    if a == '*':
        res.append(pos[0])

    if b == '*':
        res.append(pos[1])

    return res

def is_neighbor(a, pos):
    if a == '*':
        return pos
    return

def set_limits(row, x, y, size, op_type):
    h1, h2 = y-1, y+1
    v1, v2 = x-1, x+1
    sup_esq, inf_esq, sup_dir, inf_dir = (v1, h1), (v2, h1), (v1, h2), (v2, h2)
    
    text = []
    if op_type == 'h':
        if y == 0:
            text.append(is_neighbor(row[h2], (x, h2)))
        elif y == size:
            text.append(is_neighbor(row[h1], (x, h1)))
        else:
            text.append(is_neighbors(row[h1], row[h2], [(x, h1),(x, h2)]))
        return text
    elif op_type == 'v':
        if y == 0:
            text.append(is_neighbor(row[v2], (x, h2)))
        elif y == size:
            text.append(is_neighbor(row[v1], (x, h1)))
        else:
            text.append(is_neighbors(row[v1], row[v2], [(v1, y),(v2, y)]))
    else:
        return
    if text == []:
        return
    return text



def read_text(rows_list):
    rows_size = len(rows_list[0])

    for x in range(len(rows_list)):
        for y in range(rows_size):
            if rows_list[x][y] == '*':
                area_box = {}
                area_box["origin"] = rows_list[x][y],

                horizontal_neighbors = set_limits(rows_list[x], x, y, rows_size, 'h')
                if horizontal_neighbors:
                    area_box["horizontal_neighbors"] = horizontal_neighbors,

                vertical_neighbors = set_limits(rows_list[x], x, y, rows_size, 'v')
                if vertical_neighbors:
                    area_box["vertical_neighbors"] = vertical_neighbors,

                diagonal_neighbors = set_limits(rows_list[x], x, y, rows_size, 'd')
                area_box["diagonal_neighbors"] = diagonal_neighbors,
                print(area_box)


def check_horizontally(rows_set):
    around_box = ""
    x = 0
    while x < len(rows_set):
        y = 0
        while y < len(rows_set[x]):
            # Caso de primeira linha horizontal
            if x-1 < 0:
                print(rows_set[x][y])
            elif (x+1) > len(rows_set):
                h = x-1
                print(rows_set[x][y])
            else:
                h = x-1
                print(rows_set[h][y])
            y+=1
        x+=1


def read_board(text):
    rows = text.splitlines()
    read_text(rows)
