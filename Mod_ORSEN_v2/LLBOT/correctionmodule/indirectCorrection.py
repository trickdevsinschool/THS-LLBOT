import time

def start(msg,desc,rule,rep,offset,length,txt):
    print("ENTERED INDIRECT CORRECTION")
    tbrindex= offset+length #to be replaced index
    
    tbr= txt[offset:tbrindex] #to be replaced
    correctedtxt= txt.replace(tbr,rep)

    print("=========================================================")
    print("LLBOT: I think you made a little mistake on the last sentence you sent")
    print("=========================================================")
    time.sleep(1.5)
    print("=========================================================")
    print("LLBOT: Remember <Lesson reminder depending on level")
    print("=========================================================")
    time.sleep(1.5)
    print("=========================================================")
    print("LLBOT: Go ahead and try to send your last sentence again, this time following <Topic> :D")
    print("=========================================================")
    userattempt= input()
    userattempt= clean(userattempt)
    if userattempt == correctedtxt:
        print("=========================================================")
        print("LLBOT: That's correct, <Student Name>!")
        print("=========================================================")
        time.sleep(1.5)
        print("=========================================================")
        print("LLBOT: The what happens?")
        print("=========================================================")
    elif userattempt != correctedtxt:
        print("=========================================================")
        print("LLBOT: Not quite, but that's okay!")
        print("=========================================================")
        time.sleep(1.5)
        print("=========================================================")
        print("LLBOT: I think you meant: " + correctedtxt)
        print("=========================================================")
        time.sleep(1.5)
        print("=========================================================")
        print("LLBOT: What happens after that?")
        print("=========================================================")


def clean(response):
    #Tweaked for capitalization
    response = response.strip()
    if response.endswith(".") == False:
        response = response + "."
    if response== "the end.":
        return response
    else: 
        first_word= response.split()[0]
        first_word=first_word.capitalize()

        #print(first_word)

        response= response.replace(response.split()[0],first_word,1)

        return response


