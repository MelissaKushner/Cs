import random


def reverse_string(string):                         #REVERSE A STRING
    return string[::-1]                             #FIRST PARAMATER IS STARTING POS, SECOND PARM IS END, THIRD IS DIRECTION


def count_vowels(name):                                  #COUNTS THE VOWELS
    vowels = ['A'',a','E','e','I','i','O','o','U','u']   #ALL THE VOWELS UPPER AND LOWER CASE
    for letter in name:                                  #FOR EVERY LETTER IN THE NAME WITH A VOWEL
            vc = vc+1                                    #VOWEL COUNT GOES UP !
            vc = count_vowels(name)                      #VOWEL COUNT IS COUNT THE VOWEL    

    return vc                                            #RETURN VOWEL COUNT 
def count_consonant(name):                               #COUNTS THE CONSONANTS 
    alphabet = ['B','b','C','c','D','d','F','f','G','g','h','J','j','K','k','L','l','M','m','N','n','P','p','Q','q','R','S','s','T','t','V','v','W','w','X','x','Y','y','Z','z']  #ALL THE LETTWERS IN THE ALPHABET UPPER AND LOWERCASE EVERYTHING BUT CONSONANTS
    for letter in name:                                  #FOR EVERY LETTER IN THE NAME WITH A CONSONANT
        if letter in alphabet:                           #IF THE FOLLOWING LETTERS IN LIST ARE IN THE NAME 
            cc = cc+1                                    #CONSONANT COUNT GOES UP 1
            cc = count_consonant(name)                   #CONSONANT COUNT IS COUNT THE CONSONANTS 
    
    return cc                                            #RETURN CONSONANT COUNT 


def first_name(name):                                    #FIND THE FIRST NAME
    output = ""                                          #YOU DONT KNOW THE NAME SO THE OUTPUT IN EMTY
    for letter in name:                                  #FOR EVERY LETTER IN NAME
        if letter == " ":                                #IF LETTER IS BEFORE THE SPACE
            break                                        #BREAK
        else:                                            #THEN
            output = output + letter                     #OUTPUT IS THE OUTPUT AND LETTER
    return output                                        #RETURN THE OUTPUT

def last_name(name):                                     #FIND THE LAST NAME
    for index in range(len(name)-1,-1,-1):              
        if name[index] == ' ':
            break
        else: 
            output = output + name[index]
    return reverse_string(output)                       #RETURN REVERSE STRING



def middle_name(name):                                  #FIND MIDDLE NAME 
    beg = 0                                             #START AT 0
    for index in range(0,len(name)-1):                  #FOR INDEX IN RANGE START AT 0 AND GO TO NEG 1
        if name[index] == ' ':                          #IF NAME INDEX IS NOTHING
            break                                       #BREAK
    else:                                               #THEN
         beg = beg +1                                   #GO TO THE BEGGING AND ADD ONE 

    end = len(name)-1                                   #

    for index in range(len(name)-1,-1,-1):
        if name[index] == ' ':
            break
    end = end -1

def upper_case(name):                                   #FIND UPPER CASE 

    for letter in name:                                 #FOR LETTER IN NAMEn
        if ord(letter) >64  and ord(letter) <91:
            num = ord(letter)
        num = num + 32
        letter = char(num)
        nameout = nameout + letter
    else: 
        nameout = nameout + letter
        return nameout

def lower_case(name):
    for letter in name:
        if ord(letter) > 96 and ord(letter) <122:
            num = ord(letter)
        num = num - 32
        letter = char(num)
        nameout = nameout + letter
    else: 
        nameout = nameout + letter
        return nameout

    
def main():

    name = input("enter your full name: ")

    print('1. to reverse string')

    choice = input("enter choice")
    
    if choice == '1':
         output = reverse_string(name)
         print(output)

    if choice == '2':
         output = count_vowels(name)
         print(output)
        
    elif choice == '3':
         output = count_consonant(name)
         print(output)
    
    elif choice == '4':
         output = first_name(name)
         print(output)

    elif choice == '5':
         output = last_name(name)
         print(output)
        
    elif choice == '6':
         output = middle_name(name)
         print(output)
    else:
        print("i dont know what to do..")
 

main()



   
  

    