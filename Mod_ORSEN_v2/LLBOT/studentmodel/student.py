#set, get, update students here
from LLBOT.studentmodel import LLBOTdb
from LLBOT.studentmodel import grades


class student():

    db = LLBOTdb.LLBOTdb()
    conn = db.get_connection()
    cursor = conn.cursor()

    def __init__(self, studentName):
        #TO Broqz: these should be SQL fetches thanks! -Trick
        self.studentname = studentName
        self.studentid = self.create_new_student(self.studentname)
        self.grades = grades.grades(self.studentid)#this isn't suppose to assign the student id to the grades, rather sends it to grades to find a match in the DB
  
    #Additional methods below
    def getstudentname(self):
        return self.studentname

    #Creates a new student returns the ID
    def create_new_student(self,studentName):
        sql = "INSERT INTO students (studentName) VALUES (%s)"
        self.cursor.execute(sql,[studentName])
        print("Current Student Count:", self.cursor.rowcount, "new student was inserted.")
        self.conn.commit()

        return self.cursor.lastrowid;

  