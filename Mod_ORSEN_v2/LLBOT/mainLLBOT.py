from LLBOT.intro import intro_lesson
from LLBOT.studentmodel import grades
from LLBOT.studentmodel import student

studentid=""
class mainLLBOT:
    def __init__(self):
        self.studentid=""

    def start(self):
        print("=========================================================")
        print("LLBOT: Hello! I'm LLBOT. What's your name?")
        print("=========================================================")
    
        name= input()
        stud = student.student(name) #this initializes the student
        self.studentid= stud.getstudentid()
        intro= intro_lesson.intro_lesson(stud) #this sends the student information and creates an intro lesson module
        intro.startlesson() #starts the intro lesson module

    def retrieveStudentid(self):
        return self.studentid