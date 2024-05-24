"""
Колода карт
Игра в "Больше-меньше"
"""

import random

# Константы карт
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'Jack', 'Queen', 'King')
NCARDS = 8


# Проходим по колоде, и эта функция возвращает случайную карту из колоды
def get_card(deckListIn: list):
    return deckListIn.pop()


# Проходим по колоде, и эта функция возвращает перемешанную копию колоды
def shuffle(deckListIn: list):
    deckListOut = deckListIn[:]
    random.shuffle(deckListOut)
    return deckListOut


# Основной код
filler = f'{"":-^82}'
GRETING = """
----------------------HIGHER OR LOWER------------------------
Welcome to Higher or Lower.
_____________________________________________________________
You have to choose whether the next card to be shown will be 
higher or lower than the current card.
_____________________________________________________________
Getting it right adds 20 points; get it wrong and you lose 
15 points.
_____________________________________________________________
You have 50 points to start.

"""
print(GRETING)

starting_deck_list = []
for suit in SUIT_TUPLE:
    for value, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': value + 1}
        starting_deck_list.append(cardDict)

score = 50

# [print(el) for el in starting_deck_list]
while True:
    print()
    game_deck_list = shuffle(starting_deck_list)
    current_card_dict = get_card(game_deck_list)
    current_card_rank = current_card_dict['rank']
    current_card_suit = current_card_dict['suit']
    current_card_value = current_card_dict['value']
    print(f'Starting card is: {current_card_rank} of {current_card_suit}')
    print()
    for card_number in range(NCARDS):
        print(card_number)
        answer = input(f'Will the next card be higher or lower than the {current_card_rank} of'
                       f'{current_card_suit}? (enter +(higher) or -(lower)):  ')
        answer = answer.casefold()  # переводим в нижний регистр
        next_card_dict = get_card(game_deck_list)
        next_card_rank = next_card_dict['rank']
        next_card_suit = next_card_dict['suit']
        next_card_value = next_card_dict['value']
        print(f'Next card is: {next_card_rank} of {next_card_suit}')

        if answer == '+':
            if next_card_value > current_card_value:
                print('You got it right, it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15

        elif answer == '-':
            if next_card_value < current_card_value:
                print('You got it right, it was lower')
                score += 20
            else:
                print('Sorry, it was not lower')
                score -= 15

        print(f'Your score is: {score}')
        print()
        current_card_rank = next_card_rank
        current_card_value = next_card_value  # не нужна текущая масть

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break


print('OK bye')
print(f'Your score is {score}')