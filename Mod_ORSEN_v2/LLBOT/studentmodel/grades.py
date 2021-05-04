#set, get , and update grades here
from LLBOT.studentmodel import LLBOTdb

class grades():

    db = LLBOTdb()
    conn = db.get_connection()
    cursor = conn.cursor()

    def __init__(self,studentid):
        self.studentid = studentid
        self.curr_lesson="SVA" 
        self.curr_level= "1"
        self.curr_score="0"
        self.prereq="0"
        
   #additional methods below
   
    def getcurr_lesson(self):
       return self.curr_lesson   

    ##CREATES SVA SCORE ROW TO INITIALIZE STUDENT
    def new_student_score(studentId):
        sql ="INSERT INTO scores (studentID, lessonID, score, level, status, status_) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,[studentId, 1, 0, "Beginner", 0, "In Progress"])
        print("New student SVA score initialized.")
        conn.commit()

    ##CREATES A NEW ROW IN SCORES TABLE given the STUDENT ID AND LESSON ID
    def unlock_new_lesson(studentID, lessonID):
        sql ="INSERT INTO scores (studentID, lessonID, score, level, status, status_) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,[studentID, lessonID, 0, "Beginner", 0, "In Progress"])
        print("New lesson initialized.")
        conn.commit()

    ##GETS SCORE OF STUDENT AND LESSON
    def get_Score(studentID, lessonID):
        sql ="SELECT score FROM scores WHERE studentID = %s AND lessonID = %s"
        cursor.execute(sql,[studentID, lessonID])
        score = cursor.fetchone()[0] ##always only gets one row because of StudentID + LessonID

        return score 
    
    ## RETRIEVES student score and increases and adjusts statuses accordingly
    def inc_Score(studentID, lessonID):
        sql="UPDATE scores SET score = %s, level = %s, status =%s, status_= %s WHERE studentID = %s AND lessonID = %s"
        score = get_Score(studentID,lessonID)
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
        
        cursor.execute(sql, [new_score, level, status, status_, studentID, lessonID])
        mydb.commit()
    
    ## RETRIEVES student score and decrease and adjusts statuses accordingly
    def dec_Score(studentID, lessonID):
        sql="UPDATE scores SET score = %s, level = %s, status =%s, status_= %s WHERE studentID = %s AND lessonID = %s"
        score = get_Score(studentID,lessonID)
        
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
        
        cursor.execute(sql, [new_score, level, status, status_, studentID, lessonID])
        mydb.commit()