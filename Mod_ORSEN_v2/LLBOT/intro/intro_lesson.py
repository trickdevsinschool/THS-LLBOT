import time
from LLBOT.studentmodel import *
from src import Logger



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

        if self.firstsession==True:
            welcome_line= self.initwelcome(self.studentname)
            print(welcome_line)
            time.sleep(self.secs)
            print("I'm LLBOT!")
            time.sleep(self.secs)
            if self.stud.grades.getcurr_lesson(self.studID) ==1: #checks if curr lesson of the student is SVA
                i = 0
                SVAexamples = ["If the subject is singular, the verb must be singular too.\nExample: She writes every day.",
                         "If the subject is plural, the verb must also be plural.\nExample: They write every day. ",
                         "When the subject of the sentence is composed of two or more nouns or pronouns connected by and, use a plural verb.\nExample: The doctoral student and the committee members write every day.",
                         "When there is one subject and more than one verb, the verbs throughout the sentence must agree with the subject.\nExample: Interviews are one way to collect data and allow researchers to gain an in-depth understanding of participants.",
                         "When a phrase comes between the subject and the verb, remember that the verb still agrees with the subject, not the noun or pronoun in the phrase following the subject of the sentence.\nExample: The student, as well as the committee members, is excited.",
                         "When two or more singular nouns or pronouns are connected by 'or' or 'nor,' use a singular verb.\nExample: The chairperson or the CEO approves the proposal before proceeding.",
                         "When a compound subject contains both a singular and a plural noun or pronoun joined by 'or' or 'nor,' the verb should agree with the part of the subject that is closest to the verb. This is also called the rule of proximity.\nExample: The student or the committee members write every day.\nExample: The committee members or the student writes every day.",
                         "The words and phrases 'each,' 'each one,' 'either,' 'neither,' 'everyone,' 'everybody,' 'anyone,' 'anybody,' 'nobody,' 'somebody,' 'someone,' and 'no one' are singular and require a singular verb.\nExample: Each of the participants was willing to be recorded.\nExample: Neither alternative hypothesis was accepted.",
                         "Noncount nouns take a singular verb.\nExample: Education is the key to success.\nExample: Diabetes affects many people around the world.",
                         "Some countable nouns in English such as earnings, goods, odds, surroundings, proceeds, contents, and valuables only have a plural form and take a plural verb.\nExample: The earnings for this quarter exceed expectations.",
                         "In sentences beginning with 'there is' or 'there are,' the subject follows the verb. Since 'there' is not the subject, the verb agrees with what follows the verb. Example: There is little administrative support.\nExample: There are many factors affecting teacher retention.",
                         "Collective nouns are words that imply more than one person but are considered singular and take a singular verb. Some examples are 'group,' 'team,' 'committee,' 'family,' and 'class.'\nExample: The group meets every week."]
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
                    print("\nLLBOT: SVA states that subjects and verbs must AGREE with one another in number (singular or plural).")
                    print(" Usage:\n")
                    print(SVAexamples[0])
                    print("=========================================================")
                    teach=False
                elif user_reply=="No" or user_reply=="no":
                    print("=========================================================")
                    print("LLBOT: That's alright! We can learn about it together!")
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("LLBOT: Let’s start with defining the terms first")
                    print("\n   Subject" +"\n"
                          " -is the one being talked about in the sentence\n"
                          " -is often the doer of the action\n")
                    print(" Verb\n"
                          " -is the one that talks about the subject\n"
                          " -is often the action or condition of the subject\n")
                    print("Now, what is Subject-Verb Agreement (SVA)?\n")
                    print(" SVA states that subjects and verbs must AGREE with one another in number (singular or plural).\n"
                          " Thus, if a subject is singular, its verb must also be singular;\n"
                          " if a subject is plural, its verb must also be plural.\n")
                    print("Usage:\n")
                    print(SVAexamples[i]+"\n")
                    i=i+1
                    print(SVAexamples[i])
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach==True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example= input()
                        if (more_example=="Yes" or more_example=="yes"):
                            i=i+1
                            print("=========================================================")
                            print("LLBOT: "+ SVAexamples[i])
                            print("=========================================================")
                        else:
                            teach=False

                elif user_reply=="A little bit" or user_reply=="a little bit":
                    print("=========================================================")
                    print("LLBOT: That's alright! I'll help you remember")
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("LLBOT: Subject-Verb Agreement (SVA) states that subjects and verbs must AGREE with one another in number (singular or plural).  "
                          "\n   Thus, if a subject is singular, its verb must also be singular; "
                          "\n   if a subject is plural, its verb must also be plural.")
                    print("\nUsage:")
                    print("\n"+ SVAexamples[i])
                    print("=========================================================")
                    time.sleep(self.secs)
                    while teach==True:
                        print("=========================================================")
                        print("LLBOT: Do you want another example?")
                        print("=========================================================")
                        more_example=input()
                        if (more_example=="Yes" or more_example=="yes"):
                            i = i + 1
                            print("=========================================================")
                            print("LLBOT: " + SVAexamples[i])
                            print("=========================================================")
                        else:
                            teach=False
            elif self.stud.grades.getcurr_lesson(self.studID) == 2:
                i = 0
                OOAexamples = ["I saw Kresta carrying a huge, orange, wooden bookshelf.\n"
                               "    -size -> color -> material",
                               "There are five large rectangular paintings inside our house:\n"
                               "    -quantity -> size -> shape",
                               "I want to give you a beautiful large yellow paper sunflower.\n"
                               "    -opinion -> size -> color -> material",
                               "We cooked creamy heart-shaped yema candies in school.\n"
                               "    -opinion -> shape",
                               "Georgee lives with her fat old brown cat named Pepe.\n"
                               "    -opinion -> age -> color"] #transfer to db
                print("=========================================================")
                print("LLBOT: Before we start, I have to ask. Are you familiar with the Order of Adjectives?")
                print("=========================================================")
                user_reply = input()
                teach = True
                if user_reply == "yes" or user_reply == "Yes":
                    print("=========================================================")
                    print("LLBOT: Awesome! Just a quick refresher")
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("\nLLBOT: Order of Adjectives (OOA) states that when more than one adjective comes before a noun, the adjectives are normally in a particular order")
                    print(" Usage:\n")
                    print(OOAexamples[0])
                    print("=========================================================")
                    teach = False
                elif user_reply == "No" or user_reply == "no":
                    print("=========================================================")
                    print("LLBOT: That's alright! We can learn about it together!")
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print("LLBOT: Let’s start with defining the terms first")
                    print("\n   Order" + "\n"
                            " -the arrangement or disposition of things\n"
                            " -a particular pattern or sequence")
                    print("\n   Adjective\n"
                          " -words that describe nouns\n"
                          " -modifies a noun or noun phrase or describes its referent\n")
                    print("Now, what is Order of Adjectives (OOA)?\n")
                    print(" OOA states that when more than one adjective comes before a noun, the adjectives are normally in a particular order.\n"
                          " Adjectives which describe opinions or attitudes usually come first, before more neutral, factual ones.\n")
                    print("The most usual sequence of adjectives is:\n"
                          " 1. QUANTITY: How many are there? one, some, few\n"
                          " 2. OPINION:  What do you think about something? beautiful, wonderful, cute\n"
                          " 3. SIZE: How big or small is it? small, tall, big\n"
                          " 4. AGE:  How old or young is it? old, new, young\n"
                          " 5. SHAPE:    What is the shape? square, round, irregular\n"
                          " 6. COLOR:    What color is it? blue, yellow, red\n"
                          " 7. ORIGIN:   Where is it from? American, Spanish, Filipino\n"
                          " 8. MATERIAL: What is it made of? paper, plastic, metal\n")
                    print("Usage:\n")
                    print(OOAexamples[i] + "\n")
                    i = i + 1
                    print(OOAexamples[i])
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
                    print("=========================================================")
                    print("LLBOT: That's alright! I'll help you remember")
                    print("=========================================================")
                    time.sleep(self.secs)
                    print("=========================================================")
                    print(
                        "LLBOT: Order of Adjectives (OOA) states that when more than one adjective comes before a noun, the adjectives are normally in a particular order. "
                        "\nAdjectives which describe opinions or attitudes usually come first, before more neutral, factual ones.")
                    print("\nUsage:")
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
            print("=========================================================")
            print("LLBOT: Now let's make a story to test this new lesson out!")
            print("LLBOT: Try to start your first story by telling me what a character is doing!")
            print("LLBOT: For example: The king sings a song")
            print("LLBOT:Go ahead! You try!")
            print("=========================================================")
            
            #end of intro module, should return to Driver.py and execute start_storytelling()
            
            
    