import time
from LLBOT.studentmodel import LLBOTdb
from src import Logger

db = LLBOTdb.LLBOTdb()
conn = db.get_connection()
cursor = conn.cursor()
correctedtxt = ""
boti = ""
def start(msg,desc,rule,rep,offset,length,txt,level,lessonID, bot, message):
    print("ENTERED INDIRECT CORRECTION")
    global correctedtxt
    global boti
    boti = bot
    tbrindex= offset+length #to be replaced index
    
    tbr= txt[offset:tbrindex] #to be replaced
    correctedtxt= txt.replace(tbr,rep)

    print("=========================================================")
    print("LLBOT: I think you made a little mistake on the last sentence you sent")
    print("=========================================================")
    Logger.log_conversation("LLBOT" + ": " + "I think you made a little mistake on the last sentence you sent")
    time.sleep(1.5)
    boti.reply_to(message, "I think you made a little mistake on the last sentence you sent... \U0001F9D0")
    printLessonMessage(lessonID,level, message, boti)
    time.sleep(1.5)
    print("=========================================================")
    print("LLBOT: Go ahead and try to send your last sentence again, this time following the rules!")
    print("=========================================================")
    Logger.log_conversation("LLBOT" + ": " + "Go ahead and try to send your last sentence again, this time following the rules!")
    # boti.reply_to(message, "Go ahead and try to send your last sentence again, this time following the rules! :D")
    # userattempt= input()
    # Logger.log_conversation("User" + ": " + userattempt)

    msg = boti.reply_to(message, "Go ahead and try to send your last sentence again, this time following the rules! \U0001F913")
    boti.register_next_step_handler(msg, process_IC)
    # userattempt= clean(userattempt)

def process_IC (message):
    global correctedtxt
    userattempt = clean(message.text)
    Logger.log_conversation("USER" + ": " + userattempt)
    if userattempt == correctedtxt:
        print("=========================================================")
        print("LLBOT: That's correct!")
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "That's correct!")
        boti.reply_to(message, "That's correct! \U0001F604 \U0001F44D")
        time.sleep(1.5)
        print("=========================================================")
        print("LLBOT: The what happens?")
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "Then what happens next?")
        boti.reply_to(message, "Then what happens next?")
    elif userattempt != correctedtxt:
        print("=========================================================")
        print("LLBOT: Not quite, but that's okay!")
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "Not quite, but that's okay!")
        boti.reply_to(message, "Not quite, but that's okay!")
        time.sleep(1.5)
        print("=========================================================")
        print("LLBOT: I think you meant: " + correctedtxt)
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "I think you meant:"+correctedtxt)
        boti.reply_to(message, "I think you meant: " + correctedtxt)
        time.sleep(1.5)
        print("=========================================================")
        print("LLBOT: What happens after that?")
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "What happens after that?")
        boti.reply_to(message, "What happens after that?")


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
def printLessonMessage(lessonID, level, message, boti):
        lesson=""
        if lessonID==1:
            lesson= "Subject Verb Agreement"
        elif lessonID==2:
            lesson= "Order of Adjectives"
        elif lessonID==3:
            lesson= "Degree of Adjectives"
        print("THS IS LESSON ID:" + str(lessonID))
        sql = "SELECT dialogue_template FROM lessonresponse WHERE resp_type = %s and lessonID= %s"
        cursor.execute(sql,["ind_cor",lessonID])
        res = cursor.fetchall()
        res=[i[0] for i in res]
        resp1= res[0]
        resp2 = res[1]
        print(level)
        if level=="Beginner":
            print("=========================================================")
            print("LLBOT: Remember,"+ " "+ resp1)
            print("=========================================================")
            Logger.log_conversation("LLBOT" + ": " + "Remember, "+resp1)
            boti.reply_to(message, "Remember,"+ " "+ resp1 + " \U0001F60A")
            time.sleep(1.5)
            print("=========================================================")
            print("LLBOT:" + " "+ resp2)
            print("=========================================================")
            Logger.log_conversation("LLBOT" + ": " + resp2)
            boti.reply_to(message, resp2)
        elif level=="Intermediate":
            print("=========================================================")
            print("LLBOT: Remember,"+ " "+ resp2)
            print("=========================================================")
            Logger.log_conversation("LLBOT" + ": " + "Remember, "+ resp2)
            boti.reply_to(message, "Remember,"+ " "+ resp2)
        elif level=="Expert":
            print("=========================================================")
            print("LLBOT: Remember the rules of "+ lesson )
            print("=========================================================")
            Logger.log_conversation("LLBOT" + ": " + "Remember the rules of "+ lesson)
            boti.reply_to(message, "Remember the rules of "+ lesson + " \uE10F")



        

