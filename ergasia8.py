import random
from collections import Counter

WTOWER = '1.Πύργος Λευκός'
BBISHOP = '2.Αξιωματικός Μαύρος'
DRAW = '3.Ισοπαλία'


def generate_random_position(board_size):
    x_position = random.randrange(board_size[0])
    y_position = random.randrange(board_size[1])
    return (x_position, y_position)


def check_winner(wtower_pos, bbishop_pos, board_size):
    # Έλεγχος για νίκη Πύργου
    if wtower_pos[0] == bbishop_pos[0] or wtower_pos[1] == bbishop_pos[1]:
        return WTOWER
    # Έλεγχος για τον Μαύρο αξιωματικό
    bisop_control_positions = []
    xbishop, ybishop = bbishop_pos

    for i in range(1, max(board_size)):
        ax, ay = xbishop+i, ybishop - i
        bx, by = xbishop-i, ybishop - i
        cx, cy = xbishop+i, ybishop + i
        dx, dy = xbishop-i, ybishop + i
        if ax >= 0 and ay >= 0:
            bisop_control_positions.append((ax, ay))
        if bx >= 0 and by >= 0:
            bisop_control_positions.append((bx, by))
        if cx >= 0 and cy >= 0:
            bisop_control_positions.append((cx, cy))
        if dx >= 0 and dy >= 0:
            bisop_control_positions.append((dx, dy))
    if wtower_pos in bisop_control_positions:
        return BBISHOP
    return DRAW


def play_game(size):
    """
    result: winner
    drow, bishop, tower
    """
    wtower_position = generate_random_position(size)
    bbishop_position = generate_random_position(size)
    while wtower_position == bbishop_position:
        bbishop_position = generate_random_position(size)

    result = check_winner(wtower_position, bbishop_position, size)
    print(
        f"Θέση πύργου:{wtower_position}, Θέση αξιωματικού:{bbishop_position}, Νικητής: {result}")
    return result


def play_many(number_of_games: int, board_size: int):
    results = []
    for _ in range(number_of_games):
        results.append(play_game(board_size))
    fdic = dict(Counter(results))
    print(f'\nΑποτελέσματα μετά από {number_of_games} παιχνίδια')
    for winner in sorted(fdic):
        print(f"{winner:22}: {fdic[winner]}")


if __name__ == '__main__':
    play_many(1000, (8, 8))
    # print(check_winner((0, 0), (3, 3), (8, 8)))
