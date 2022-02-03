import triliza_engine as ten


def test_check_win():
    win, pos = ten.check_win([[0, 0, 1], [0, 0, 1], [1, 0, 0], [0, 1, 0], [
                             0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0]])
    assert pos == (0, 1, 2)


def test_random_engine():
    for _ in range(10):
        number, _ = ten.play_random_game()
        assert number >= 3
