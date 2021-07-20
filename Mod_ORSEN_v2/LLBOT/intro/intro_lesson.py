import time
from LLBOT.studentmodel import LLBOTdb
from src import Logger
import telebot
from telebot import types

TOKEN = "1911425925:AAEGVXLEG7JzdiNwZ_VMzZLeRjbEZhPvlY0"
#TOKEN = "1817683801:AAGHVOy3MWNaJBwIcqEt_deRa87sM0tm4jw"
bot = telebot.TeleBot(TOKEN)

db = LLBOTdb.LLBOTdb()
conn = db.get_connection()
cursor = conn.cursor()
secs= 1.5
studentname=" "
stud= ""
studID=" "
class intro_lesson():
    


    def __init__(self,student, t_f): #initializes everything
        self.stud= student
        self.studID= student.getstudentid()
        self.lesson= student.grades.getcurr_lesson(self.studID)
        self.firstsession= t_f
        self.studentname= self.stud.getstudentname()
        
    def initwelcome(self,studentname): #makes the opening statement with the name
        welcome_line= "Hello " + studentname + " nice to meet you!"
        return welcome_line
    
    def startlesson(self,message):

        if self.firstsession == True:
            welcome_line = self.initwelcome(self.studentname)
            print(welcome_line)
            bot.reply_to(message, welcome_line)
            Logger.log_conversation("LLBOT" + ": " + welcome_line)
            time.sleep(self.secs)
            print("I'm LLBOT!")
            Logger.log_conversation("LLBOT" + ": " + "I'm LLBOT!")
            time.sleep(self.secs)
            if self.stud.grades.getcurr_lesson(self.studID) == 1:  # checks if curr lesson of the student is SVA
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
                user_reply = input()
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                markup.add('Yes', 'No', 'A little bit')
                msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
                bot.register_next_step_handler(msg, process_SVA)
                Logger.log_conversation("User" + ": " + user_reply)
                teach = True
                if user_reply == "yes" or user_reply == "Yes":
                    print("=========================================================")
                    print("LLBOT: " + res[0])
                    print(res[7])
                    print("=========================================================")
                    Logger.log_conversation("LLBOT" + ": " + res[0])
                    Logger.log_conversation("LLBOT" + ": " + res[7])
                    time.sleep(self.secs)
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
                    Logger.log_conversation("LLBOT" + ": " + res[1])
                    Logger.log_conversation("LLBOT" + ": " + res[3])
                    Logger.log_conversation("LLBOT" + ": " + res[4])
                    Logger.log_conversation("LLBOT" + ": " + res[4])
                    Logger.log_conversation("LLBOT" + ": " + res[6])
                    time.sleep(self.secs)
                    print("\nNow that the terms are clear,\n" + res[7])
                    Logger.log_conversation("LLBOT" + ": " + "Now that the terms are clear"+res[7])
                    print("\n" + SVAexamples[i] + "\n")
                    Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
                    i = i + 1
                    print(SVAexamples[i])
                    Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
                    i = 2
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        Logger.log_conversation("LLBOT" + ": " + "Do you want another example?")
                        more_example = input()
                        Logger.log_conversation("User" + ": " + more_example)
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + SVAexamples[i])
                            print("=========================================================")
                            Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
                        else:
                            teach = False

                elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    Logger.log_conversation("LLBOT" + ": " + res[2])
                    Logger.log_conversation("LLBOT" + ": " + res[7])
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + SVAexamples[i])
                    print("=========================================================")
                    #Logger.log_conversation("LLBOT" + ": " + "For example...")
                    Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        Logger.log_conversation("LLBOT" + ": " + "Do you want another example?")
                        more_example = input()
                        Logger.log_conversation("User" + ": " + more_example)
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + SVAexamples[i])
                            print("=========================================================")
                            Logger.log_conversation("LLBOT" + ": " + SVAexamples[i])
                        else:
                            teach = False
            elif self.stud.grades.getcurr_lesson(self.studID) == 2:
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
                user_reply = input()
                Logger.log_conversation("User" + ": " + user_reply)
                teach = True
                if user_reply == "yes" or user_reply == "Yes":
                    print("=========================================================")
                    print("LLBOT: " + res[0])
                    print(res[7])
                    print("=========================================================")
                    Logger.log_conversation("LLBOT" + ": " + res[0])
                    Logger.log_conversation("LLBOT" + ": " + res[7])
                    time.sleep(self.secs)
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
                    Logger.log_conversation("LLBOT" + ": " + res[1])
                    Logger.log_conversation("LLBOT" + ": " + res[3])
                    Logger.log_conversation("LLBOT" + ": " + res[4])
                    Logger.log_conversation("LLBOT" + ": " + res[5])
                    Logger.log_conversation("LLBOT" + ": " + res[6])
                    time.sleep(self.secs)
                    print("\nNow that the terms are clear,\n" + res[7])
                    Logger.log_conversation("LLBOT" + ": " + "Now that the terms are clear..." + res[7])
                    print("\n" + OOAexamples[i] + "\n")
                    Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
                    i = i + 1
                    print(OOAexamples[i])
                    Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
                    i = 2
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        Logger.log_conversation("LLBOT" + ": " + "Do you want another example?")
                        more_example = input()
                        Logger.log_conversation("User" + ": " + more_example)
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + OOAexamples[i])
                            print("=========================================================")
                            Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
                        else:
                            teach = False
                elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    Logger.log_conversation("LLBOT" + ": " + res[2])
                    Logger.log_conversation("LLBOT" + ": " + res[7])
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + OOAexamples[i])
                    print("=========================================================")
                    Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        Logger.log_conversation("LLBOT" + ": " + "Do you want another example?")
                        more_example = input()
                        Logger.log_conversation("User" + ": " + more_example)
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + OOAexamples[i])
                            print("=========================================================")
                            Logger.log_conversation("LLBOT" + ": " + OOAexamples[i])
                        else:
                            teach = False
            elif self.stud.grades.getcurr_lesson(self.studID) == 3:
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
                user_reply = input()
                teach = True
                if user_reply == "yes" or user_reply == "Yes":
                    print("=========================================================")
                    print("LLBOT: " + res[0])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
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
                    time.sleep(self.secs)
                    print("\nNow that the terms are clear,\n" + res[7])
                    print("\n" + DOAexamples[i] + "\n")
                    i = i + 1
                    print(DOAexamples[i])
                    i = 2
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + DOAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False
                elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + DOAexamples[i])
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + DOAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False
            print("=========================================================")
            print("LLBOT: Now let's make a story to test this new lesson out!")
            Logger.log_conversation("LLBOT" + ": " + "Now let's make a story to test this new lesson out!")
            if self.stud.grades.getcurr_lesson(self.studID) == 1:
                print("LLBOT: Try to start your first story by telling me what a character is doing!")
                Logger.log_conversation("LLBOT" + ": " + "Try to start your first story by telling me what a character is doing!")
                print("LLBOT: For example: The king sings a song")
                Logger.log_conversation("LLBOT" + ": " + "For example: The king sings a song")
            elif self.stud.grades.getcurr_lesson(self.studID) == 2:
                print("LLBOT: Try to start your first story by describing us a character!")
                print("LLBOT: For example: The big, brown, and happy, bear likes to eat honey.")
            print("LLBOT:Go ahead! You try!")
            Logger.log_conversation("LLBOT" + ": " + "Go ahead! You try!")
            print("=========================================================")
            
            #end of intro module, should return to Driver.py and execute start_storytelling()

def process_SVA(message):
    user_reply=message.text
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
       

def process_OOA(message):
    bot.reply_to(message,"Hi! I'm Sample LLBOT. Try to make a story!")

def process_DOA(message):
    bot.reply_to(message,"Hi! I'm Sample LLBOT. Try to make a story!")         
            
    