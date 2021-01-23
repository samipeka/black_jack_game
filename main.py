############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
###############################################################

import random
from replit import clear
from art import logo

#Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace.

def deal_card():
    """Deals one card..."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 
instead of the actual score. 0 will represent a blackjack in our game.

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0   
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same 
# score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the
# player with the highest score wins.

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "Loose, opponent has BlackJack"    
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You loose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
       
    #The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of BlackJack Type 'y or 'n': ") == "y":
    clear()
    play_game()
