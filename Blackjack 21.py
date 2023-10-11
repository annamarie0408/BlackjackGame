import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
bank = 0
bet = 0
count = 0
playerwins = False
tie = False

# Define functions for gameplay
def bank_value():
    global bank
    bank = input("How much does the guest start with?")
    try:
        if int(bank) > 0:
            bank = int(bank)
            print("You entered:", str(bank)) #Made for verifying that it took the int 
            return bank
    except ValueError:
        print("Invalid Bank Input")
        play_blackjack()



def request_wager():
    global bet
    print("\nYour bank is: ", bank)
    bet = input("How much do you want to bet? ")
    try:
        if int(bet) <= int(bank):
            bet = int(bet)
            return bet
        else:
            print("You cannot bet more than you have, Try Again")
            request_wager()
    except ValueError:
        print("Please enter a numeric response")


    

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
    print("Dealer's Hand:", dealer_hand[0], "Value:", values[dealer_hand[0].split()[0]])

def display_full_dealers_hand(dealer_hand):
    print("Dealer's Hand:", ', '.join(dealer_hand), "Value:", calculate_hand_value(dealer_hand))


def play_blackjack(count):
    global bank
    global bet
    #global count
    #global playerwins

    tie = False
    
    if count == 0:
        bank_value()
        
    
    request_wager()
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
            print("\nPlayer has Blackjack! Player wins!")
            playerwins = True
            bet = bet * 1.5 #If the player gets BlackJack, they win 1.5 the amount of their bet
            break
        elif calculate_hand_value(dealer_hand) == 21:
            display_full_dealers_hand(dealer_hand)
            print("\nDealer has Blackjack! Dealer wins!")
            playerwins = False
            break
        
        # Player's turn
        action = input("\nDo you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            deal_card(deck, player_hand)
            if calculate_hand_value(player_hand) > 21:
                display_table(player_hand, dealer_hand)
                print("Player busts! Dealer wins!")
                playerwins = False
                break
        elif action == 'stand':
            # Dealer's turns
            while calculate_hand_value(dealer_hand) < 17:
                deal_card(deck, dealer_hand)
            
            #display_table(player_hand, dealer_hand)
            
            if calculate_hand_value(dealer_hand) > 21:
                display_full_dealers_hand(dealer_hand)
                playerwins = True
            elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
                display_full_dealers_hand(dealer_hand)
                playerwins = True
            elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
                display_full_dealers_hand(dealer_hand)
                playerwins = False
            else:
                display_full_dealers_hand(dealer_hand)              
                tie = True
                playerwins = True
            
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'")

    if playerwins == True and tie == False:
        bank = bank + bet
        print("\nThe Player won! Their total bank is: ", str(bank))
    elif playerwins == False and tie == False:
        bank = bank - int(bet)
        print("\nThe player lost, their bank is: ", str(bank))
    elif playerwins == True and tie == True:
        print("It's a tie! No money is gain or lost. Bank is: ", bank)
        
    
    
    count+=1

    if bank == 0:
        print("\nGame over, please come back when you have $$")
        exit
    elif bank > 0:
        play_blackjack(count)

                  
play_blackjack(count)
