
from playing_cards import Playing_Cards as Cards
import sys

#print(sys.path)

#creates tuple of all cards in a playing card deck
game_deck = Cards.create_deck()

#creates a list of shuffled cards from the game deck
deck = Cards.shuffle_cards(game_deck)

#creates list of cards in hand and removes those cards from the shuffled cards
user_hand = Cards.draw_cards(deck, 15)
cpu_hand = Cards.draw_cards(deck, 15)

def user_request_cards():
    print('You ask: Do you have any... (2-10,JQKA) ? ',end='')
    while True:
        u_req = input()
        if u_req == 'J' or u_req == 'Q' or u_req == 'K' or u_req == 'A':
            return u_req
            break
        elif u_req == '':
            print('Try input again.')
            continue
        elif int(u_req) > 1 and int(u_req) < 11:
            return u_req
            break
        else:
            print('Try input again.')
            continue

def cpu_AI(hand):

    import random

    request = 0

    dice = random.randint(1,3)

    if dice == 1:

        for card in hand:

            current_face = card[0]

            face_qty = 0
            for other_cards in hand:
                if current_face == other_cards[0]:
                    face_qty += 1

                if face_qty == 3:
                    request = current_face

    if request != 0:
        print('CPU asks: Do you have any... ' + str(request) + "'s?")
    else:
        choicelist = ['2', '3', '4', '5', '6', '7', '8', '10', 'J', 'Q', 'K', 'A']
        request = random.choice(choicelist)
        print('CPU asks: Do you have any... ' + str(request) + "'s?")

    return request



def check_hand(player_hand, req):
    req_C = str(req + 'C')
    req_D = str(req + 'D')
    req_H = str(req + 'H')
    req_S = str(req + 'S')
    poss_cards = [req_C, req_D, req_H, req_S]

    #print('you requested: ' + str(poss_cards))

    check = any(item in player_hand for item in poss_cards)
    cards_received = []

    if check is True:
        #print('Here are your cards')
        for card in poss_cards:

            if player_hand == cpu_hand:

                if card in player_hand:
                    player_hand.remove(card)
                    user_hand.append(card)
                    cards_received.append(card)

            if player_hand == user_hand:

                if card in player_hand:
                    player_hand.remove(card)
                    cpu_hand.append(card)
                    cards_received.append(card)

        if player_hand == cpu_hand:
            print('~~~~~ You Received: ' + str(cards_received) + ' ~~~~~')
        else:
            print('~~~~~ CPU Received: ' + str(cards_received) + ' ~~~~~')

        #print('The following cards are in your hand: ', end='')
        #Cards.print_cards(user_hand)
        print()

        fishing = False
        return fishing

    else:

        if player_hand == cpu_hand:

            print('~~~~~ CPU Says: Go Fish ~~~~~~~~')
        else:
            print('~~~~~ You Say: Go Fish ~~~~~~~~')

        fishing = True
        return fishing

def go_fishing(player):

    if len(deck) == 0:
        print('The Ocean is all fished out.')
    else:

        if player == user_hand:

            card = Cards.draw_card(deck)

            print('You draw a ' + str(card))
            print()
            print()
            player.append(card)

        if player == cpu_hand:

            card = Cards.draw_card(deck)
            player.append(card)

            print('CPU drew a card.', end=' ')
            print('CPU has ' + str(len(cpu_hand)) + ' cards.')
            print()


def check_book(hand):
    book = []
    point = 0  #quick test
    for card in hand:

        current_face = card[0]

        face_qty = 0
        for other_cards in hand:
            if current_face == other_cards[0]:
                face_qty += 1

            if face_qty == 4:
                book.append(card)

    for card in book:
        hand.remove(card)

    if book:

        #return book
        point = 1
    return point


def book_management(player, user_pts, cpu_pts):   #user_bks, cpu_bks): #something is wrong, books are not counting properly

    # user_bks = list(filter(None, user_bks))
    # cpu_bks = list(filter(None, cpu_bks))
    #
    # current_user_bks = len(user_bks)
    # current_cpu_bks = len(cpu_bks)
    #
    #
    #
    # user_bks.append((check_book(user_hand)))
    # user_bks = list(filter(None, user_bks))
    #
    # cpu_bks.append((check_book(cpu_hand)))
    # cpu_bks = list(filter(None, cpu_bks))
    point = 0
    point = check_book(player)


    # if player == user_hand:
    #     point


    user_pt_adder = 0
    cpu_pt_adder = 0

    if player == user_hand:
        if point > 0:
            user_pt_adder = point + user_pt_adder
    if player == cpu_hand:
        if point > 0:
            cpu_pt_adder = point + cpu_pt_adder

    global user_points
    global cpu_points

    user_points = user_points + user_pt_adder
    cpu_points = cpu_points + cpu_pt_adder

    if user_pt_adder > 0 or cpu_pt_adder > 0:
        print('You have ' + str(user_points) + ' books.')
        print('CPU has ' + str(cpu_points) + ' books.')
        print()

    if user_points > 6:
        print()
        print('YOU WIN')
        sys.exit()
    if cpu_points > 6:
        print()
        print('YOU LOSE')
        sys.exit()





    # if len(user_bks) > current_user_bks or len(cpu_bks) > current_cpu_bks:
    #
    #     print('You have ' + str(len(user_bks)) + ' books.')
    #     print('CPU has ' + str(len(cpu_bks)) + ' books.')

#intialize books for each player
user_books = []
cpu_books = []

global user_points
user_points = 0
global cpu_points
cpu_points = 0

#checks for books and displays to user
#book_management(user_hand, user_books, cpu_books)

'''game loop'''
while True:
    '''USER TURN'''
    #start with displaying cards in your hand
    print('The following cards are in your hand: ', end='')
    Cards.print_cards(user_hand)

    #print('The following cards are in cpu''s hand: ', end='')
    #Cards.print_cards(cpu_hand)

    #user's turn to request if cpu has requested face value
    user_card_requested = user_request_cards()

    book_management(user_hand, user_books, cpu_books)

    #check cpu hand with requested card and removes cpu cards
    fishing = check_hand(cpu_hand, user_card_requested)

    book_management(user_hand, user_books, cpu_books)

    #check to see if user needs to go fishing
    if fishing is True:

        go_fishing(user_hand)
        fishing = False

    book_management(user_hand, user_books, cpu_books)

    '''CPU TURN'''


    cpu_card_requested = cpu_AI(cpu_hand)

    input()

    book_management(cpu_hand, user_books, cpu_books)

    fishing = check_hand(user_hand, cpu_card_requested)

    book_management(cpu_hand, user_books, cpu_books)

    #check to see if CPU needs to go fishing
    if fishing is True:

        go_fishing(cpu_hand)

        fishing = False

    book_management(cpu_hand, user_books, cpu_books)


    continue
