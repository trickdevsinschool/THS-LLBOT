import time
from LLBOT.fos import replyTransform
from src import Logger


def start(msg,desc,rule,rep,offset,length,txt,bot,message):
    print("ENTERED DIRECT CORRECTION")
    tbrindex= offset+length #to be replaced index
    
    tbr= txt[offset:tbrindex] #to be replaced
    correctedtxt= txt.replace(tbr,rep)

    initialReply= "I see, so "+ correctedtxt.lower()
    finalReply= replyTransform.call(initialReply) #consult FOS
    #template
    print("=========================================================")
    print("LLBOT"+ ": "+ finalReply +'.') 
    print("=========================================================")
    Logger.log_conversation("LLBOT" + ": " + finalReply+ '.')
    time.sleep(1.5)
    bot.reply_to(message, finalReply +'.')
    print("=========================================================")
    print("LLBOT:What happens next?")
    print("=========================================================")
    Logger.log_conversation("LLBOT" + ": " + "What happens next?")
    bot.reply_to(message, "What happens next? \U0001F62E")



    



