import random
from typing import Union

# Look-up table for all variations of counts patterns
count_rankings = {(5,): 10, (4, 1): 7, (3, 2): 6, (3, 1, 1): 3, (2, 2, 1): 2,
                  (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}


def poker(hands: list[list[str]]) -> list[str]:
    """Return the best hand: poker([hand,...]) => hand"""
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    result, max_val = [], None
    key = key or (lambda x: x)
    for x in iterable:
        x_val = key(x)
        if not result or x_val > max_val:
            result, max_val = [x], x_val
        elif x_val == max_val:
            result.append(x)
    return result


def group(items):
    """Return a list of [(count, x)...], the highest count first, then x first."""
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(pairs):
    """Convert a list of pairs into a par of lists"""
    return zip(*pairs)


def hand_rank(hand: list[str]) -> tuple:
    """Return a value indicating how high the hand ranks."""
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = max(ranks) - min(ranks) == 4 and len(ranks) == 5
    flush = len(set([s for r, s in hand])) == 1
    # 4*straight converts bool into int implicitly
    return max(count_rankings[counts], 4 * straight, 5 * flush), ranks


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


def deal(numhands: int, deck: list[str], n=5):
    """Use random to shuffle the deck of cards and create hands with n cards in each."""
    random.shuffle(deck)
    if numhands * n > len(deck):
        print("Not enough cards in the deck.")
        return
    hands = []
    for i in range(numhands):
        hands.append(deck[i * n:i * n + n])
    return hands
