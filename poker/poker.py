import random
from typing import Union


def poker(hands: list[list[str]]) -> list[str]:
    """Return the best hand: poker([hand,...]) => hand"""
    return max(hands, key=hand_rank)


def hand_rank(hand: list[str]) -> tuple:
    """Return a value indicating the rank of a hand"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks)
    elif two_pair(ranks):
        return 2, two_pair(ranks), kind(1, ranks)
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks


def kind(n, ranks) -> Union[int, None]:
    """Return the first rank that this hand has exactly n of. Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks) -> Union[tuple, None]:
    """If there are two pair, return the two ranks as a tuple: (highest, lowest); otherwise return None."""
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return pair, low_pair
    return None


def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    if ranks[0] == 14 and ranks[1] == 5:
        n_ranks = ranks[1:]
        n_ranks.append(1)
        if straight(n_ranks):
            return n_ranks
    return ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand: list[str]) -> bool:
    return len(set([s for r, s in hand])) == 1


def deal(numhands: int, deck: list[str], n=5):
    random.shuffle(deck)
    if numhands * n > len(deck):
        print("Not enough cards in deck")
        return
    hands = []
    for i in range(numhands):
        hands.append(deck[i * n:i * n + n])
    return hands
