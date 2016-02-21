import random

# Question: on average, how many turns does it take to finish a game of War?


class Deck(object):
    def __init__(self):
        self.cards = range(13) * 4  # suites do not matter, only value
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def size(self):
        return len(self.cards)


class Player(object):
    def __init__(self):
        self.hand = []
        self.discardPile = []

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def add_card_to_discard_pile(self, card):
        self.discardPile.append(card)

    def play_card(self):
        if self.hand:
            return self.hand.pop()
        if self.discardPile:
            random.shuffle(self.discardPile)  # shuffle to avoid infinite loop
            self.hand = self.discardPile[::]
            self.discardPile = []
            return self.hand.pop()
        return None  # the last played card will be the war card

    def get_number_of_cards(self):
        return sum([len(self.hand), len(self.discardPile)])


class CardGameWar(object):
    def __init__(self):
        self.players = [Player(), Player()]
        self.deal_starting_cards_to_players()
        self.warPiles = [[], []]  # for player zero and one
        self.isGameOver = False
        assert len(self.players[0].hand) == len(self.players[1].hand) == 26

    def deal_starting_cards_to_players(self):
        deck = Deck()
        dealToPlayer = 0
        while deck.size() > 0:
            self.players[dealToPlayer].add_card_to_hand(deck.deal_card())
            dealToPlayer ^= 1  # xor flips between zero and one

    def both_players_play_card_to_war_pile(self):
        self.warPiles[0].append(self.players[0].play_card())
        self.warPiles[1].append(self.players[1].play_card())

    def add_war_piles_to_player(self, player):
        for pile in self.warPiles:
            for card in pile:
                player.add_card_to_discard_pile(card)

    def play_turn(self):
        self.both_players_play_card_to_war_pile()

        if self.warPiles[0][-1] is None or self.warPiles[1][-1] is None:
            self.isGameOver = True
            # Game OVER!
            return

        while self.warPiles[0][-1] == self.warPiles[1][-1]:
            for i in range(4):
                self.both_players_play_card_to_war_pile()

        if self.warPiles[0][-1] is None or self.warPiles[1][-1] is None:
            self.isGameOver = True
            # Game OVER!
            return

        if self.warPiles[0][-1] > self.warPiles[1][-1]:
            self.add_war_piles_to_player(self.players[0])
        else:
            self.add_war_piles_to_player(self.players[1])

        assert sum(player.get_number_of_cards() for player in self.players) == 52

    def clean_up_turn(self):
        self.warPiles = [[], []]

    def simulate_game(self):
        count = 0
        while not self.isGameOver:
            count += 1
            self.play_turn()
            self.clean_up_turn()

        return count


numTrials = 500
numTurnsToFinishGame = 0.
for trial in range(numTrials):
    game = CardGameWar()
    numTurnsToFinishGame += game.simulate_game()

print "After {} trials, the average game of War took {} turns.".format(numTrials, numTurnsToFinishGame/numTrials)
