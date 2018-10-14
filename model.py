#!/usr/bin/env python3 

from random import randint
def computer_choice():
    number = randint(1, 3)
    if number == 1:
        computer_choice = 'r'
    elif number ==  2:
        computer_choice = 'p'
    else: 
        computer_choice = 's'
    return computer_choice