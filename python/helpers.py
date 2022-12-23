import random


def generate_random():
    value = random.randint(0,1)
    if value == 1:
        return "*"
    return "."


def mount_board():
    board = ""
    size = 50
    for _ in range(size):
        for _ in range(size):
            board+= generate_random()
        board+="\n"
    return board


def is_neighbor(list):
    res = 0
    for i in list:
        if i == '*':
            res += 1
    return res


def get_neighbors(x, y, rows):
    size = len(rows)
    home = (x, y)
    actual_row = rows[x]
    neighbors_count = 0
    
    # Possible coordenates
    back, front = y-1, y+1
    up, down = x-1, x+1

    #Check horizontally
    if y == 0:
        neighbors_count+= is_neighbor([actual_row[front]])
    elif y == size-1:
        neighbors_count+= is_neighbor([actual_row[back]])
    else:
        neighbors_count+= is_neighbor([actual_row[back], actual_row[front]])

    #Check vertically
    if x == 0:
        neighbors_count+= is_neighbor([rows[down][y]])
    elif x == size-1:
        neighbors_count+= is_neighbor([rows[up][y]])
    else:
        neighbors_count+= is_neighbor([rows[up][y], rows[down][y]])

    #Check diagonals
    if x == 0 and y == 0:
        neighbors_count+= is_neighbor([rows[down][front]])
    elif x == size-1 and y == 0:
        neighbors_count+= is_neighbor([rows[up][front]])
    elif x == 0 and y == size-1:
        neighbors_count+= is_neighbor([rows[down][back]])
    elif x == size-1 and y == size-1:
        neighbors_count+= is_neighbor([rows[up][back]])
    elif x == 0:
        neighbors_count+= is_neighbor([rows[down][back], rows[down][front]])
    elif x == size-1:
        neighbors_count+= is_neighbor([rows[up][back], rows[up][front]])
    elif y == 0:
        neighbors_count+= is_neighbor([rows[up][front], rows[down][front]])
    elif y == size-1:
        neighbors_count+= is_neighbor([rows[up][back], rows[down][back]])
    else:
        neighbors_count+= is_neighbor([rows[up][back], rows[down][back], rows[up][front], rows[down][front]])

    return neighbors_count


def update_matrix(actual_item, item_neighbors):
    new_item = ""
    if item_neighbors < 2 or item_neighbors > 3:
        new_item = "."
    elif item_neighbors == 3 and actual_item == ".":
        new_item = "*"
    else:
        new_item = actual_item
    return new_item


def read_text(rows_list):
    rows_size = len(rows_list[0])
    new_matrix =""
    for x in range(len(rows_list)):
        for y in range(rows_size):
            origin = rows_list[x][y]
            origin_pos = (x, y)
            neighbors = 0
            neighbors += get_neighbors(x, y, rows_list)
            new_matrix+= update_matrix(rows_list[x][y], neighbors)
        new_matrix+="\n"
    return new_matrix


def read_board(text):
    rows = text.splitlines()
    return read_text(rows)
