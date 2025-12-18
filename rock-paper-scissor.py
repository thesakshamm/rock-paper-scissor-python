import random

items = [1,2,3]

win_count = 0
lose_count = 0
tie_count = 0

while(True):
    print("\nROCK PAPER AND SCISSORS GAME\n")
    computer_output = (random.choice(items))
    user_input = int(input("PRESS:\n 1 for ROCK\n 2 for PAPER\n 3 for SCISSOR\n ==>"))
    
    
    if user_input == computer_output:
        tie_count = tie_count + 1
        print("\nIT'S A TIE!")
        
    elif  ((user_input == 1 and computer_output == 3) or 
         (user_input == 2 and computer_output == 3 )or
         (user_input == 3 and computer_output == 2)
         ):
        win_count = win_count + 1
        print("\nYOU WIN!!")
        
        
        
    else:
        print("\nYOU LOSE!")
        lose_count = lose_count + 1
        
        
        
    #to print computer output
    if computer_output == 1:    
        print("\ncomputer:  rock")
    elif computer_output == 2:    
        print("\ncomputer: paper")
    elif computer_output == 3:    
        print("\ncomputer: scissor")
        
        
     #to print computer output
    if user_input == 1:    
        print("you: rock")
    elif user_input == 2:    
        print("you: paper")
    elif user_input == 3:    
        print("you: scissor")
        
    
    play_again = input("\n\npress 'y' if you want to play again.\npress any key to exit.\n ")
    
    
                   
    if play_again == "y":
        print("LETS PLAY AGAIN!!!")
    else:
        print("Your Score: ", win_count)
        print("Computer Score: ", lose_count)
        break
    
 
    
 #FIRST CODE   
"""
rock = 1    
paper 2
scissor = 3
"""

"""#MAIN GAME
if user_input == computer_output:
    print("tie")
    
#for rock
if user_input == 1 and computer_output == 3:
    print ("you win")
elif user_input == 1 and computer_output == 2:
    print ("you lose")
    
#for paper 
if user_input == 2 and computer_output == 3 :
    print ("you lose")   
elif user_input == 2 and computer_output == 1:
    print ("you win")    
    
#for scissor
if user_input == 3 and computer_output == 1:
    print ("you lose")
elif user_input == 3 and computer_output == 2:
    print ("you win")
    
"""


    

    
    


    

    
