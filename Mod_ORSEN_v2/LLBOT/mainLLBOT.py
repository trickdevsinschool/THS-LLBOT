from LLBOT.intro import intro_lesson
from LLBOT.studentmodel import grades
from LLBOT.studentmodel import student


def start():    
    stud= student.student()
    intro= intro_lesson.intro_lesson(stud)
    intro.startlesson()
    