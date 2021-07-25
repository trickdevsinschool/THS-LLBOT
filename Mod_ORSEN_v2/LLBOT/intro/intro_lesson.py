import time
from LLBOT.studentmodel import LLBOTdb
from src import Logger
import telebot
from telebot import types

TOKEN = "1906492501:AAF_Ayf_23luAcVLIrahfMEpSIOKP2VcMxM"
#TOKEN = "1817683801:AAGHVOy3MWNaJBwIcqEt_deRa87sM0tm4jw"
bot = telebot.TeleBot(TOKEN)

db = LLBOTdb.LLBOTdb()
conn = db.get_connection()
cursor = conn.cursor()
secs= 1.5

class intro_lesson():
    studentname=" "
    stud= ""
    studID=" "
    firstsession=""
    bot=""


    def __init__(self,student, t_f,bot): #initializes everything
        self.stud= student
        self.studID= student.getstudentid()
        self.lesson= student.grades.getcurr_lesson(self.studID)
        self.firstsession= t_f
        self.studentname= self.stud.getstudentname()
        self.bot=bot
    def startlesson(self,message):
        startINTRO(message,self.studentname,self.firstsession,self.studID,self.stud,self.bot)
        
def initwelcome(studentname): #makes the opening statement with the name
    welcome_line= "Hello " + studentname + " nice to meet you!"
    return welcome_line
    
