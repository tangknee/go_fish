
from playing_cards import Playing_Cards as Cards

#print(sys.path)

#creates tuple of all cards in a playing card deck
game_deck = Cards.create_deck()

#creates a list of shuffled cards from the game deck
deck = Cards.shuffle_cards(game_deck)

#creates list of cards in hand and removes those cards from the shuffled cards
user_hand = Cards.draw_cards(deck, 5)
cpu_hand = Cards.draw_cards(deck, 40)

def user_request_cards():
    print('You ask: Do you have any... (2-10,JQKA?)')
    while True:
        u_req = input()
        if u_req == 'J' or u_req == 'Q' or u_req == 'K' or u_req == 'A':
            return u_req
            break
        elif int(u_req) > 1 and int(u_req) < 11:
            return u_req
            break
        else:
            print('Try input again.')
            continue

def check_cpu_hand(u_req):
    u_req_C = str(u_req + 'C')
    u_req_D = str(u_req + 'D')
    u_req_H = str(u_req + 'H')
    u_req_S = str(u_req + 'S')
    poss_cards = [u_req_C, u_req_D, u_req_H, u_req_S]

    print('you requested: ' + str(poss_cards))

    check = any(item in cpu_hand for item in poss_cards)
    cards_received = []

    if check is True:
        #print('Here are your cards')
        for card in poss_cards:

            if card in cpu_hand:
                cpu_hand.remove(card)
                user_hand.append(card)
                cards_received.append(card)

        print('You received: ' + str(cards_received))

        print('The following cards are in your hand: ', end='')
        Cards.print_cards(user_hand)

        fishing = False
        return fishing

    else:
        print('Go Fish')
        fishing = True
        return fishing

def go_fishing():
    print('You draw a card')



def check_book(hand):
    book = []
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
        return book


user_books = []
cpu_book = []


'''game loop'''
while True:
    print('The following cards are in your hand: ', end='')
    Cards.print_cards(user_hand)
    print('The following cards are in cpu''s hand: ', end='')
    Cards.print_cards(cpu_hand)


    user_books.append((check_book(user_hand)))
    user_books = list(filter(None, user_books))
    print(user_books)
    #book = check_book(cpu_hand)
    book = 0


    user_card_requested = user_request_cards()

    print('you requested: ' + str(user_card_requested))

    fishing = check_cpu_hand(user_card_requested)

    user_books.append((check_book(user_hand)))
    user_books = list(filter(None, user_books))
    print(user_books)

    if fishing is True:

        go_fishing()
    else:
        print('You are not fishing.')

    user_books.append((check_book(user_hand)))
    user_books = list(filter(None, user_books))
    print(user_books)


    continue

















    break
