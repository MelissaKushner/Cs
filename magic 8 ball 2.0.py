import random                                                                                                                                  #import random

responses = ['yes','no','never','maybe','you wish','never in a million years','ofc','yes yeS yES YES!','invalid','unclear','uncomprehendable'] #make a list a responses 
question_words = ['why','what','will','when','who']                                                                                            #Words with questions


while True:                                                                                                                                    #forever loop
    question = input("Ask a question: ")                                                                                                       #ask a question
    first_words = question.split()[0]                                                                                                          #what are some of the first words                                        
    
    if question == "exit":                                                                                                                     #if they write exit
        print("good bye!")                                                                                                                     #bye
        break                                                                                                                                  #else
    elif "?" in question or first_words in question_words:                                                                                     #if ? is in one of the list
        print(random.choice(responses))                                                                                                        #print a random response from the list responses
    else:                                                                                                                                      #break
        print("invalid")                                                                                                                       #invalid repsonse

    
    


    
