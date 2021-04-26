#get, set, update students here
from LLBOT.studentmodel import grades

class student():
    studentname=""
    studentid=""
    def __init__(self):
        #TO Broqz: these should be SQL fetches thanks! -Trick
        studentname="Charlie"
        studentid="1234"
        self.grades= grades.grades(studentid)

        
        
    #Additional methods below
    def getstudentname(self):
        return self.studentname