def startINTRO(message,studentname,firstsession,studID,stud,bot):
    global secs
    if firstsession == True:
        welcome_line = initwelcome(studentname)
        print(welcome_line)
        bot.reply_to(message, welcome_line)
        Logger.log_conversation("LLBOT" + ": " + welcome_line)
        time.sleep(secs)
        print("I'm LLBOT!")
        bot.reply_to(message, 'I am LLBOT!')
        Logger.log_conversation("LLBOT" + ": " + "I'm LLBOT!")
        time.sleep(secs)
        if stud.grades.getcurr_lesson(studID) == 1:  # checks if curr lesson of the student is SVA
            sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
            cursor.execute(sql, ["SVA", "GEN"])
            res = cursor.fetchall()
            res = [i[0] for i in res]
            SVAexamples = []
            for i in range(8, 19, 1):
                SVAexamples.append(res[i])
            print("=========================================================")
            print("LLBOT: Before we start, I have to ask. Are you familiar with the Subject Verb Agreement?")
            print("=========================================================")
            Logger.log_conversation("LLBOT" + ": " + "Before we start, I have to ask. Are you familiar with the Subject Verb Agreement?")
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Yes', 'No', 'A little bit')
            msg = bot.reply_to(message, 'Before we start, I have to ask. Are you familiar with the Subject Verb Agreement?',reply_markup=markup)
            bot.register_next_step_handler(msg, process_SVA)
            

        elif stud.grades.getcurr_lesson(studID) == 2:
            sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
            cursor.execute(sql, ["OOA", "GEN"])
            res = cursor.fetchall()
            res = [i[0] for i in res]
            OOAexamples = []
            for i in range(8, 13, 1):
                OOAexamples.append(res[i])
            print("=========================================================")
            print("LLBOT: Before we start, I have to ask. Are you familiar with the Order of Adjectives?")
            print("=========================================================")
            Logger.log_conversation("LLBOT" + ": " + "Before we start, I have to ask. Are you familiar with the Order of Adjectives?")
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Yes', 'No', 'A little bit')
            msg = bot.reply_to(message, 'Before we start, I have to ask. Are you familiar with the Order of Adjectives?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_OOA)
        
        elif stud.grades.getcurr_lesson(studID) == 3:
            sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
            cursor.execute(sql, ["DOA", "GEN"])
            res = cursor.fetchall()
            res = [i[0] for i in res]
            DOAexamples = []
            for i in range(8, 13, 1):
                DOAexamples.append(res[i])
            print("=========================================================")
            print("LLBOT: Before we start, I have to ask. Are you familiar with the Degree of Adjectives?")
            print("=========================================================")
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Yes', 'No', 'A little bit')
            msg = bot.reply_to(message, 'Before we start, I have to ask. Are you familiar with the Degree of Adjectives?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_OOA)



def process_SVA(message):
    print('ENTERED PROCESS SVA')
    user_reply=message.text
    Logger.log_conversation("User:" + user_reply)
    sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
    cursor.execute(sql, ["SVA", "GEN"])
    res = cursor.fetchall()
    res = [i[0] for i in res]
    SVAexamples = []
    for i in range(8, 19, 1):
        SVAexamples.append(res[i])
    teach = True
    if user_reply == "yes" or user_reply == "Yes":
        print("=========================================================")
        print("LLBOT: " + res[0])
        print(res[7])
        print("=========================================================")
        bot.reply_to(message,res[0])
        bot.reply_to(message,res[7])
        Logger.log_conversation("LLBOT" + ": " + res[0])
        Logger.log_conversation("LLBOT" + ": " + res[7])
        time.sleep(secs)
        teach = False
    elif user_reply == "No" or user_reply == "no":
        i = 0
        print("=========================================================")
        print("LLBOT: " + res[1])
        print("\n" + res[3])
        print("\n" + res[4])
        print("\n" + res[5])
        print("\n" + res[6])
        print("=========================================================")
        bot.reply_to(message,res[1])
        bot.reply_to(message,res[3])
        bot.reply_to(message,res[4])
        bot.reply_to(message,res[5])
        bot.reply_to(message,res[6])
        Logger.log_conversation("LLBOT" + ": " + res[1])
        Logger.log_conversation("LLBOT" + ": " + res[3])
        Logger.log_conversation("LLBOT" + ": " + res[4])
        Logger.log_conversation("LLBOT" + ": " + res[4])
        Logger.log_conversation("LLBOT" + ": " + res[6])
        time.sleep(secs)
        print("\nNow that the terms are clear,\n" + res[7])
        bot.reply_to(message,"Now that the terms are clear...")
        bot.reply_to(message,res[7])
        Logger.log_conversation("LLBOT" + ": " + "Now that the terms are clear"+res[7])
        print("\n" + SVAexamples[i] + "\n")
        bot.reply_to(message,SVAexamples[i])
        Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
        i = i + 1
        print(SVAexamples[i])
        bot.reply_to(message,SVAexamples[i])
        Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
        bot.reply_to(message,SVAexamples[i])
        i = 2
        print("=========================================================")
        time.sleep(secs)
    elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    bot.reply_to(message,res[2])
                    bot.reply_to(message,res[7])
                    Logger.log_conversation("LLBOT" + ": " + res[2])
                    Logger.log_conversation("LLBOT" + ": " + res[7])
                    time.sleep(secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + SVAexamples[i])
                    print("=========================================================")
                    bot.reply_to(message,'For example:')
                    bot.reply_to(message,SVAexamples[i])
                    #Logger.log_conversation("LLBOT" + ": " + "For example...")
                    Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
                    time.sleep(secs)
    print("=========================================================")
    print("LLBOT: Now let's make a story to test this new lesson out!")
    bot.reply_to(message,'Now let us make a story to test this new lesson out!')
    Logger.log_conversation("LLBOT" + ": " + "Now let's make a story to test this new lesson out!")
    print("LLBOT: Try to start your first story by telling me what a character is doing!")
    bot.reply_to(message,'Try to start your first story by telling me what a character is doing!')
    Logger.log_conversation("LLBOT" + ": " + "Try to start your first story by telling me what a character is doing!")
    print("LLBOT: For example: The king sings a song")
    bot.reply_to(message,'For example: The king sings a song')
    Logger.log_conversation("LLBOT" + ": " + "For example: The king sings a song")
    print("LLBOT:Go ahead! You try!")
    Logger.log_conversation("LLBOT" + ": " + "Go ahead! You try!")
    bot.reply_to(message,'Go ahead! You try!')
    print("=========================================================")
    

def process_OOA(message):
    user_reply=message.text
    Logger.log_conversation("User:" + user_reply)
    sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
    cursor.execute(sql, ["OOA", "GEN"])
    res = cursor.fetchall()
    res = [i[0] for i in res]
    OOAexamples = []
    for i in range(8, 13, 1):
        OOAexamples.append(res[i])
    teach = True
    if user_reply == "yes" or user_reply == "Yes":
        print("=========================================================")
        print("LLBOT: " + res[0])
        print(res[7])
        print("=========================================================")
        bot.reply_to(message,res[0])
        bot.reply_to(message,res[7])
        Logger.log_conversation("LLBOT" + ": " + res[0])
        Logger.log_conversation("LLBOT" + ": " + res[7])
        time.sleep(secs)
        teach = False
    elif user_reply == "No" or user_reply == "no":
        i = 0
        print("=========================================================")
        print("LLBOT: " + res[1])
        print("\n" + res[3])
        print("\n" + res[4])
        print("\n" + res[5])
        print("\n" + res[6])
        print("=========================================================")
        bot.reply_to(message,res[1])
        bot.reply_to(message,res[3])
        bot.reply_to(message,res[4])
        bot.reply_to(message,res[5])
        bot.reply_to(message,res[6])
        Logger.log_conversation("LLBOT" + ": " + res[1])
        Logger.log_conversation("LLBOT" + ": " + res[3])
        Logger.log_conversation("LLBOT" + ": " + res[4])
        Logger.log_conversation("LLBOT" + ": " + res[4])
        Logger.log_conversation("LLBOT" + ": " + res[6])
        time.sleep(secs)
        print("\nNow that the terms are clear,\n" + res[7])
        bot.reply_to(message,"Now that the terms are clear...")
        bot.reply_to(message,res[7])
        Logger.log_conversation("LLBOT" + ": " + "Now that the terms are clear"+res[7])
        print("\n" + OOAexamples[i] + "\n")
        bot.reply_to(message,OOAexamples[i])
        Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
        i = i + 1
        print(OOAexamples[i])
        bot.reply_to(message,OOAexamples[i])
        Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
        bot.reply_to(message,OOAexamples[i])
        i = 2
        print("=========================================================")
        time.sleep(secs)
    elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    bot.reply_to(message,res[2])
                    bot.reply_to(message,res[7])
                    Logger.log_conversation("LLBOT" + ": " + res[2])
                    Logger.log_conversation("LLBOT" + ": " + res[7])
                    time.sleep(secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + OOAexamples[i])
                    print("=========================================================")
                    bot.reply_to(message,'For example:')
                    bot.reply_to(message,OOAexamples[i])
                    #Logger.log_conversation("LLBOT" + ": " + "For example...")
                    Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
                    time.sleep(secs)
    print("=========================================================")
    print("LLBOT: Now let's make a story to test this new lesson out!")
    bot.reply_to(message,'Now let us make a story to test this new lesson out!')
    Logger.log_conversation("LLBOT" + ": " + "Now let's make a story to test this new lesson out!")
    print("LLBOT: Try to describe your character this time!")
    bot.reply_to(message,'Try to describe your character this time!')
    Logger.log_conversation("LLBOT" + ": " + "Try to describe your character this time!")
    print("LLBOT: For example: The big, brown, happy bear is sleeping")
    bot.reply_to(message,'For example: The big, brown, happy bear is sleeping')
    Logger.log_conversation("LLBOT" + ": " + "For example: The big, brown, happy bear is sleeping")
    print("LLBOT:Go ahead! You try!")
    Logger.log_conversation("LLBOT" + ": " + "Go ahead! You try!")
    bot.reply_to(message,'Go ahead! You try!')
    print("=========================================================")

def process_DOA(message):
    user_reply=message.text
    Logger.log_conversation("User:" + user_reply)
    sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
    cursor.execute(sql, ["DOA", "GEN"])
    res = cursor.fetchall()
    res = [i[0] for i in res]
    DOAexamples = []
    for i in range(8, 13, 1):
        DOAexamples.append(res[i])
    teach = True
    if user_reply == "yes" or user_reply == "Yes":
        print("=========================================================")
        print("LLBOT: " + res[0])
        print(res[7])
        print("=========================================================")
        bot.reply_to(message,res[0])
        bot.reply_to(message,res[7])
        Logger.log_conversation("LLBOT" + ": " + res[0])
        Logger.log_conversation("LLBOT" + ": " + res[7])
        time.sleep(secs)
        teach = False
    elif user_reply == "No" or user_reply == "no":
        i = 0
        print("=========================================================")
        print("LLBOT: " + res[1])
        print("\n" + res[3])
        print("\n" + res[4])
        print("\n" + res[5])
        print("\n" + res[6])
        print("=========================================================")
        bot.reply_to(message,res[1])
        bot.reply_to(message,res[3])
        bot.reply_to(message,res[4])
        bot.reply_to(message,res[5])
        bot.reply_to(message,res[6])
        Logger.log_conversation("LLBOT" + ": " + res[1])
        Logger.log_conversation("LLBOT" + ": " + res[3])
        Logger.log_conversation("LLBOT" + ": " + res[4])
        Logger.log_conversation("LLBOT" + ": " + res[4])
        Logger.log_conversation("LLBOT" + ": " + res[6])
        time.sleep(secs)
        print("\nNow that the terms are clear,\n" + res[7])
        bot.reply_to(message,"Now that the terms are clear...")
        bot.reply_to(message,res[7])
        Logger.log_conversation("LLBOT" + ": " + "Now that the terms are clear"+res[7])
        print("\n" + DOAexamples[i] + "\n")
        bot.reply_to(message,DOAexamples[i])
        Logger.log_conversation("LLBOT" + ": " + DOAexamples[i])
        i = i + 1
        print(DOAexamples[i])
        bot.reply_to(message,DOAexamples[i])
        Logger.log_conversation("LLBOT" + ": " + DOAexamples[i])
        bot.reply_to(message,DOAexamples[i])
        i = 2
        print("=========================================================")
        time.sleep(secs)
    elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    bot.reply_to(message,res[2])
                    bot.reply_to(message,res[7])
                    Logger.log_conversation("LLBOT" + ": " + res[2])
                    Logger.log_conversation("LLBOT" + ": " + res[7])
                    time.sleep(secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + DOAexamples[i])
                    print("=========================================================")
                    bot.reply_to(message,'For example:')
                    bot.reply_to(message,DOAexamples[i])
                    #Logger.log_conversation("LLBOT" + ": " + "For example...")
                    Logger.log_conversation("LLBOT" + ": " + DOAexamples[i])
                    time.sleep(secs)
    print("=========================================================")
    print("LLBOT: Now let's make a story to test this new lesson out!")
    bot.reply_to(message,'Now let us make a story to test this new lesson out!')
    Logger.log_conversation("LLBOT" + ": " + "Now let's make a story to test this new lesson out!")
    print("LLBOT: Try to compare 2 characters first this time!")
    bot.reply_to(message,'Try to compare 2 characters first this time!')
    Logger.log_conversation("LLBOT" + ": " + "Try to compare 2 characters first this time!")
    print("LLBOT: For example: Timmy is bigger than Joey")
    bot.reply_to(message,'For example: Timmy is bigger than Joey')
    Logger.log_conversation("LLBOT" + ": " + "For example: Timmy is bigger than Joey")
    print("LLBOT:Go ahead! You try!")
    Logger.log_conversation("LLBOT" + ": " + "Go ahead! You try!")
    bot.reply_to(message,'Go ahead! You try!')
    print("=========================================================")         
            
#bot.enable_save_next_step_handlers(delay=2)
#bot.load_next_step_handlers()
