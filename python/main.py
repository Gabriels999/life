import os
from time import sleep

from helpers import mount_board, read_board

def main():
    board = mount_board()
    try:
        while True:
            print(board)
            sleep(0.5)
            os.system('clear')
            board = read_board(board)
    except KeyboardInterrupt:
        print('\n\nJogo interrompido!')

main()