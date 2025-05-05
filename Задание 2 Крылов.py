import os

def clear_screen():
    # очищает экран
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("    0   1   2")
    for i, row in enumerate(board):
        row_display = " | ".join(row)
        print(f"{i}   {row_display}")
        if i < 2:
            print("   ---+---+---")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_input(player, board):
    while True:
        try:
            print(f"\nХод игрока {player}")
            row = int(input("введите номер строки (0-2): "))
            col = int(input("введите номер столбца (0-2): "))
            if row not in range(3) or col not in range(3):
                print("ошибка: допустимые значения — от 0 до 2.")
                continue
            if board[row][col] != " ":
                print("ошибка: клетка уже занята.")
                continue
            return row, col
        except ValueError:
            print("ошибка: введите целое число.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        clear_screen()
        print("добро пожаловать в крестики нолики")
        print_board(board)

        row, col = get_input(current_player, board)
        board[row][col] = current_player

        if check_win(board):
            clear_screen()
            print_board(board)
            print(f"\n игрок {current_player} победил")
            break
        if check_draw(board):
            clear_screen()
            print_board(board)
            print("\nНичья!")
            break

        current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__":
    main()
