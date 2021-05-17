import time
from LLBOT.fos import replyTransform



def start(msg,desc,rule,rep,offset,length,txt):
    print("ENTERED DIRECT CORRECTION")
    tbrindex= offset+length #to be replaced index
    
    tbr= txt[offset:tbrindex] #to be replaced
    correctedtxt= txt.replace(tbr,rep)

    initialReply= "LLBOT: I see, so "+ correctedtxt.lower()
    finalReply= replyTransform.call(initialReply) #consult FOS
    #template
    print("=========================================================")
    print(finalReply+'.') 
    print("=========================================================")
    time.sleep(1.5)
    print("=========================================================")
    print("LLBOT:What happens next?")
    print("=========================================================")
    



