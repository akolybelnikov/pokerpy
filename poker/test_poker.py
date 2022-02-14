import unittest

from .poker import poker, hand_rank, card_ranks, straight, flush, kind

sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
fk = "9D 9H 9S 9C 7D".split()
fh = "TD TC TH 7C 7D".split()


class MyTestCase(unittest.TestCase):
    """test cases for the functions in the poker program."""

    @staticmethod
    def test_poker():
        pk = poker([sf, fk, fh])
        assert pk == sf
        assert poker([fk, fh]) == fk
        assert poker([fh, fh]) == fh
        assert poker([fh]) == fh
        assert poker([sf] + 99 * [fh]) == sf

    @staticmethod
    def test_hand_rank():
        assert hand_rank(sf) == (8, 10)
        assert hand_rank(fk) == (7, 9, 7)
        assert hand_rank(fh) == (6, 10, 7)

    @staticmethod
    def test_card_ranks():
        assert card_ranks(sf) == [10, 9, 8, 7, 6]
        assert card_ranks(fk) == [9, 9, 9, 9, 7]
        assert card_ranks(fh) == [10, 10, 10, 7, 7]

    @staticmethod
    def test_straight_flush():
        assert straight([9, 8, 7, 6, 5]) is True
        assert straight([9, 8, 8, 6, 5]) is False
        assert flush(sf) is True
        assert flush(fk) is False

    @staticmethod
    def test_kind():
        assert kind(4, card_ranks(fk)) == 9
        assert kind(3, card_ranks(fk)) is None
        assert kind(2, card_ranks(fk)) is None
        assert kind(1, card_ranks(fk)) == 7


if __name__ == '__main__':
    unittest.main()
