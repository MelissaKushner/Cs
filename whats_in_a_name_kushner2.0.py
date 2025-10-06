'Melissa Kushner'
'Date Created:9/4/2025'
'Last Modified: 9/29?2025'
'Python Version 1.0'
'Description: Takes your name a lets you do different'


import random
def reverse_string(string): 
    '''
    takes a string and reverses it 
    Args:
        string(name) 
    Returns:
        str: revered name 
    '''                                                                                           
    return string[::-1]                                                      
def count_vowels(name):     
    '''
    counts vowels of the name
    Args:
        name(stirng)
    Returns:
        name: vowels of name 
    '''                                                                      
    vowels = ['A','a','E','e','I','i','O','o','U','u']                       
    vc = 0

    for letter in name:                                                       
        if letter in vowels:
            vc += 1  
    return vc                                                                

def count_consonant(name):   
    '''
    counts the consonants of the name
    Args:
        name(string)
    Retunrs:
        name: consonants of the name
    '''                                             
    consonants = ['B','b','C','c','D','d','F','f','G','g','h','J','j','K','k','L','l','M','m','N','n','P','p','Q','q','R','S','s','T','t','V','v','W','w','X','x','Y','y','Z','z']  #ALL THE LETTWERS IN THE ALPHABET UPPER AND LOWERCASE EVERYTHING BUT CONSONANTS
    cc = 0
    
    for letter in name:                                                     
        if letter in consonants:                                             
            cc+= 1                                                          
    return cc                                                               

def get_names(fullname):                                                      
    '''
    creates a split function 
    Args:
        name
    Returns:
        parts of name
    '''
    names = []                                                            

    for letter in fullname:
        if letter == ' ':
            names.append(name)
            name = '' 
        else: 
            name += letter
    names.append(name)
    return names

def first_name(name):   
    '''
    gets the first name
    Args:
        name
    Returns:
        the first name
    '''  
    names = get_names(name)                            
    return names[0]                                       

def last_name(name):       
    '''
    gets the last name
    Args:
        name
    Returns:
        the last name
    '''  
    names = get_names(name)                           
    return names[-1]                                      

def middle_name(name):  
    '''
    gets the middle name
    Args:
        name
    Returns:
        the middle name
    '''  
    names = get_names(name)                          
    return ' '.join(names[1:-1])

def has_hyphen(name):
    '''
    says if it has a hyphen
    Args:
        name
    Returns:
        hypens
    
    '''
    return '-' in last_name(name)

def lower_case(name):  
    '''
    shows all lowercase letter
    Args:
        name
    Returns:
        lowercase letters 
    '''                               

    for letter in name:                                
        if ord(letter) > 96 and ord(letter) < 123:       
            nameout = chr(ord(letter) - 32)
        nameout += letter
    return nameout

def upper_case(name):  
    '''
    shows all uppercase letter
    Args:
        name
    Returns:
       uppercase letters 
    '''                                             
    nameout = ''
    for letter in name:                                 
        if ord(letter) > 64  and ord(letter) < 91:       
            nameout = chr(ord(letter) + 32)                     
    return nameout

def gen_random(name):
    char_list = list(name)
    random.shuffle(char_list)
    return "".join(char_list)
  
def is_palidrome (name):
    return name == name[::1]

def get_initials(name):
    '''
    ets initals of letters 
    Args:
        name
    Returns:
       uppercase letters 
       '''
    initials = ''
    names = get_names(name)

    for n in names:
        initials += n[0]

    return initials

def main():
    name = input("enter your full name: ")

    print('1.  to reverse string 2.  to count vowels   3.  to count consonant   4.  to print first name   5.  to print last name 6.  to print middle name 7.  to show hyphens if you have    8.  to show all lower case  9.  to show all upper case  10. to generate random11. to print if it is a palidrome12. to get initials')

    while True:
        choice = input("enter choice ")
        
        if choice == '1':
            output = reverse_string(name)
            print(output)
        elif choice == '2':
            output = count_vowels(name)
            print(output)
            #You can promt user for a paticular vowel or create subtotals for each
        elif choice == '3':
            output = count_consonant(name)
            print(output)
            #bonus: subtotals of each consonant
        elif choice == '4':
            output = first_name(name)
            print(output)
        elif choice == '5':
            output = last_name(name)
            print(output)
        elif choice == '6':
            output = middle_name(name)
            print(output)
        elif choice == '7':
            output = has_hyphen(name)
            print(output)
        elif choice == '8':
            output = lower_case(name)
            print(output)
        elif choice == '9':
            output = upper_case(name)
            print(output)
        elif choice == '10':
            output = gen_random(name)
            print(output)
        elif choice == '11':
            output = is_palidrome(name)
            print(output)
            #return full name as a sorted array of character(bonus)
            #BUILD A MENU
        elif choice == '12':
            output = get_initials(name)
            print(output)
            #return boolean if name containes title?distication (dr""sir""esq"phd)(bonus0)
            #COME UP WITH MY OWN
            #SECREAT ASK TEACHER 
            #DOCUMENT WHOLE THING
        else:
            print("i dont know what to do..")
main()



   
  


    
