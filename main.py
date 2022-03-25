rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
output = [rock, paper, scissors]
randomNum =0
choice = '0'
while(1==1):
  choice = int(input("enter your choice 1. Rock, 2. Paper 3. Scissors 4. Exit ")) -1
  randomNum = random.randint(0,2)
  if(choice == 4):
    break
  else:
    print("Your choice : \n ")
    print(output[choice ])
    print("Computer choice : \n ")
    print(output[randomNum])
    if(choice == randomNum):
      print("TIE retry")
    elif(choice<randomNum):
      if(choice ==0  and randomNum ==2):
        print("you win!!")
      else:
        print("you loose!!")
    else :
      if(choice ==2  and randomNum ==0):
        print("you loose!!")
      else:
        print("you win!!")
      
  
    
