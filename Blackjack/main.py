from random import randint

import art

'''
- This is a simple game of Blackjack
    - The player will be dealt two cards and the computer will be dealt one card
    - The player can choose to hit or stand
    - If the player goes over 21, they lose
    - If the player gets 21, they win
    - If the player stands, the computer will hit until it reaches 17 or busts
    - If the computer busts, the player wins
    - If the computer has a higher hand value than the player, the player loses
- imported art file provided by 100 days of Code written by Dr. Angela Yu
'''

def game_start():
    print(art.logo)
    player_cards = [randint(1, 11) for _ in range(2)]
    comp_cards = [randint(1, 11)]
    
    hand_val = sum(player_cards)
    player_cards, hand_val = ace_check(player_cards, hand_val)
    
    print(f"\tYour cards: {player_cards}, Current Hand Value: {hand_val}")
    print(f"\tComputer's first card: {comp_cards[0]}")

    return player_cards, hand_val, comp_cards

def ace_check(cards, hand_val):
    while 11 in cards and hand_val > 21:
        cards[cards.index(11)] = 1
        hand_val = sum(cards)
    return cards, hand_val

def hit_player(player_cards):
    player_cards.append(randint(1,11))
    return player_cards

def hit_comp(comp_cards):
    keep_hitting = True
    while keep_hitting:
        comp_cards.append(randint(1, 11))
        comp_val = sum(comp_cards)
        comp_cards, comp_val = ace_check(comp_cards, comp_val)
        if comp_val > 21:
            keep_hitting = False
        elif comp_val <= 16:
            continue
        elif 17 <= comp_val <= 21:
            keep_hitting = False
    return comp_val


def final_hand_message(player_cards, hand_val, comp_cards):
    print(f"\tYour final cards: {player_cards}, Final Hand Value: {hand_val}")
    print(f"\tComputer's first card: {comp_cards}, Final Hand Value: {sum(comp_cards)}")
    print("You went over. You lose!!")
    main()

def hand_decision(comp_val, hand_val, player_cards, comp_cards):
    print(f"\tYour final cards: {player_cards}, Final Hand Value: {hand_val}")
    print(f"\tComputer's first card: {comp_cards}, Final Hand Value: {comp_val}")
    if comp_val > 21:
        print("Dealer Busted, You Win!!")
        main()
    elif comp_val >= hand_val:
        print("You Lose!!")
        main()
    else:
        print("You Win!!")
        main()
    

def main():
    while True:
        start_question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if start_question == "y":
            player_cards, hand_val, comp_cards = game_start()
            while True:
                hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")
                if hit_or_stand == "y":
                    player_cards = hit_player(player_cards)
                    player_cards, hand_val = ace_check(player_cards, sum(player_cards))
                    print(f"\tYour cards: {player_cards}, Current Hand Value: {hand_val}")
                    print(f"\tComputer's first card: {comp_cards}")
                    if hand_val > 21:
                        final_hand_message(player_cards, hand_val, comp_cards)
                        break
                    elif hand_val == 21:
                        print(f"\tYour cards: {player_cards}, Current Hand Value: {hand_val}")
                        print(f"\tComputer's first card: {comp_cards}")
                        comp_val = hit_comp(comp_cards)
                        hand_decision(comp_val, hand_val, player_cards, comp_cards)
                        break
                elif hit_or_stand == "n":
                    comp_val = hit_comp(comp_cards)
                    hand_decision(comp_val, hand_val, player_cards, comp_cards)
                    break
        elif start_question == "n":
            exit()
        

main()