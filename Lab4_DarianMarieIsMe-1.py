'''Lab 4 Programming Assignment- Option 1
Darian Marie Bruce
This program simulates dealing a hand of cards to
the user
02/06/2026'''

import random

print("This program will deal you a hand of random cards.")

#check that input is valid

while True:
    users_cards = int(input("How many cards would you like to be dealt? Please input a valid amount. (1-52): "))
    if 1 <= users_cards <= 52:
        break
    else:
        print("Invalid input. Please enter a number between 1 and 52.")

#Per assignment instructions, cards are represented and abbreviated in a shorthand format

card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card_suits = ["h", "d", "c", "s"]

#create a list to hold the user's hand of cards

hand = []


print(f"You have requested {users_cards} cards. Here is your hand:")

# Logic to print hand of cards

while len(hand) < users_cards:
    card = random.choice(card_values) + random.choice(card_suits)
    if card not in hand:
        hand.append(card)
print(hand)