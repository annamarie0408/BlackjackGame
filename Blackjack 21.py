import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Define functions for gameplay

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)

def calculate_hand_value(hand):
    value = 0
    num_aces = hand.count('Ace of Hearts') + hand.count('Ace of Diamonds') + hand.count('Ace of Clubs') + hand.count('Ace of Spades')
    
    for card in hand:
        rank = card.split()[0]
        value += values[rank]
    
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    
    return value

def display_table(player_hand, dealer_hand):
    print("\nPlayer's Hand:", ', '.join(player_hand), "Value:", calculate_hand_value(player_hand))
    print("Dealers Hand:", ', '.join(dealer_hand), "Value:", calculate_hand_value(dealer_hand))

def play_blackjack():
    deck = create_deck()
    shuffle_deck(deck)
    
    player_hand = []
    dealer_hand = []
    
    # Deal initial cards
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)

    

    
    while True:
        display_table(player_hand, dealer_hand)
        
        # Check for blackjack
        if calculate_hand_value(player_hand) == 21:
            print("Player has Blackjack! Player wins!")
            break
        elif calculate_hand_value(dealer_hand) == 21:
            print("Dealer has Blackjack! Dealer wins!")
            break
        
        # Player's turn
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            deal_card(deck, player_hand)
            if calculate_hand_value(player_hand) > 21:
                display_table(player_hand, dealer_hand)
                print("Player busts! Dealer wins!")
                break
        elif action == 'stand':
            # Dealer's turn
            while calculate_hand_value(dealer_hand) < 17:
                deal_card(deck, dealer_hand)
            
            display_table(player_hand, dealer_hand)
            
            if calculate_hand_value(dealer_hand) > 21:
                print("Dealer busts! Player wins!")
            elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
                print("Player wins!")
            elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
                print("Dealer wins!")
            else:
                print("It's a tie!")
            
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'")
                  
play_blackjack()
