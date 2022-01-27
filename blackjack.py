import random
import os
from art import logo


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    randcard = random.choice(cards)
    return randcard


def calculate_score(cards):
    """Take a list of cards and return the score calculated from cards """

    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw")
    elif computer_score == 0 or user_score > 21:
        print("You lose")
    elif user_score == 0 or computer_score < 21:
        print("You win")

    elif user_score > computer_score:
        print("You win")
    else:
        print("You lose")


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards} , current score : {user_score} ")
        print(f"Computer's first card : {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            users_choice = input(
                "Type 'y' to get another card and 'n'to deny : ")
            if users_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(
        f"Your final score is : {user_cards} , final score is : {user_score}")
    print(
        f"Your final score is : {computer_cards} , final score is : {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of BlackJack ? Type 'y' for yes and 'n' for no ") == "y":
    clearConsole()
    play_game()
