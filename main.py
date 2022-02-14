from poker.poker import deal, poker, hand_rank

if __name__ == '__main__':
    my_deck = [r + s for r in '23456789TJQKA' for s in 'SHDC']
    hands = deal(10, my_deck)
    winner_hands = poker(hands)
    for hand in winner_hands:
        print(hand, hand_rank(hand))
