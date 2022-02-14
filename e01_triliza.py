import random

SMALL, MIDDLE, LARGE = 1, 2, 3


def is_valid_move(board, position, piece):
    if not (0 <= position <= 8):
        return False
    if not (1 <= piece <= 3):
        return False
    if piece in board[position]:
        return False
    if board[position] and piece < board[position][-1]:
        return False
    return True


victory_positions = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


def check_victory(board):
    board_values = [any(i) for i in board]
    for pos in victory_positions:
        if all([board_values[i] for i in pos]):
            return True, pos
    return False, None


def play(move_function):
    board = [
        [], [], [],
        [], [], [],
        [], [], []
    ]

    total_moves = 0
    total_valid_moves = 0
    win_pos = None
    win = False
    while not win:
        total_moves += 1
        position, piece = move_function()
        if is_valid_move(board, position, piece):
            total_valid_moves += 1
            board[position].append(piece)
            win, win_pos = check_victory(board)
        else:
            print(
                f"not valid movement(position/piece={position}-{piece}, board={board}). please try again")
    return total_moves, total_valid_moves, board, win_pos


def play_many_random_games(number_of_games):
    total_moves_list = []
    total_valid_list = []
    for _ in range(number_of_games):
        total_moves, total_valid, board, winpos = play(random_move)
        print(total_moves, board, winpos)
        total_moves_list.append(total_moves)
        total_valid_list.append(total_valid)
    average_moves = round(sum(total_moves_list) / len(total_moves_list), 1)
    average_valid = round(sum(total_valid_list) / len(total_valid_list), 1)
    return number_of_games, average_moves, average_valid


def report(games, average_moves, average_valid):
    report = f"\nProgram played {games} random games\n"
    report += f"Average moves       = {average_moves}\n"
    report += f"Average valid moves = {average_valid}\n"
    print(report)


def report_gr(games, average_moves, average_valid):
    report = f"\nΤο πρόγραμμα έπαιξε {games} τυχαία παιχνίδια\n"
    report += f"Μέσος όρος κινήσεων               = {average_moves}\n"
    report += f"Μέσος όρος επιτυχημένων κινήσεων  = {average_valid}\n"
    print(report)


def random_move():
    position = random.randrange(8)
    piece = random.randrange(1, 4)
    return position, piece


def player_move():
    res = tuple(input("Enter position/piece: "))
    position, piece = res
    return int(position), int(piece)


if __name__ == '__main__':
    report_gr(*play_many_random_games(100))
    # print(play(player_move))
