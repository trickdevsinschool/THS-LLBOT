from LLBOT.intro import intro_lesson
from LLBOT.studentmodel import grades
from LLBOT.studentmodel import student
from src import Logger

studentid=""
class mainLLBOT:
    def __init__(self):
        self.studentid=""

    def start(self):
        print("=========================================================")
        print("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        print("=========================================================")
        Logger.log_conversation("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")

        yon = input()
        Logger.log_conversation("User: "+yon)

        if(yon == 'n' or yon == 'N'):
            print("=========================================================")
            print("LLBOT: What is your Student number?")
            print("=========================================================")
            Logger.log_conversation("LLBOT: What is your Student number?")
            id = input()
            Logger.log_conversation("User: "+id)
            stud = student.student(yon, id)
            self.studentid = stud.getstudentid()
            intro= intro_lesson.intro_lesson(stud, True) ## MUST BE SET TO FALSE FOR NON NEW STUDENT GREETING
            intro.startlesson()
        elif(yon =='y' or yon == 'Y'):
            print("=========================================================")
            print("LLBOT: What is your name?")
            print("=========================================================")
            Logger.log_conversation("LLBOT: What is your name?")
            name = input()
            Logger.log_conversation("User: "+name)
            stud = student.student(yon, name)
            self.studentid = stud.getstudentid()
            intro= intro_lesson.intro_lesson(stud, True)
            intro.startlesson()
        else:
            print("=========================================================")
            print("LLBOT: Please Try Again!")
            print("=========================================================")
            Logger.log_conversation("LLBOT: Please Try Again!")
            self.start()

    def retrieveStudentid(self):
        return self.studentid
