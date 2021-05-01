import time
from LLBOT.studentmodel import *



class intro_lesson():
    firstsession= True #first session should depend on the student id retrieved from the db. Not sure if need to put another column or just look at existing values like score or passed/inprogress
    secs= 1
    studentname=" "
    stud= " "
    def __init__(self,student): #initializes everything
        self.stud= student
        self.lesson= student.grades.getcurr_lesson()
        self.firstsession=True
        self.studentname= self.stud.getstudentname()
        
    def initwelcome(self,studentname): #makes the opening statement with the name
        welcome_line= "Hello " + studentname + " nice to meet you!"
        return welcome_line
    
    def startlesson(self):
        if self.firstsession==True:
            welcome_line= self.initwelcome(self.studentname)
            print(welcome_line)
            time.sleep(self.secs)
            print("I'm LLBOT!")
            time.sleep(self.secs)
            if self.stud.grades.getcurr_lesson() =="SVA": #checks if curr lesson of the student is SVA
                print("=========================================================")
                print("LLBOT: Before we start, I have to ask. Are you familiar with the Subject Verb Agreement?")
                print("=========================================================")
            user_reply= input()
            teach= True
            if user_reply=="yes" or user_reply=="Yes":
                print("=========================================================")
                print("LLBOT: Awesome! Just a quick refresher")
                print("=========================================================")
                time.sleep(self.secs)
                print("=========================================================")
                print("LLBOT: <Here is Main description>")
                print("LLBOT: <Here is an example>")
                print("=========================================================")
                teach=False
            elif user_reply=="No" or user_reply=="no":
                print("=========================================================")
                print("LLBOT: That's alright! We can learn about it together!")
                print("=========================================================")
                time.sleep(self.secs)
                print("=========================================================")
                print("<Here is Main description>")
                print("<Here is supporting description")
                print("<Here is another description")
                print("<Here is example")
                print("=========================================================")
                time.sleep(self.secs)
                while teach==True:
                    print("=========================================================")
                    print("Do you want another example?")
                    print("=========================================================")
                    more_example= input()
                    if (more_example=="Yes" or more_example=="yes"):
                        print("=========================================================")
                        print("LLBOT: <Here is another example>")
                        print("LLBOT: Do you want another one?")
                        print("=========================================================")
                    else:
                        teach=False
                        
            elif user_reply=="A little bit":
                print("=========================================================")
                print("LLBOT: That's alright! I'll help you remember")
                print("=========================================================")
                time.sleep(self.secs)
                print("=========================================================")
                print("LLBOT: <Here is Main description>")
                print("LLBOT: <Here is supporting description>")
                print("LLBOT: <Here is an example>") 
                print("=========================================================")
                time.sleep(self.secs)
                while teach==True:
                    print("Do you want another example?")
                    more_example=input()
                    if (more_example=="Yes" or more_example=="yes"):
                        print("=========================================================")
                        print("LLBOT: <Here is another example>")
                        print("LLBOT: Do you want another one?")
                        print("=========================================================")
                    else:
                        teach=False
            print("=========================================================")
            print("LLBOT: Now let's make a story to test this new lesson out!")
            print("LLBOT: Try to start your first story by telling me about a character and what they are doing")
            time.sleep(self.secs)
            print("LLBOT: For example: A king eats an apple!")
            print("LLBOT:Go ahead! You try!")
            print("=========================================================")
            #end of intro module, should return to Driver.py and execute start_storytelling()
            
            
    