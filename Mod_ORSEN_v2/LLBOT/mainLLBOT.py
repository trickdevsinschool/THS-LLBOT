from LLBOT.intro import intro_lesson
from LLBOT.studentmodel import grades
from LLBOT.studentmodel import student
from src import Logger
import telebot
#TELEGRAM NEEDS 
TOKEN = "1912486706:AAHjPKksAyDkR-yWJELHeGtfUJ9XYG86vms"
bot = telebot.TeleBot(TOKEN)
studentid=""

def process_yes_or_no_step(message):
    try:
        #chat_id = message.chat.id
        y_or_n = message.text
        
        if(y_or_n== 'n' or y_or_n == 'N' or y_or_n == 'No' or y_or_n == 'no' ):
            print("=========================================================")
            print("LLBOT: What is your Student number?")
            print("=========================================================")
            Logger.log_conversation("LLBOT: What is your Student number?")
            msg= bot.reply_to(message, "What is your Student number?")
            bot.register_next_step_handler(msg, process_student_number)
        elif(y_or_n=='y' or y_or_n == 'Y' or y_or_n == 'Yes' or y_or_n == 'yes' ):
            print("=========================================================")
            print("LLBOT: What is your Student number?")
            print("=========================================================")
            Logger.log_conversation("LLBOT: What is your name?")
            msg= bot.reply_to(message, "What is your name?")
            bot.register_next_step_handler(msg, process_student_name)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_student_number(message):
        try:
            chat_id = message.chat.id
            studnum = message.text
            if not studnum.isdigit():
                msg = bot.reply_to(message, 'You should enter a number. What is your student number?')
                bot.register_next_step_handler(msg, process_student_number)
                return
            Logger.log_conversation("User: "+ studnum)
            stud = student.student('n', studnum)
            studentid = stud.getstudentid()
            intro= intro_lesson.intro_lesson(stud, True) ## MUST BE SET TO FALSE FOR NON NEW STUDENT GREETING
            intro.startlesson()
        except Exception as e:
            bot.reply_to(message, 'oooops')

def process_student_name(message):
        try:
            chat_id = message.chat.id
            studname = message.text
            stud = student.student('y', studname)
            studentid = stud.getstudentid()
            intro= intro_lesson.intro_lesson(stud, True)
            intro.startlesson()
        except Exception as e:
            bot.reply_to(message, 'oooops')

def start(message):
        print("=========================================================")
        print("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        print("=========================================================")
        Logger.log_conversation("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        msg= bot.reply_to(message, "Hello! I'm LLBOT. Is this your first time? Y/N")
        
        bot.register_next_step_handler(msg, process_yes_or_no_step)
        

class mainLLBOT:
    def __init__(self):
        self.studentid=""
    
    def mainstart(self,message):
        start(message)


    

        #if(yon == 'n' or yon == 'N'):
            #print("=========================================================")
            #print("LLBOT: What is your Student number?")
            #print("=========================================================")
            #Logger.log_conversation("LLBOT: What is your Student number?")
            #id = input()
            #Logger.log_conversation("User: "+id)
            #stud = student.student(yon, id)
            #self.studentid = stud.getstudentid()
            #intro= intro_lesson.intro_lesson(stud, True) ## MUST BE SET TO FALSE FOR NON NEW STUDENT GREETING
            #intro.startlesson()
        #elif(yon =='y' or yon == 'Y'):
            #print("=========================================================")
            #print("LLBOT: What is your name?")
            #print("=========================================================")
            #Logger.log_conversation("LLBOT: What is your name?")
            #name = input()
            #Logger.log_conversation("User: "+name)
            #stud = student.student(yon, name)
            #self.studentid = stud.getstudentid()
            #intro= intro_lesson.intro_lesson(stud, True)
            #intro.startlesson()
        #else:
            #print("=========================================================")
            #print("LLBOT: Please Try Again!")
            #print("=========================================================")
            #Logger.log_conversation("LLBOT: Please Try Again!")
            #self.start()

    def retrieveStudentid(self):
        return self.studentid

    


    

    
