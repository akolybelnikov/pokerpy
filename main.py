from poker.poker import kind, two_pair, card_ranks, deal, poker, hand_rank

if __name__ == '__main__':
    my_deck = [r + s for r in '23456789TJQKA' for s in 'SHDC']
    hands = deal(10, my_deck)
    winner_hand = poker(hands)
    winner_rank = hand_rank(winner_hand)
    print(winner_rank, winner_hand)
