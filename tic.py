def play_turn(game_board: list, x: int, y: int, piece: str):
    if game_board[y][x] != "X" or game_board[y][x] != "O":
        game_board[y][x] = piece
        return True
    else:
        return False

game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(game_board, 2, 0, "X"))
print(game_board)