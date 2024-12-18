import time                                                                #Iimporttime

while True:                                                                #if true 
    snooze = input("Your alarm went off! Snooze? y/n: ").lower()           #tell your alarm went off
    
    if snooze == "y":                                                      #if snooze is yes
        print("Sleep for 5 more minutes")                                  #sleep for five more min
        time.sleep(2)                                                      #show what snooze
    elif snooze == "n":                                                    #if snooze is no
        break                                                              #esle
    else:                                                                  #else
        print("Invalid")                                                   #invalid response
 
while True:                                                                #if true
    brushteeth = input ("Do you want to brush your teeth? y/n: ").lower()  #Do you want to brush your teeth

    if brushteeth == "n":                                                  #if brush teeth is no
        print("ew")                                                        #show ew 
        break                                                              #if brush teeth is yes 
    elif brushteeth == "y":                                                #if brush teeth is yes 
        time.sleep(2)                                                      #show sleep snooze again 
        print("You brushed your teeth!")                                   #show you brushed your teeth
        break                                                              #break
    else:
        print("Invalid response")                                          #show invalid response

while True:                                                                #if true
    comfy = input("Do you want to dress comfy? y/n: ").lower()             #do you want to dress comfy?

    if comfy == "y":                                                       #if yes
        print("put baggy clothes on")                                      #put baggy clothes 
        break                                                              #break
    elif comfy == "n":                                                     #if no
        print("put on nice clothes")                                       #put on nice clothes
        break                                                              #break
    else:                                                                  #else
        print("Invalid response")                                          #show invalid response
time.sleep(2)                                                              #show sleep
print("its time to leave the house now are you ready")                     #show its time to leave the house
print("leave for school. Goodbye!")                                        #leave for school goodbye

while True:                                                                #while true
    car = input ("Do you want to take a car?")                             #do you want to takethe car 
 
    if car = "y":                                                          #if yes 
        print=("get in the car")                                           #get in car
        break                                                              #break
    elif car= "n":                                                         #if no
        print("walk to bus")                                               #walk to the bus
        
