import random
option=("rock","paper","scissor")
while True:
    playerOption=input("enter your option(rock/paper/scissor)")
    computerOption=random.choice(option)
    print(f"\nYou chose {playerOption}.")
    print(f"\ncomputer chose {computerOption}.\n")
    if playerOption==computerOption:
       print("Tie")
    elif playerOption=="rock":
         if computerOption=="paper":
             print("You Lose")
         else:
              print("You Win")
    elif playerOption=="paper":
          if computerOption=="scissor":
              print("You Lose")
          else:
               print("You Win")
    elif playerOption=="scissor":
          if computerOption=="rock":
               print("You Lose")
          else:
                print("You Win")
    else:
         print("Invalid input.Please try again")
         continue
    play_again=input("do u want to play again?(y/n)")
    if play_again.lower()=="n":
     break
