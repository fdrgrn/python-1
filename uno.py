#Assume there is only 2 players and that players won't cheat and look at other players' cards
#You can add special cards later, 
import random

def start_game():
    colors = ('Blue', 'Green', 'Red', 'Yellow')
    ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    deck = [(rank, color) for rank in ranks for color in colors]
    random.shuffle(deck)

    p1 = [deck.pop() for _ in range(7)]
    p2 = [deck.pop() for _ in range(7)]

    center_card = deck.pop()
    turn = random.randint(1, 2)
    play_turn(p1, p2, deck, center_card, turn)

def play_turn(p1, p2, deck, center_card, turn):
    #Assign the turns cards
    #REREAD LATER, does Python attribute 'cards' as a pointer to p1 or p2?
    if turn == 1:
        cards = p1
    else:
        cards = p2

    print(f"\n \n The center card is: {center_card}")
    print(f"Player {turn}, your cards are: {cards}")

    #Playable cards
    available_cards = playable_cards(cards, center_card)
    print(f"Your playable cards are: {available_cards}")

    #Check if no cards are playable
    if len(available_cards) == 0:
        print("No cards can be played, you must DRAW")
        cards.append(deck.pop())
    else:
        choice = int(input("Do you want to PLAY A CARD(0) or DRAW A CARD(1)? "))
        if choice == 1:
            if len(deck) == 0:
                #Recheck later, might not be necessary or there might be a better way to do this
                print("Since the deck is empty, it will be reshuffled")
                #reshuffle_deck(deck, center_card)
            cards.append(deck.pop())
        elif choice == 0:
            card_choice = int(input(f"Pick which card to play through its place in the order, starting from 1: "))
            if 1 <= card_choice <= len(available_cards):
                deck.append(center_card)
                center_card = cards.pop(cards.index(available_cards[card_choice - 1]))
                if len(cards) == 1:
                    print("UNO!")
                if len(cards) == 0:
                    print(f"Player {turn} wins!")
                    return
            else:
                play_turn(p1, p2, deck, center_card, turn)

    #Change turns
    turn = 1 if turn == 2 else 2
    play_turn(p1, p2, deck, center_card, turn)

#Returns a list of all playable cards
def playable_cards(cards, center_card):
    return [card for card in cards if card[0] == center_card[0] or card[1] == center_card[1]]

#RESHUFFLE
#def reshuffle_deck(deck, center_card):
    #deck.append(center_card)
    #random.shuffle(deck)

#START THE GAME HERE
start_game()
