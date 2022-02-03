import random

VICTORY_POSITIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


def check_win(game_board) -> bool:
    """
    check wining positions for a table
    """
    board = game_board[:]
    tablevalues = [any(cell) for cell in board]
    for position in VICTORY_POSITIONS:
        if all([tablevalues[i] for i in position]):
            print(position)
            return True, position
    return False, [-1, -1, -1]


def play_random_game():
    """"
    returns (number_of_iterations, gameboard)
    """
    gameboard = [
        [0, 0, 0], [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0], [0, 0, 0]
    ]
    # print('gb', gameboard)
    number_of_iterations = 0
    win = False
    while not win:
        number_of_iterations += 1
        position = random.randrange(9)
        pouli_position = random.randrange(3)
        if gameboard[position][pouli_position] == 0:
            gameboard[position][pouli_position] = 1
        win, _ = check_win(gameboard)
    # print('->', number_of_iterations)
    return number_of_iterations, gameboard


def play_many_random_games(number_of_games: int):
    """
    Plays many random games
    returns
    mean value of numbe of iterations per game
    """
    iterations_per_game = []
    for _ in range(number_of_games):
        itnum, gameboard = play_random_game()
        iterations_per_game.append(itnum)
        print(gameboard, itnum)
    return round(sum(iterations_per_game) / len(iterations_per_game), 1)


if __name__ == '__main__':
    print(play_many_random_games(100))
    # print(play_randomly())
