#set, get , and update grades here
from LLBOT.studentmodel import LLBOTdb
from src import Logger
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
        #fetches string level: Beginner, Expert, Intermediate
       sql="SELECT level from scores where studentID=%s and lessonID=%s"
       self.cursor.execute(sql, [studentID,lessonID])
       res = self.cursor.fetchone()

       level=res[0]
       return level

    ##GETS ALL LATEST STUDENT CURRENT VALUES
    def getLatestLvlScore(self, studentID):
        level= self.getcurr_lesson(studentID)
        score= self.get_Score(studentID,level)

        return level, score

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
    def get_status (self,studentID,lessonID):
        sql ="SELECT status FROM scores WHERE studentID=%s and lessonID=%s "
        self.cursor.execute(sql,[studentID,lessonID])
        status= self.cursor.fetchone()
        
        status1=status[0]
        
        return status1
    def checkIfCanPass(self,studentID,lessonID,bot,message):
        
        clessonid, cscore= self.getLatestLvlScore(studentID)
        status= self.get_status(studentID,clessonid)
        if status==0 and cscore==6 and lessonID!=3:
            sql ="UPDATE scores SET status=1,status_= %s WHERE studentID = %s AND lessonID = %s"
            self.cursor.execute(sql,["Passed", studentID, clessonid])
            self.conn.commit()
            self.unlock_new_lesson(studentID,clessonid+1)
            if(lessonID==1):
                bot.reply_to(message,"Hey! Looks like you're good enough to learn about a new topic! \U0001F929")
                bot.reply_to(message, "How about we try learning Order of Adjectives now!")
                bot.reply_to(message, "Order of Adjectives talks about the proper arrangement of how you describe an object")
                bot.reply_to(message, "Go ahead and try to describe a new character to your story! \U0001F98A \U0001F43C \uE527")
                bot.reply_to(message, "Example: A big, brown, happy wolf")
                bot.reply_to(message, "The order of adjective should be as follows: Quantity, Opinion, Size, Age, Shape, Color, Origin, and then Material")
                bot.reply_to(message,"Go ahead, test it out!")
                Logger.log_conversation("LLBOT: Hey! Looks like you're good enough to learn about a new topic!")
                Logger.log_conversation("LLBOT: How about we try learning Order of Adjectives now!")
                Logger.log_conversation("LLBOT: Order of Adjectives talks about the proper arrangement of how you describe an object")
                Logger.log_conversation("LLBOT: Go ahead and try to describe a new character to your story!")
                Logger.log_conversation("LLBOT: Example: A big brown happy wolf ate a rabbit.")
                Logger.log_conversation("LLBOT: The order of adjective should be as follows: Quantity,Opinion,Size,Age,Shape,Color,Origin, and then Material")
                Logger.log_conversation("LLBOT: Go ahead, test it out!")
            elif(lessonID==2):
                bot.reply_to(message, "YAHOOO! You're doing great! Let's try to learn about Degree of Adjectives now! \U0001F929")
                bot.reply_to(message, "Degree of Adjective says that adjectives are compared in different ways: positive, comparative and superlative.")
                bot.reply_to(message, "Adjectives form their comparative by adding ???er??? at the end of the word or adding ???more??? before the adjective and their superlative by adding ???est??? at the end of the word or adding ???most??? before the adjective.")
                bot.reply_to(message, "Example: Eric is taller than Richard")
                bot.reply_to(message, "or another example would be: The king is the greatest of them all!")
                bot.reply_to(message,"Go ahead and create comparisons between your own characters! \U0001F469\u200D\U0001F3A4 \U0001F468\u200D\U0001F3A4")
                Logger.log_conversation("LLBOT: YAHOOO! You're doing great! Let's try to learn about Degree of Adjectives now!")
                Logger.log_conversation("LLBOT: Degree of Adjective says that adjectives are compared in different ways: positive, comparative and superlative.")
                Logger.log_conversation("LLBOT: Adjectives form their comparative by adding ???er??? at the end of the word or adding ???more??? before the adjective and their superlative by adding ???est??? at the end of the word or adding ???most??? before the adjective.")
                Logger.log_conversation("LLBOT: Example: Eric is taller than Richard")
                Logger.log_conversation("LLBOT: or another example would be: The king is the greatest of them all!")
                Logger.log_conversation("LLBOT: Go ahead and create comparisons between your own characters!")
        elif status==0 and cscore==6 and lessonID==3:
                bot.reply_to(message, "Psst, hey! \U0001F440")
                bot.reply_to(message, "You're probably loving your story right now but I just want to tell you...")
                bot.reply_to(message, "You've accomplished all of our lessons pretty well so far! \U0001F973")
                bot.reply_to(message, "From Subject-Verb Agreement to Order of Adjectives to Degree of Adjectives...")
                bot.reply_to(message, "You aced them all! Congrats champ! \uE131 \U0001F947")
                bot.reply_to(message,"Now, let's get back to creating your story! I wanna hear more about it!")
                bot.reply_to(message,"What happens next?")
                Logger.log_conversation("LLBOT: Psst, hey!")
                Logger.log_conversation("LLBOT: You're probably loving your story right now but I just want to tell you...")
                Logger.log_conversation("LLBOT: You've done all of our lessons pretty well so far!")
                Logger.log_conversation("LLBOT: From Subject-Verb Agreement to Order of Adjectives to Degree of Adjectives...")
                Logger.log_conversation("LLBOT:You aced them all! Congrats champ!")
                Logger.log_conversation("LLBOT: Now, let's get back to creating your story! I wanna hear more about it!")
                Logger.log_conversation("LLBOT: What happens next?")
                sql ="UPDATE scores SET status=1,status_= %s WHERE studentID = %s AND lessonID = %s"
                self.cursor.execute(sql,["Passed", studentID, clessonid])
                self.conn.commit()


            



    ## RETRIEVES student score and increases and adjusts statuses accordingly
    def inc_Score(self,studentID, lessonID,bot,message):
        level=""
        sql="UPDATE scores SET score = %s, level = %s WHERE studentID = %s AND lessonID = %s"
        score = self.get_Score(studentID,lessonID)
        new_score = score + 1
        
        if(new_score >= 0 and new_score < 4 ): 
            level = "Beginner"
            

        elif(new_score >= 4 and new_score <=7):
            level = "Intermediate"
            
        
        elif(new_score >= 8 and new_score < 10):
            level = "Expert"
            

        ## SCORE CANNOT GO ABOVE 10
        elif(score == 10):
            new_score = 10
            level = "Expert"
            
        
        self.cursor.execute(sql, [new_score, level, studentID, lessonID])
        self.conn.commit()
        self.checkIfCanPass(studentID,lessonID,bot,message)
    
    ## RETRIEVES student score and decrease and adjusts statuses accordingly
    def dec_Score(self,studentID, lessonID):
        sql="UPDATE scores SET score = %s, level = %s WHERE studentID = %s AND lessonID = %s"
        score = self.get_Score(studentID,lessonID)
        
        ##SCORE CANNOT GO BELOW ZERO
        if(score == 0):
            new_score = 0
            level = "Beginner"
            
        
        elif(score > 0 and score <= 4):
            new_score = score - 1
            level = "Beginner"
            

        elif(score > 4 and score <= 6):
            new_score = score - 1
            level = "Intermediate"
            

        elif(score == 7 or score == 8):
            new_score = score - 1
            level = "Intermediate"
            
        
        elif(score > 8):
            new_score = score - 1
            level = "Expert"
            
        
        self.cursor.execute(sql, [new_score, level, studentID, lessonID])
        self.conn.commit()