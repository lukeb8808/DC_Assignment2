"""
blackjack

Welcome to blackjack!
Try to beat the dealer by getting close to 21.

"""

import random
import time

def main():
    while True:
        home_screen = input("Do you want to start a game of Blackjack? (y/n): ").upper()
        if home_screen == "Y":
            start_game()
        elif home_screen == "N":
            print("Thank you for playing blackjack, Goodbye!")
            exit()
        else:
            print("Please enter \"y\" to start a new game or \"n\" to exit")

def start_game():
    deck = ["a K", "a Q", "a J", "a 10", "a 9", "an 8", "a 7", "a 6", "a 5", "a 4", "a 3", "a 2"]
    deck_dict = {"high ace":11,"low ace":1,"a K":10,"a Q":10,"a J":10,"a 10":10,"a 9":9,"an 8":8,"a 7":7,"a 6":6,"a 5":5,"a 4":4,"a 3":3,"a 2":2}
    player_card_1 = random.choice(deck)
    player_card_2 = random.choice(deck)
    player_total = deck_dict.get(player_card_1) + deck_dict.get(player_card_2)
    dealer_card_1 = random.choice(deck)
    dealer_hidden_card = random.choice(deck)
    dealer_total = deck_dict.get(dealer_card_1) + deck_dict.get(dealer_hidden_card)
    show_draw = f'''You draw {player_card_1} and {player_card_2} for a total of {player_total}.
The dealer draws {dealer_card_1} and has another card face down. \n'''
    for show in show_draw:
        print(show, end="", flush=True)
        time.sleep(.06)
    while player_total <= 21:
        choice = input("Hit or Stand? (H/S): ").upper()
        if choice == "H":
            new_card = random.choice(deck)
            player_total += deck_dict.get(new_card)
            new_total = f"You have drawn {new_card}, your total is now {player_total}. \n"
            if player_total > 21:
                new_total = f"You have drawn {new_card}, your total is now {player_total}.\nBusted! The dealer wins!\n"
        elif choice == "S":
            new_total = f"The dealers hidden card is {dealer_hidden_card}, The dealers total is {dealer_total}.\n"
        else:
            print("Invalid Entry. Enter \"H\" to hit or \"S\" to stand")
            continue
        for new in new_total:
            print(new, end="", flush=True)
            time.sleep(.06)
        if choice == "S":
            break
        if player_total > 21:
            main()

    while dealer_total <= 16:
        dealer_draw = random.choice(deck)
        dealer_total += deck_dict.get(dealer_draw)
        new_dealer_total = f"The dealer hits and draws {dealer_draw}. The dealers total is now {dealer_total}.\n"
        for new in new_dealer_total:
            print(new, end="", flush=True)
            time.sleep(.06)
        if dealer_total > 21:
            new_dealer_total = "The dealer has busted! You win!\n"
            break
    if 16 < dealer_total <= 21:
        new_dealer_total = "The dealer stands."

    next_line = f"Your total is {player_total} and the dealer's total is {dealer_total}."
    if player_total <= dealer_total <= 21:
        winner = f"{new_dealer_total} \n{next_line} \nThe dealer wins!\n"
    if player_total > dealer_total:
        winner = f"{new_dealer_total} \n{next_line} \nYou win!\n"
    if dealer_total > 21:
        winner = new_dealer_total
    for win in winner:
        print(win, end="", flush=True)
        time.sleep(.06)
    main()


if __name__ == '__main__':
    main()
