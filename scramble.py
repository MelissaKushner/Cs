import random                                                                                                      #import random                                                                        
 
name = input("what is your name?")                                                                                 #computer asks user for name                                                               
print("Goodluck", name)                                                                                            #display message "goodluck;name                                                      
words = ['computer','science','programming','pthyon','logic','board','game','condition']                           #list of words:computer,science,programming,python,log,board,game,condi
games,wins = 0,0                                                                                                   #amount of games set to zero
                                                                                                                   #amount of wins set zero
while True:                                                                                                        #forver loop
    turns = 5                                                                                                      #amount of turns is set to 5    
    word = random.choice(words)                                                                                    #set word to random element from list words 
    display = list(word)                                                                                           #scramble list 
    random.shuffle(display)                                                                                        #turn list back into word   
    display = ''.join(display)
    
    while turns > 0:                                                                                               #while turns >0 
        guess = input(f"Unscramble {display}, enter real word here: ")                                             #set guess to input unscramble display and says enter real word here

        if guess == word:                                                                                          #if guess is the same at the word
            print('you got it')                                                                                    #print"you got it
            score +=1                                                                                              #add 1 to score
            break                                                                                                  #end loop

        while True:                                                                                                #forver loop
            scramble= input("You did not get the word, would you like to unscramble? Enter yes or no")             #set scramble to input you did not get the word. Would you like to rescramble?Enter y or no

            if scramble== "no":                                                                                    #if user says no
                break                                                                                              #end loop
            elif scramble== "yes":                                                                                 #else if user says "y"
                display = list(word)                                                                               #set display to converting word to list
                random.shuffle(display)                                                                            #scramble list 
                display = ''.join(display)                                                                         #turn list back into word
                break    end loop
            else:                                                                                                  #if user says something else 
                print("invalid response")                                                                          #print invalid response

        turns -= 1                                                                                                 #subrtact 1 turn

    print("The word was (words)")                                                                                  #print "the word was(whatver word was answer
    games +=1 add 1 to games 

    while True:                                                                                                    #forever loop
        playagain= input(f"{name}, you have won {wins} out of {games}. Would you like to play again? yes or no? ") #set play again to input(user name, you have win (# of games won) outof (#of games played) games. Would you like to play again y/n. 
        
        if playagain== "no":                                                                                       #if plan again is n
            exit()                                                                                                 #end code
        elif playagain=="yes":                                                                                     #else if play again is y 
            break                                                                                                  #end loop
        else:                                                                                                      #if user says anything else
            print("invalid response")                                                                              #print invalid response
                
        
