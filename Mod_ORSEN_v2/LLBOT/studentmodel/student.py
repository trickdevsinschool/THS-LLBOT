#set, get, update students here
from LLBOT.studentmodel import LLBOTdb
from LLBOT.studentmodel import grades


class student():

    db = LLBOTdb.LLBOTdb()
    conn = db.get_connection()
    cursor = conn.cursor()

    ## IF IS NEW == true then Create a new student IF NOT A NEW STUDENT student variable will contain studentID
    def __init__(self, isNew, student): 
        #TO Broqz: these should be SQL fetches thanks! -Trick
        if(isNew == 'y' or isNew == 'Y'):
            self.studentname = student
            self.studentid = self.create_new_student(self.studentname)
            self.grades = grades.grades(isNew , self.studentid)
        else:
            self.studentid, self.studentname = self.getStudentbyId(student)
            self.grades = grades.grades(isNew , self.studentid)


    #Additional methods below
    def getstudentname(self):
        return self.studentname

    #Creates a new student returns the ID
    def create_new_student(self,studentName):
        sql = "INSERT INTO students (studentName) VALUES (%s)"
        self.cursor.execute(sql,[studentName])
        print("Current Student Count:", self.cursor.rowcount, "new student was inserted.")
        self.conn.commit()
        return self.cursor.lastrowid

    def getstudentid(self):
        return self.studentid

    def getStudentbyId(self, studentID):
        sql = "SELECT * from students WHERE id = %s"
        self.cursor.execute(sql,[studentID])
        res = self.cursor.fetchone()

        id = res[0]
        name = res[1]

        return id,name ##studentId and studentName
 
