import time
from LLBOT.studentmodel import LLBOTdb
from src import Logger
import random


db = LLBOTdb.LLBOTdb()
conn = db.get_connection()
cursor = conn.cursor()
correctedtxt = ""
correctedtxt2=""
boti = ""
def start(msg,desc,rule,rep,offset,length,txt,level,lessonID, bot, message,indices):
    print("ENTERED INDIRECT CORRECTION")
    global correctedtxt
    global correctedtxt2 #for OOA commas
    global boti
    boti = bot
    tbrindex= offset+length #to be replaced index
    
    tbr= txt[offset:tbrindex] #to be replaced
    correctedtxt= txt.replace(tbr,rep)
    
    if rule== "EN_ADJ_ORDER":
        temp= list(txt)
        for i, j in indices:
            temp.insert(i + j, ',')
        correctedtxt2.join('temp')


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
    if rule=="EN_ADJ_ORDER":
        msg = boti.reply_to(message, "Go ahead and try to send your last sentence again, this time following the rules! \U0001F913")
        boti.register_next_step_handler(msg, process_IC_OOA)
    else:
        msg = boti.reply_to(message, "Go ahead and try to send your last sentence again, this time following the rules! \U0001F913")
        boti.register_next_step_handler(msg, process_IC)
    # userattempt= clean(userattempt)

def process_IC (message):
    global correctedtxt
    stickerint=random.randint(1, 4)
    if stickerint==1:
        sti = 'CAACAgIAAxkBAAECvXxhFo39rK13ZKoQVwjbw_6IQxby0gACEwADwDZPE6qzh_d_OMqlIAQ'#cherry wave
    elif stickerint==2:
        sti= 'CAACAgIAAxkBAAECvXZhFo258K93I6fcZnuOAc2gqjzhSQACNQADrWW8FPWlcVzFMOXgIAQ' #pupper
    elif stickerint==3:
        sti= 'CAACAgIAAxkBAAECvXphFo3rnG2UlnkOoEcdwKe59G9G6AACUwIAAladvQq9xYpEKcd7QyAE' #goldy
    elif stickerint==4:
        sti= 'CAACAgIAAxkBAAECvYRhFo-ZpozaIc0NrCVJAiyWMnEdOgACIwIAAladvQo231NYTgl1JyAE' #panda-emic
    userattempt = clean(message.text)
    Logger.log_conversation("USER" + ": " + userattempt)
    if userattempt == correctedtxt:
        print("=========================================================")
        print("LLBOT: That's correct!")
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "That's correct!")
        boti.reply_to(message, "That's correct!")
        boti.send_sticker(message.chat.id, sti)
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

def process_IC_OOA (message):
    global correctedtxt
    global correctedtxt2
    userattempt = clean(message.text)
    Logger.log_conversation("USER" + ": " + userattempt)
    stickerint=random.randint(1, 4)
    if stickerint==1:
        sti = 'CAACAgIAAxkBAAECvXxhFo39rK13ZKoQVwjbw_6IQxby0gACEwADwDZPE6qzh_d_OMqlIAQ'#cherry wave
    elif stickerint==2:
        sti= 'CAACAgIAAxkBAAECvXZhFo258K93I6fcZnuOAc2gqjzhSQACNQADrWW8FPWlcVzFMOXgIAQ' #pupper
    elif stickerint==3:
        sti= 'CAACAgIAAxkBAAECvXphFo3rnG2UlnkOoEcdwKe59G9G6AACUwIAAladvQq9xYpEKcd7QyAE' #goldy
    elif stickerint==4:
        sti= 'CAACAgIAAxkBAAECvYRhFo-ZpozaIc0NrCVJAiyWMnEdOgACIwIAAladvQo231NYTgl1JyAE' #panda-emic
    if userattempt == correctedtxt or userattempt==correctedtxt2:
        print("=========================================================")
        print("LLBOT: That's correct!")
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "That's correct!")
        boti.reply_to(message, "That's correct!")
        boti.send_sticker(message.chat.id, sti)
        time.sleep(1.5)
        print("=========================================================")
        print("LLBOT: The what happens?")
        print("=========================================================")
        Logger.log_conversation("LLBOT" + ": " + "Then what happens next?")
        boti.reply_to(message, "Then what happens next?")
    elif userattempt != correctedtxt or userattempt!=correctedtxt2:
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
            time.sleep(2)
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



        

