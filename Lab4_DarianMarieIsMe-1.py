'''Lab 4 Programming Assignment- Option 1
Darian Marie Bruce
This program simulates dealing a hand of cards to
the user
02/06/2026'''

import random

print("This program will deal you a hand of random cards.")

users_cards = int(input("Please enter the number of cards you would like to be dealt: "))

#Per assignment instructions, cards are represented and abbreviated in a shorthand format

card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card_suits = ["h", "d", "c", "s"]

hand = []


print(f"You have requested {users_cards} cards. Here is your hand:")

while len(hand) < users_cards:
    card = random.choice(card_values) + random.choice(card_suits)
    if card not in hand:
        hand.append(card)
print(hand)