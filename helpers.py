import random


def generate_random():
    value = random.randint(0,5)
    if value == 1:
        return "*"
    return " "


def mount_board():
    board = ""
    size = 4
    for _ in range(size):
        for _ in range(size):
            board+= generate_random()
        board+="\n"
    return board


def identify_neighbors():
    
    cardinal_point = {}
    return cardinal_point


def field_exist(row, *tup):
    if tup[0] < 0 or tup[1] < 0:
        return False
    if row[tup[0]][tup[1]] == "*":
        return True


def read_text(rows_list):
    rows_size = len(rows_list[0])

    for x in range(len(rows_list)):
        for y in range(rows_size):
            if rows_list[x][y] == '*':
                area_box = {}
                area_box["origin"] = rows_list[x][y],
                if field_exist(rows_list[x], x, y-1):
                    area_box["y-1"] = (x, y-1)
                if field_exist(x, y+1):
                    area_box["y+1"] = (x, y+1)

                # area_box = {
                #     "horizontal_neighbors_values": [rows_list[x][y-1], rows_list[x][y+1]],
                #     "vertical_neighbors_location": [(x-1, y), (x+1, y)],
                #     "vertical_neighbors_values": [rows_list[x-1][y], rows_list[x+1][y]],
                #     "diagonal_neighbors_location": [(x-1, y-1), (x+1, y+1)],
                #     "diagonal_neighbors_values": [rows_list[x-1][y-1], rows_list[x+1][y+1]],
                # }
                # print(area_box)


def check_horizontally(rows_set):
    around_box = ""
    x = 0
    while x < len(rows_set):
        y = 0
        while y < len(rows_set[x]):
            actual = rows_set[x][y]
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



ex="""*  * 
  ***
 **  
*****"""

read_board(ex)