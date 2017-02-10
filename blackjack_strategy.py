# quick sketch proof of concept

import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # treat as infinite num decks

strategy = {(player_hand, dealer_up_card):
                {action: {'win': 0, 'draw': 0, 'loss': 0} for action in "hs"}
            for player_hand in range(4, 23)
            for dealer_up_card in range(2, 12)}


def calc_dealer_final_score(dealer_hand):
    while sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(deck))
    return sum(dealer_hand)


def update_outcome(outcome, player_final_score, dealer_final_score):
    if player_final_score > 21:
        outcome["loss"] += 1
    elif dealer_final_score > 21:
        outcome["win"] += 1
    elif player_final_score > dealer_final_score:
        outcome["win"] += 1
    elif player_final_score == dealer_final_score:
        outcome["draw"] += 1
    else:
        outcome["loss"] += 1


def update_player_score(player_score, action, deck):
    if action == 'h':
        return player_score + random.choice(deck)
    elif action == 's':
        return player_score


for _ in range(100000):

    player_start = [random.choice(deck), random.choice(deck)]
    dealer_start = [random.choice(deck), random.choice(deck)]

    player_total = sum(player_start)
    dealer_up_card = dealer_start[-1]

    dealer_final_score = calc_dealer_final_score(dealer_start)

    for action in "hs":
        player_final_score = update_player_score(player_total, action, deck)
        update_outcome(strategy[(player_total, dealer_up_card)][action], player_final_score, dealer_final_score)


for i in strategy:
    print(i, strategy[i])
