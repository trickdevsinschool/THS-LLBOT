#set, get , and update grades here
from LLBOT.studentmodel import LLBOTdb

class grades():

    db = LLBOTdb.LLBOTdb()
    conn = db.get_connection()
    cursor = conn.cursor()

    def __init__(self, isNew, studentid):
        if isNew =='Y' or isNew =='y':
            self.studentid = studentid
            self.curr_lesson="SVA" 
            self.curr_level= "1"
            self.curr_score="0"
            self.prereq="0"
            self.new_student_score(self.studentid)
        elif isNew =='N' or isNew == 'n':
            # GET THE LATEST VALUE FROM DB OF THE STUDENT SCORE
            self.studentid = studentid
            
            self.curr_level,self.curr_score = self.getLatestLvlScore(self.studentid)
            self.curr_lesson,self.prereq = self.getCurrentLesson(self.getcurr_lesson(self.studentid))

   
   #METHODS
   #gets the current lesson the student is learning
    def getcurr_lesson(self,studentID):
       sql="SELECT MAX(lessonID) FROM scores where studentID=%s"
       self.cursor.execute(sql, [studentID])
       res = self.cursor.fetchone()

       lesid=res[0]

       return lesid

    def getcurr_level(self, studentID,lessonID):
       sql="SELECT level from scores where studentID=%s and lessonID=%s"
       self.cursor.execute(sql, [studentID,lessonID])
       res = self.cursor.fetchone()

       level=res[0]
       return level

    ##GETS ALL LATEST STUDENT CURRENT VALUES
    def getLatestLvlScore(self, studentID):
        sql= "SELECT MAX(lessonID) AS highestLvl, score  FROM scores WHERE studentID = %s"
        self.cursor.execute(sql, [studentID])
        res = self.cursor.fetchone()

        score = res[0]
        level = res[1]

        return str(level), str(score)

    def getCurrentLesson(self,lessonID):
        sql = "SELECT lessonCode, preReq FROM lessons WHERE id = %s"
        self.cursor.execute(sql,[lessonID])
        res = self.cursor.fetchone()
        print(res)
        lesson = res[0]
        preReq = res[1]

        return lesson, preReq


    ##CREATES SVA SCORE ROW TO INITIALIZE STUDENT
    def new_student_score(self,studentId):
        sql ="INSERT INTO scores (studentID, lessonID, score, level, status, status_) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql,[studentId, 1, 0, "Beginner", 0, "In Progress"])
        print("New student SVA score initialized.")
        self.conn.commit()

    ##CREATES A NEW ROW IN SCORES TABLE given the STUDENT ID AND LESSON ID
    def unlock_new_lesson(self,studentID, lessonID):
        sql ="INSERT INTO scores (studentID, lessonID, score, level, status, status_) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql,[studentID, lessonID, 0, "Beginner", 0, "In Progress"])
        print("New lesson initialized.")
        self.conn.commit()

    ##GETS SCORE OF STUDENT AND LESSON
    def get_Score(self,studentID, lessonID):
        sql ="SELECT score FROM scores WHERE studentID = %s AND lessonID = %s"
        self.cursor.execute(sql,[studentID, lessonID])
        score = self.cursor.fetchone()[0] ##always only gets one row because of StudentID + LessonID

        return score 
    
    ## RETRIEVES student score and increases and adjusts statuses accordingly
    def inc_Score(self,studentID, lessonID):
        sql="UPDATE scores SET score = %s, level = %s, status =%s, status_= %s WHERE studentID = %s AND lessonID = %s"
        score = self.get_Score(studentID,lessonID)
        new_score = score + 1
        
        if(score >= 0 and score < 3 ): 
            level = "Beginner"
            status = 0
            status_ = "In Progress"

        elif(score >= 3 and score < 5):
            level = "Intermediate"
            status = 0
            status_ = "In Progress"

        elif(score >= 5 and score < 8):
            level = "Intermediate"
            status = 1
            status_ = "Passed"
        
        elif(score >=8 and score < 10):
            level = "Expert"
            status = 1
            status_ = "Passed"

        ## SCORE CANNOT GO ABOVE 10
        elif(score == 10):
            new_score = 10
            level = "Expert"
            status = 1
            status_ = "Passed"
        
        self.cursor.execute(sql, [new_score, level, status, status_, studentID, lessonID])
        self.conn.commit()
    
    ## RETRIEVES student score and decrease and adjusts statuses accordingly
    def dec_Score(self,studentID, lessonID):
        sql="UPDATE scores SET score = %s, level = %s, status =%s, status_= %s WHERE studentID = %s AND lessonID = %s"
        score = self.get_Score(studentID,lessonID)
        
        ##SCORE CANNOT GO BELOW ZERO
        if(score == 0):
            new_score = 0
            level = "Beginner"
            status = 0
            status_ = "In Progress"
        
        elif(score > 0 and score <= 4):
            new_score = score - 1
            level = "Beginner"
            status = 0
            status_ = "In Progress"

        elif(score > 4 and score <= 6):
            new_score = score - 1
            level = "Intermediate"
            status = 0
            status_ = "In Progress"

        elif(score == 7 or score == 8):
            new_score = score - 1
            level = "Intermediate"
            status = 1
            status_ = "Passed"
        
        elif(score > 8):
            new_score = score - 1
            level = "Expert"
            status = 1
            status_ = "Passed"
        
        self.cursor.execute(sql, [new_score, level, status, status_, studentID, lessonID])
        self.conn.commit()