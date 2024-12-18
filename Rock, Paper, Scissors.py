import random                  

game= input("Rock Paper Scissors? or Pick a number 1-10!").lower()     #Do you want to play Rock Paper Scissors? or Pick a number 1-10!

if game == "rock paper scissors":                                      #if you chose rock paper scissors
    score = 0                                                          #your score is 0
    options = ['rock', 'paper', 'scissors','stick']                    #the options are rock paper or scissors
    score_limit = 10                                                   #score limit is ten
    while score <score_limit:                                          
        user_guess = input("Rock,Paper or Scissors?").lower()          #you can gues rock paper or scissors
        computer = random.choice(options)                              #the computer will generate
        print(f"user chose{user_guess},but computer chose{computer}")  #show what the compuer chose after the user picked there option 

        if user_guess == "rock" and computer == "scissors":            #user guess rock and the computer guesses scissors
           print("you win!")                                           #say you win!
           score +=1                                                   #you gain a piont
        elif user_guess == "rock" and computer == "rock":              #user guess rock and computer guesses
             print("try again!")                                       #say try again
        elif user_guess == "rock" and computer == "paper":             #user guess is rock and computer guess is paper
             print("you loose!")                                       #say you loose
             score -=1                                                 #score is subtratced
        elif user_guess == "paper" and computer == "rock":             #user guess is paper and computer guess is rock
             print("you win!")                                         #say you win
             score +=1                                                 #add to your score
        elif user_guess == "paper" and computer == "paper":            #user guess is paper and computer guess is paper
             print("try again!")                                       #say try again
        elif user_guess == "paper" and computer == "scissors":         #user guess is paper and computer is siccors 
             print("you loose!")                                       #say you loose
             score -=1                                                 #you score is subtratced
        elif user_guess == "stick" and computer == "scissors":         #user guess is stick and computer is siccors 
             print("you loose!")                                       #say you loose
             score -=1                                                 #your score is subtracted 
        elif user_guess == "scissors" and computer == "paper":         #user guess is scissors and computer guess is paper
             print("you win!")                                         #say you win
             score +=1                                                 #your score goes up
        elif user_guess == "scissors" and computer == "scissors":      #user guess is scissors and computer guess is scissors
             print("try again!")                                       #say try again
        elif user_guess == "scissors" and computer == "rock":          #user guess is scissors and computer is rock
             print("you loose!")                                       #say you loose
             score -=1                                                 #your score is subtratced
        else:
            print ("invaldid responses")                               #print invaldi repsonse
        print("your score is", score)                                  #print your score

elif game == "pick a number 1-10!":                                    #user picks the 1-10 game
    print("               /A\,")                                       #display this image
    print("            .//`_`\\,")                                     #display this image
    print("          ,//`____-`\\,")                                   #display this image
    print("        ,//`[_ROVER_]`\\,")                                 #display this image
    print("      ,//`=  ==  __-  _`\\,")                               #display this image
    print("      //|__=  __- == _  __|\\")                             #display this image
    print("      ` |  __ .-----.  _  | `")                             #display this image
    print("        | - _/       \-   |")                               #display this image
    print("        |__  | .-'-. | __=|")                               #display this image
    print("        |  _=|/)   (\|    |")                               #display this image
    print("        |-__ (/ a a \) -__|")                               #display this image
    print("        |___ /`\_Y_/`\____|")                               #display this image
    print("             \)8===8(/")                                    #display this image
    score = 0                                                          #score is zero
    options = ['1','2','3','4','5','6','7','8','10']                   #options the user can say
    score_limit = 10                                                   #the score limit
    
    while score <score_limit:                                          #score limit
        user_guess = input("Pick a number 1-10!")                      #The user writes pick a number 1-10
        computer_guess = random.choice(options)                        #compouter generates a random choice
        print(f"user chose {user_guess},but we chose {computer_guess}")#the user choice htere guess but the computer choice the computer guess
        if user_guess == computer_guess:                               #if user guess is the same as computer guess
           print ("You win!")                                          #you win
           score +=1                                                   #your score goes up one
        elif user_guess!= computer_guess:                              #if user guess is different as computer guess
           print ("You loose!")                                        #say you loose              
           score -=1                                                   #score goes down
        else:
            print ("invaldid responses")                               #print invaldi repsonse
        print("your score is", score)                                  #print your score


