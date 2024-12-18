import random

score = 0
options = ['1','2','3','4','5','6','7','8','10']
while True:
    user_guess = input("Pick a number 1-10!")
    computer = random.choice(options)
    print(f"user chose{user_guess},but chose {computer}")
    if(f"{user_guess} chose same number as {computer}"):
        print ("you win!")
    if(f"{user_guess} doesnt chose same number as {computer}"):
        print ("you loose!")
