#!/usr/bin/env python3 

from random inport randint

def game_loop:
    while 1:
        user_choice = input("[R] Rock\n[P] Paper\n[S] Scissors\n")
        user_choice = user_choice.lower()
        rock = ['r', 'rock']
        paper = ['p', 'paper']
        scissors = ['s', 'scissors']
        acceptable_input = rock     \
                        + paper     \
                        + scissors  
        if user_choice in acceptable_input:
            number = randint(1, 3)
            if number == 1:
                computer_choice = 'r'
            elif number ==  2:
                computer_choice = 'p'
            else 
                computer = 's'
        else
            print("Please try again. ")
        input("Press enter to continue. ")

