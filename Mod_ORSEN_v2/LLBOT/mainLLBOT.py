from LLBOT.intro import intro_lesson
from LLBOT.studentmodel import grades
from LLBOT.studentmodel import student
from src import Logger
import telebot
#TELEGRAM NEEDS 
#TOKEN = "1911425925:AAEGVXLEG7JzdiNwZ_VMzZLeRjbEZhPvlY0"
#TOKEN = "1911425925:AAEGVXLEG7JzdiNwZ_VMzZLeRjbEZhPvlY0"
#bot = telebot.TeleBot(TOKEN)
studentid=" "
boti=""
class mainLLBOT:
    studentid=""
    def __init__(self):
        self.studentid=""
        
    
    def mainstart(self,message,bot):
        self.startLLBOT(message,bot)
        
    def retrieveStudentid(self):
        print('RET STUD ID ENTER')
        print(self.studentid)
        return self.studentid
    
    def setstudentid(self,studentID):
        self.studentid = studentID
        print('SET STUDID CALLED')

#@bot.message_handler(commands=['start'])
    def startLLBOT(self,message,bot):
        global boti
        boti=bot
        print (message.text)
        print("=========================================================")
        print("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        print("=========================================================")
        Logger.log_conversation("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        msg = boti.reply_to(message, "Hello! I'm LLBOT. Is this your first time? Y/N")
        boti.register_next_step_handler(msg, self.process_yes_or_no_step)

    def process_yes_or_no_step(self,message):
        y_or_n = message.text
        print("YOU ARE IN PROCESS Y OR N")
            
        if(y_or_n == 'n' or y_or_n == 'N' or y_or_n == 'No' or y_or_n == 'no' ):
            print("=========================================================")
            print("LLBOT: What is your Student number?")
            print("=========================================================")
            Logger.log_conversation("LLBOT: What is your Student number?")
            msg = boti.reply_to(message, "What is your Student number?")
            boti.register_next_step_handler(msg, self.process_student_number)
        elif(y_or_n=='y' or y_or_n == 'Y' or y_or_n == 'Yes' or y_or_n == 'yes' ):
            print("=========================================================")
            print("LLBOT: What is your name?")
            print("=========================================================")
            Logger.log_conversation("LLBOT: What is your name?")
            msg = boti.reply_to(message, "What is your name?")
            boti.register_next_step_handler(msg, self.process_student_name)

    def process_student_number(self,message):
    # try:
        print("YOU ARE IN STUDENT NUM")
        global studentid
        chat_id = message.chat.id
        studnum = message.text
        if not studnum.isdigit():
            msg = boti.reply_to(message, 'You should enter a number. What is your student number?')
            boti.register_next_step_handler(msg, self.process_student_number)
            return
        Logger.log_conversation("User: "+ studnum)
        stud = student.student('n', studnum)
        studentid = stud.getstudentid()
        self.setstudentid(studentid)
        intro= intro_lesson.intro_lesson(stud, True,boti) ## MUST BE SET TO FALSE FOR NON NEW STUDENT GREETING
        intro.startlesson(message)
        #bot.stop_polling()
    # except Exception as e:
    #     bot.reply_to(message, 'oooops')

    def process_student_name(self,message):
    # try:
        print("YOU ARE IN PROCESS STUDENT NAME")
        global studentid
        chat_id = message.chat.id
        studname = message.text
        stud = student.student('y', studname)
        studentid = stud.getstudentid()
        print(studentid)
        self.setstudentid(studentid)
        intro = intro_lesson.intro_lesson(stud, True,boti)
        intro.startlesson(message)
    #bot.stop_polling()
# except Exception as e:
#     bot.reply_to(message, 'oooops')


#bot.enable_save_next_step_handlers(delay=1)
#bot.load_next_step_handlers()
#bot.polling()