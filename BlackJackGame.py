import random

global deal_stand
global play_stand
deal_stand = False
play_stand = False


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append({suit:rank})
        self.hand_cards = []
        self.shuffle()


    def __str__(self):
        return str(self.deck)


    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self, a_deck):
        self.hand_cards.append(a_deck.deck[-1])
        a_deck.deck.pop()
        self.hand_cards.append(a_deck.deck[-1])
        a_deck.deck.pop()

        self.card_1 = f"{list(self.hand_cards[0].keys())[0]} of {self.hand_cards[0][list(self.hand_cards[0].keys())[0]]}"
        self.card_2 = f"{list(self.hand_cards[1].keys())[0]} of {self.hand_cards[1][list(self.hand_cards[1].keys())[0]]}"
        self.card_list = [self.card_1, self.card_2]

class hand(deck):

    def __init__(self):
        deck.__init__(self)
        self.value = 0
        self.aces = 0
        self.deal(the_deck)

        self.key1 = self.hand_cards[0][list(self.hand_cards[0].keys())[0]]
        self.val1 = values[self.hand_cards[0][list(self.hand_cards[0].keys())[0]]]
        self.key2 = self.hand_cards[1][list(self.hand_cards[1].keys())[0]]
        self.val2 = values[self.hand_cards[1][list(self.hand_cards[1].keys())[0]]]
        self.temp_val = 0

        self.value += self.val1
        self.value += self.val2

    def add_card(self):
        self.hand_cards.append(the_deck.deck[-1])
        the_deck.deck.pop()
        self.temp_val = values[self.hand_cards[int(len(self.hand_cards)) - 1][list(self.hand_cards[int(len(self.hand_cards)) - 1].keys())[0]]]
        self.value += self.temp_val

        self.card_new = f"{list(self.hand_cards[int(len(self.hand_cards)) - 1].keys())[0]} of {self.hand_cards[int(len(self.hand_cards)) - 1][list(self.hand_cards[int(len(self.hand_cards)) - 1].keys())[0]]}"
        self.card_list.append(self.card_new)


        if self.val1 == 11:
            if int(input("Do you want your ace to be 11 or 1?")) == 1:
                self.value -= 10

        if self.val2 == 11:
            if int(input("Do you want your ace to be 11 or 1?")) == 1:
                self.value -= 10

        if self.temp_val == 11:
            if int(input("Do you want your ace to be 11 or 1?")) == 1:
                self.value -= 10


    def adjust_ace(self):
        if self.val1 == 11:
            if int(input("Do you want your ace to be 11 or 1?")) == 1:
                self.value -= 10

        if self.val2 == 11:
            if int(input("Do you want your ace to be 11 or 1?")) == 1:
                self.value -= 10

        if self.temp_val == 11:
            if int(input("Do you want your ace to be 11 or 1?")) == 1:
                self.value -= 10

    def show_all_cards(self):

        print(f"{self}'s cards: ")
        for card in self.card_list:
            print(card)
        print("")

    def show_some(self):
        self.half_list = self.card_list
        self.half_list.pop(0)
        print(f"{self}'s last {int(len(self.hand_cards)) - 2}:")
        for card in self.half_list:
            print(card)
        print("")









class chips(hand):
    """
    This is where the instances will be made.
    Keeps track of bets and the balance.
    """

    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.curr_bet = 0
        hand.__init__(self)

    def choose_bet(self, opponent):
        """
        Here you choose the player's bet.
        """
        while True:
            while True:
                try:
                    self.curr_bet = int(input("How much do you want to bet?"))
                    break
                except TypeError:
                    print("You have to choose a number!")

            if self.curr_bet > self.balance or self.curr_bet < 0 or self.curr_bet > opponent.balance:
                print("You do not have enough funds or the bet was lower than zero. Please choose again.")
            else:
                break

    def winorlose_bet(self, opponent):
        """
        This will determine who won the round and then adjust all balances.
        """
        if  self.value > 21 and opponent.value > 21:
            pass

        elif (self.value > opponent.value and self.value <= 21) or opponent.value > 21:
            self.balance += self.curr_bet
            opponent.balance -= self.curr_bet

        if  self.value > 21 and opponent.value > 21:
            pass

        elif (opponent.value > self.value and opponent.value <= 21) or self.value > 21:
            self.balance -= self.curr_bet
            opponent.balance += self.curr_bet

    def show_balance(self, opponent):
        print(self.balance)
        print(opponent.balance)

    def __str__(self):
        return self.name




def present_some(player, dealer):
    player.show_all_cards()
    dealer.show_some()

def present_all(player, dealer):
    player.show_all_cards()
    dealer.show_all_cards()


def hit(player):
    player.add_card()



def continue_playing():
    while True:
        answer = input("Do you want to playe again?(Yes or No)").lower()
        if answer == "yes":
            playing = True
            break

        elif answer == "no":
            playing = False
            break

        else:
            print("You have to answer yes or no!")




def hit_stand(player, dealer):
    while True:
        answer = input("Do you want to hit or stand?").lower()

        if answer == "hit":
            hit(Player)
            if dealer.value < 17:
                hit(dealer)
            else:
                deal_stand = True
            break
        elif answer == "stand":
            play_stand = True
            if dealer.value < 17:
                hit(dealer)
            else:
                deal_stand = True
            break
        else:
            print("You have to choose either hit or stand!")







the_deck = deck()


Player = chips(input("What is your name?"))
bot = chips("Bot")


present_all(Player, bot)
Player.show_balance(bot)




"""
the_deck = deck()


player = chips("Player")
bot = chips("Bot")

print(f"Bot: {bot.hand_cards}")
print(f"Player: {player.hand_cards}")

print(player.balance)

player.choose_bet(bot)

player.winorlose_bet(bot)


print(player.balance)
print(bot.balance)

player.add_card()
bot.add_card()

print(player.hand_cards)
print(bot.hand_cards)

player.winorlose_bet(bot)

player.tell_all_cards()
print(player.balance)
print(bot.balance)

"""






"""

my_hand = hand()


print(my_hand.hand_cards)

my_hand.adjust_ace()

print(my_hand.key1)
print(my_hand.val1)
print(my_hand.key2)
print(my_hand.val2)
print(my_hand.value)


my_hand.add_card()

print(my_hand.hand_cards)

(my_hand.tell_all_cards())

"""

