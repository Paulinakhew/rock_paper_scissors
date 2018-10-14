#!/usr/bin/env python3 

import model as m

def game_loop():
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
            computer_choice = m.computer_choice()
            win = 0
            loss =0
            if user_choice in rock:
                print("r vs {}".format(computer_choice))
                if user_choice == computer_choice:
                    print("Draw")
                elif computer_choice == 'p':
                    print("Computer wins")
                    loss +=1 
                else:
                    print("You win")
                    win += 1
            elif user_choice in paper:
                print("p vs {}".format(computer_choice))
                if user_choice == computer_choice:
                    print("Draw")
                elif computer_choice == 's':
                    print("Computer wins")
                    loss +=1 
                else:
                    print("You win")
                    win +=1 
            elif user_choice in scissors:
                print("s vs {}".format(computer_choice))
                if user_choice == computer_choice:
                    print("Draw")
                elif computer_choice == 'r':
                    print("Computer wins")
                    loss +=1 
                else:
                    print("You win")
                    win +=1 
            else:
                print("Error")
            print("You have won {} times and lost {} times".format(win, loss))
        else:
            print("Please try again. ")
        input("Press enter to continue. ")

if __name__=="__main__":
    game_loop()

