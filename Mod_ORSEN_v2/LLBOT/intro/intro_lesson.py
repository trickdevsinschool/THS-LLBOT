import time
from LLBOT.studentmodel import LLBOTdb

db = LLBOTdb.LLBOTdb()
conn = db.get_connection()
cursor = conn.cursor()

class intro_lesson():
    secs= 1.5
    studentname=" "
    stud= " "
    studID=" "


    def __init__(self,student, t_f): #initializes everything
        self.stud= student
        self.studID= student.getstudentid()
        self.lesson= student.grades.getcurr_lesson(self.studID)
        self.firstsession= t_f
        self.studentname= self.stud.getstudentname()
        
    def initwelcome(self,studentname): #makes the opening statement with the name
        welcome_line= "Hello " + studentname + " nice to meet you!"
        return welcome_line
    
    def startlesson(self):

        if self.firstsession == True:
            welcome_line = self.initwelcome(self.studentname)
            print(welcome_line)
            time.sleep(self.secs)
            print("I'm LLBOT!")
            time.sleep(self.secs)
            if self.stud.grades.getcurr_lesson(self.studID) == 1:  # checks if curr lesson of the student is SVA
                sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
                cursor.execute(sql, ["SVA", "GEN"])
                res = cursor.fetchall()
                res = [i[0] for i in res]
                SVAexamples = []
                for i in range(8, 19, 1):
                    SVAexamples.append(res[i])
                print("=========================================================")
                print("LLBOT: Before we start, I have to ask. Are you familiar with the Subject Verb Agreement?")
                print("=========================================================")
                user_reply = input()
                teach = True
                if user_reply == "yes" or user_reply == "Yes":
                    print("=========================================================")
                    print("LLBOT: " + res[0])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
                    teach = False
                elif user_reply == "No" or user_reply == "no":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[1])
                    print("\n" + res[3])
                    print("\n" + res[4])
                    print("\n" + res[5])
                    print("\n" + res[6])
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("\nNow that the terms are clear,\n" + res[7])
                    print("\n" + SVAexamples[i] + "\n")
                    i = i + 1
                    print(SVAexamples[i])
                    i = 2
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + SVAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False

                elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + SVAexamples[i])
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + SVAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False
            elif self.stud.grades.getcurr_lesson(self.studID) == 2:
                sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
                cursor.execute(sql, ["OOA", "GEN"])
                res = cursor.fetchall()
                res = [i[0] for i in res]
                OOAexamples = []
                for i in range(8, 13, 1):
                    OOAexamples.append(res[i])
                print("=========================================================")
                print("LLBOT: Before we start, I have to ask. Are you familiar with the Order of Adjectives?")
                print("=========================================================")
                user_reply = input()
                teach = True
                if user_reply == "yes" or user_reply == "Yes":
                    print("=========================================================")
                    print("LLBOT: " + res[0])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
                    teach = False
                elif user_reply == "No" or user_reply == "no":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[1])
                    print("\n" + res[3])
                    print("\n" + res[4])
                    print("\n" + res[5])
                    print("\n" + res[6])
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("\nNow that the terms are clear,\n" + res[7])
                    print("\n" + OOAexamples[i] + "\n")
                    i = i + 1
                    print(OOAexamples[i])
                    i = 2
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + OOAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False
                elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + OOAexamples[i])
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + OOAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False
            elif self.stud.grades.getcurr_lesson(self.studID) == 3:
                sql = "SELECT dialogue_template FROM lessonresponse  WHERE dialogue_code= %s OR dialogue_code= %s"
                cursor.execute(sql, ["DOA", "GEN"])
                res = cursor.fetchall()
                res = [i[0] for i in res]
                DOAexamples = []
                for i in range(8, 13, 1):
                    DOAexamples.append(res[i])
                print("=========================================================")
                print("LLBOT: Before we start, I have to ask. Are you familiar with the Degree of Adjectives?")
                print("=========================================================")
                user_reply = input()
                teach = True
                if user_reply == "yes" or user_reply == "Yes":
                    print("=========================================================")
                    print("LLBOT: " + res[0])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
                    teach = False
                elif user_reply == "No" or user_reply == "no":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[1])
                    print("\n" + res[3])
                    print("\n" + res[4])
                    print("\n" + res[5])
                    print("\n" + res[6])
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("\nNow that the terms are clear,\n" + res[7])
                    print("\n" + DOAexamples[i] + "\n")
                    i = i + 1
                    print(DOAexamples[i])
                    i = 2
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + DOAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False
                elif user_reply == "A little bit" or user_reply == "a little bit":
                    i = 0
                    print("=========================================================")
                    print("LLBOT: " + res[2])
                    print(res[7])
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("\nFor example:")
                    print("\n" + DOAexamples[i])
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach == True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example = input()
                        if (more_example == "Yes" or more_example == "yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + DOAexamples[i])
                            print("=========================================================")
                        else:
                            teach = False
            print("=========================================================")
            print("LLBOT: Now let's make a story to test this new lesson out!")
            print("LLBOT: Try to start your first story by telling me what a character is doing!")
            print("LLBOT: For example: The king sings a song")
            print("LLBOT:Go ahead! You try!")
            print("=========================================================")
            
            #end of intro module, should return to Driver.py and execute start_storytelling()
            
            
    