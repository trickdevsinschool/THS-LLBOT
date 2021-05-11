import time



def start(msg,desc,rule,rep,offset,length,txt):
    print("ENTERED DIRECT CORRECTION")
    tbrindex= offset+length #to be replaced index
    
    tbr= txt[offset:tbrindex] #to be replaced
    correctedtxt= txt.replace(tbr,rep)

    #template
    print("=========================================================")
    print("LLBOT: I see, so " + correctedtxt.lower()) #to be fetched dia templates in DB
    print("=========================================================")
    time.sleep(1.5)
    print("=========================================================")
    print("LLBOT:What happens next?")
    print("=========================================================")
    #checkFOS(finalstring)



