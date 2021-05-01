
from playing_cards import Playing_Cards as Cards

#print(sys.path)

game_deck = Cards.create_deck()

deck = Cards.shuffle_cards(game_deck)

user_hand = Cards.draw_cards(deck, 5)
cpu_hand = Cards.draw_cards(deck, 5)

print(user_hand)
