from LLBOT.intro import intro_lesson
from LLBOT.studentmodel import grades
from LLBOT.studentmodel import student

studentid=""
class mainLLBOT:
    def __init__(self):
        self.studentid=""

    def start(self):
        print("=========================================================")
        print("LLBOT: Hello! I'm LLBOT. Is this your first time? Y/N")
        print("=========================================================")

        yon = input()

        if(yon == 'n' or yon == 'N'):
            print("=========================================================")
            print("LLBOT: What is your Student number?")
            print("=========================================================")
            id = input()
            stud = student.student(yon, id)
            self.studentid = stud.getstudentid()
            intro= intro_lesson.intro_lesson(stud, True) ## MUST BE SET TO FALSE FOR NON NEW STUDENT GREETING
            intro.startlesson()
        elif(yon =='y' or yon == 'Y'):
            print("=========================================================")
            print("LLBOT: Hello! What is your name?")
            print("=========================================================")
            name = input()
            stud = student.student(yon, name)
            self.studentid = stud.getstudentid()
            intro= intro_lesson.intro_lesson(stud, True)
            intro.startlesson()
        else:
            print("=========================================================")
            print("LLBOT: Please Try Again!")
            print("=========================================================")
            self.start()

    def retrieveStudentid(self):
        return self.studentid
