import e08_chess_tower_bishop as er8


def test_check_winner():
    assert er8.check_winner((0, 0), (3, 3), (300, 300)) == er8.BBISHOP
    assert er8.check_winner((0, 0), (289, 289), (3000, 3000)) == er8.BBISHOP
    assert er8.check_winner((0, 1000), (289, 1000), (3000, 3000)) == er8.WTOWER
