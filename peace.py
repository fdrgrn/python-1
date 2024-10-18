# Import necessary modules

#.extend is like .append, but  multiple

import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Split the deck into two hands
p1 = [deck.pop() for _ in range(26)]
p2 = [deck.pop() for _ in range(26)]

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here
    return 1 if ranks.index(p1_card[0]) > ranks.index(p2_card[0]) else 2 if ranks.index(p1_card[0]) < ranks.index(p2_card[0]) else 0

def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here
    if len(player1_hand) == 0 or len(player2_hand) == 0:
        return

    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)

    print(f"Player 1's Card: {card1}, Player 2's Card: {card2}")

    outcome = card_comparison(card1, card2)

    if outcome == 0:
        print("Peace")
        war(player1_hand, player2_hand, [card1, card2])
    elif outcome == 1:
        print("Player 1 has won the round")
        player1_hand.extend([card1, card2])
    else:
        print("Player 2 has won the round")
        player2_hand.extend([card1, card2])

def war(player1_hand, player2_hand, list):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down,
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.
	"""
    # Your code here
    if len(player1_hand) < 4 or len(player2_hand) < 4:
        #Ask what to do at this point later
        print("ERROR ask what to do later")
        exit() #Maybe return

    tally = list + [player1_hand.pop(0) for _ in range(3)] + [player2_hand.pop(0) for _ in range(3)]
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)
    print(f"Player 1's Peace Card: {card1}0, Player 2's Peace {card2}")

    outcome = card_comparison(card1, card2)
    if outcome == 0:
        print("Peace")
        war(player1_hand, player2_hand, tally + [card1, card2])
    elif outcome == 1:
        print("Player 1 wins peace")
        player1_hand.extend(tally + [card1, card2])
    else:
        print("Player 2 wins peace")
        player2_hand.extend(tally + [card1, card2])

def play_game():
    """Main function to run the game."""
    # Your code here
    #Add quality of life stuff here, maybe info on remaining cards
    while len(p1) > 0 and len(p2) > 0:
        play_round(p1, p2)

        if len(p1) == 0:
            print("Player 2 has won")
            exit()
        elif len(p2) == 0:
            print("Player 1 has won")
            exit()

# Call the main function to start the game
play_game()
