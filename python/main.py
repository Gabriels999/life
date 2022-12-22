from helpers import mount_board, read_board

def main():
    board = mount_board()
    print(board)
    read_board(board)

main()