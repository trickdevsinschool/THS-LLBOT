#get, set, update students here
from LLBOT.studentmodel import grades

class student():
    studentname=""
    studentid=""
    def __init__(self):
        #TO Broqz: these should be SQL fetches thanks! -Trick
        self.studentname="Charlie"
        self.studentid="1234"
        self.grades= grades.grades(self.studentid)#this isn't suppose to assign the student id to the grades, rather sends it to grades to find a match in the DB

        
        
    #Additional methods below
    def getstudentname(self):
        return self.studentname