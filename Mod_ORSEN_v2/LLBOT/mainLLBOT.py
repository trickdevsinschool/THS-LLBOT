from LLBOT.intro import intro_lesson
from LLBOT.studentmodel import grades
from LLBOT.studentmodel import student
from src import Logger
import telebot
#TELEGRAM NEEDS 
TOKEN = "1912486706:AAHjPKksAyDkR-yWJELHeGtfUJ9XYG86vms"
bot = telebot.TeleBot(TOKEN)
studentid=""


class mainLLBOT:
    def __init__(self):
        self.studentid=""
    
    def mainstart(self,message):
        start(message)
        
    def retrieveStudentid(self):
        return self.studentid

@bot.message_handler(commands=['start'])
def start(message):
        print (message.text)
        print("=========================================================")
        print("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        print("=========================================================")
        Logger.log_conversation("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        msg= bot.reply_to(message, "Hello! I'm LLBOT. Is this your first time? Y/N")
        bot.register_next_step_handler(msg, process_yes_or_no_step)


def process_yes_or_no_step(message):
    try:
        #chat_id = message.chat.id
        y_or_n = message.text
        print('IM HERE')
        
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


bot.enable_save_next_step_handlers(delay=1)
bot.load_next_step_handlers()
    

    
