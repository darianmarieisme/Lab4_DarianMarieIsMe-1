'''Lab 4 Programming Assignment- Option 1
Darian Marie Bruce
This program simulates dealing a hand of cards to
the user
02/06/2026'''


print("This program will deal you a hand of random cards.")

users_cards = int(input("Please enter the number of cards you would like to be dealt: "))

#Per assignment instructions, cards are represented and abbreviated in a shorthand format

card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card_suits = ["h", "d", "c", "s"]

print(f"You have requested {users_cards} cards. Here is your hand:")

for i in range (users_cards):
    import random
    card_value = random.choice(card_values)
    card_suit = random.choice(card_suits)
    print(f"{card_value}{card_suit}")