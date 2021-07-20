from LLBOT.correction_response import start
from src.dbo import user
from src.dbo.user import DBOUser
from src.models.user import User
from src import Logger, IS_AFFIRM, IS_DENY, IS_END, UserHandler, DIALOGUE_TYPE_E_END, DIALOGUE_TYPE_RECOLLECTION, Pickle
from src.constants import *
from src.ORSEN import ORSEN
from src.textunderstanding.InputDecoder import InputDecoder
import datetime
import telebot

import time

#LLBOT imports
from LLBOT import mainLLBOT 
from LLBOT import LLBOT_proofreading

#TELEGRAM BOT 
TOKEN = "1911425925:AAEGVXLEG7JzdiNwZ_VMzZLeRjbEZhPvlY0"
bot = telebot.TeleBot(TOKEN)

# Database access
dbo_user = DBOUser('users', User)

def get_input():
    user_input = input()
    return user_input

def login_signup():
    print("Hi! Do you have an account? (Y/N)")
    user_input = input()

    if user_input == "Y":  # login
        login()
    else:
        signup()
    print(UserHandler.get_instance().curr_user)

def login():
    # ask for user details
    is_done = False

    while not is_done:
        print("What's your username?")
        name = input()
        print("What's is the secret code?")
        code = input()

        temp_user = dbo_user.get_specific_user(name, code)

        if temp_user is None:
            print("I don't think that's right. Can you try again?")

        else:
            # store user
            UserHandler.get_instance().set_global_curr_user(temp_user)
            print("Hi! Welcome back ", name)
            is_done = True

def signup():
    print("What's your username?")
    name = input()
    print("What's is the secret code?")
    code = input()

    UserHandler.get_instance().set_global_curr_user(dbo_user.add_user(User(-1, name, code)))

def login_signup_automatic():
    print("What's your name?")
    name = get_input()

    user_list = dbo_user.get_user_by_name('name')
    if user_list is not []:
        print("Do we have a secret code?")
        has_code_answer = get_input()
        has_code = False

        if has_code_answer.lower() == "y" or has_code_answer.lower() == "yes":
            print("What is the secret code?")
            input_code = get_input()
            temp_user = dbo_user.get_specific_user(name, input_code)

        else:
            # has_code_answer.lower() == "n" or has_code_answer.lower() == "no":
            print("Alright then let's make one! What should it be?")
            input_code = get_input()
            temp_user = dbo_user.add_user(User(-1, name, input_code))

        UserHandler.get_instance().set_global_curr_user(temp_user)
        print("Alright %s, let's make a story. You start!")

def clean_user_input(response):
    #Tweaked for capitalization
    response = response.strip()
    if response.endswith(".") == False:
        response = response + "."
    if response== "the end.":
        return response
    else: 
        first_word= response.split()[0]
        first_word=first_word.capitalize()

        #print(first_word)

        response= response.replace(response.split()[0],first_word,1)

        return response

def orsen_welcome():
    if CURR_ORSEN_VERSION == "ORSEN2":
        login_signup()

def start_storytelling(bot):
    is_end_story = False
    while not is_end_story:
        start_time = time.time()
        #user_input = get_input() #TODO: Uncomment after testing

        print("TRYING TO GET TIME %s: " % (time.time() - start_time))
        print("TRYING TO GET TIME again : ", str(time.time() - start_time))

        #Logger.log_conversation("LATENCY TIME (seconds): " + str(time.time() - start_time))
        # user_input = "John kicked the love"
        @bot.message_handler(content_types=['text'])
        def handle_text(message):
            user_input = message.text

            Logger.log_conversation("User : " + str(user_input))

            is_end_story = orsen.is_end_story(user_input)
            print("IS END STORY: ", is_end_story)
            
            if not is_end_story:
                #introlesson
                #check if it is a "what*** ?" question
                #check if wrong, check if right
                #if wrong: ind/direct, then orsen
                #if right :orsen
                #llbot_proofreading(user_input) if may error-> llbot mode + update student model, if wala & proper use of SVA,OAD,DOA-> back to orsen + update studentmodel
                #proofread_response = LLBOT_proofreading.call(user_input, studentid)
                proofread_response=0
                
                if proofread_response == 1:
                    print(" ")
                elif proofread_response == 0:
                    print("=========================================================")
                    print("No error, continue:")
                    print("=========================================================")

                    #insert our get user input
                    orsen_response = orsen.get_response(user_input) #[TRACE] 1st This goes to ORSEN.py
                    print("=========================================================")
                    #[TRACE] print("story telling starts here")
                    print("LLBOT" + ": " + orsen_response)
                    print("=========================================================")
                    Logger.log_conversation("LLBOT" + ": " + str(orsen_response))
                    bot.reply_to(message, orsen_response)
                    # is_end_story = orsen.is_end_story(user_input)
            elif CURR_ORSEN_VERSION == EDEN:
                """EDEN"""
                # orsen_response = orsen.get_response("", move_to_execute = DIALOGUE_TYPE_E_END)
                orsen_response = orsen.get_response("", move_to_execute = DIALOGUE_TYPE_RECOLLECTION)
                # orsen_response = orsen_response + orsen.get_response("", move_to_execute = DIALOGUE_TYPE_RECOLLECTION)
                print("=========================================================")
                print(CURR_ORSEN_VERSION + ": " + orsen_response)
                print("=========================================================")
                Logger.log_conversation(CURR_ORSEN_VERSION + ": " + str(orsen_response))
            elif CURR_ORSEN_VERSION == ORSEN1 or CURR_ORSEN_VERSION == ORSEN2:
                # """ORSEN"""
                orsen_response = "Thank you for the story! Do you want to hear it again?"
                print("=========================================================")
                    #[TRACE] print("story telling ends here")
                print("LLBOT" + ": " + orsen_response)
                print("=========================================================")
                Logger.log_conversation("LLBOT" + ": " + str(orsen_response))
                
                user_input = get_input()
                if user_input.lower() in IS_AFFIRM:
                    print(orsen.repeat_story())

orsen = ORSEN()


# start here
# Initialize loggers
Logger.setup_loggers()
# Retrieve User Details --- User objects
print("---------Retrieving User Details---------")
print("done")

# pickle_filepath = '../logs/user world/' + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + "-" + UserHandler.get_instance().curr_user.name
pickle_filepath = '../logs/user world/' + UserHandler.get_instance().curr_user.name
# pickle_filepath = '../Mod_ORSEN_v2//logs/user world/' + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + "-" + UserHandler.get_instance().curr_user.name

# try:
#
#
#
#     print("---------Launching ORSEN---------")
#
#     #TODO: uncomment after testing
#     #for repeating the story
#     is_engaged = True
#     while is_engaged:
#         orsen.initialize_story_prerequisites()
#         print("Let's make another story! You go first")
#         start_storytelling()
#
#         #save story world
#         Pickle.pickle_world_wb(pickle_filepath, orsen.world.get_pickled_world())
#
#         print("Do you want to make another story?")
#         user_input = get_input()
#         if user_input.lower() in IS_DENY:
#             is_engaged = False
#         # else:
#             # pickle_filepath = '../logs/user world/' + datetime.datetime.now().strftime(
#             #     "%Y-%m-%d %H-%M-%S") + "-" + UserHandler.get_instance().curr_user.name
#             # pickle_filepath = '../Mod_ORSEN_v2//logs/user world/' + datetime.datetime.now().strftime(
#             #     "%Y-%m-%d %H-%M-%S") + "-" + UserHandler.get_instance().curr_user.name
#
#
# except:
#     print("Something went wrong when writing to the file")
# finally:
#     print("AT FINALLY")
#     Pickle.pickle_world_wb(pickle_filepath, orsen.world.get_pickled_world())
#     Pickle.pickle_world_rb(pickle_filepath)
# print("---------Closing ORSEN---------")


# Logger.setup_loggers()
# print("---------Launching ORSEN---------")cd
# orsen.initialize_story_prerequisites()
# print("Let's make another story! You go first")
# start_storytelling()
# print("---------Closing ORSEN---------")


#print("---------Launching ORSEN---------")
#main
print("---------Launching LLBOT(ORSEN)---------")

# #TODO: uncomment after testing
#for repeating the story
is_engaged = False
is_end_story = False
#llbot= mainLLBOT.mainLLBOT()
studentID= ''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global is_engaged
    global is_end_story
    global studentID
    is_engaged = True
    is_end_story=False
    orsen.initialize_story_prerequisites()
    orsen.world.reset_world()
    orsen.dialogue_planner.reset_new_world() 
    studentid=""
    #temp_welcome = orsen.get_response(move_to_execute = orsen.dialogue_planner.get_welcome_message_type())
    #bot.reply_to(message,"Hi! I'm Sample LLBOT. Try to make a story!")
    #insert here the student creation
    mainLLBOT.start(message)
    

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global is_engaged
    global is_end_story
    user_input=message.text
    user_input= clean_user_input(user_input)
    #while is_engaged:

        # orsen_welcome()
        #print(temp_welcome)
        #mainLLBOT.start() is where to start the intro lesson module
        #llbot= mainLLBOT.mainLLBOT()
        #llbot.start()
        #studentid= llbot.retrieveStudentid()

        #start_storytelling(bot)
    #is_end_story = orsen.is_end_story(user_input)
    if(is_engaged):   
        is_end_story = orsen.is_end_story(user_input) 
     
        if not is_end_story:
            #introlesson
            #check if it is a "what*** ?" question
            #check if wrong, check if right
            #if wrong: ind/direct, then orsen
            #if right :orsen
            #llbot_proofreading(user_input) if may error-> llbot mode + update student model, if wala & proper use of SVA,OAD,DOA-> back to orsen + update studentmodel
            #proofread_response = LLBOT_proofreading.call(user_input, studentid)
            proofread_response=0
            
            if proofread_response == 1:
                print(" ")
            elif proofread_response == 0:
                print("=========================================================")
                print("No error, continue:")
                print("=========================================================")

                #insert our get user input
                orsen_response = orsen.get_response(user_input) #[TRACE] 1st This goes to ORSEN.py
                print("=========================================================")
                #[TRACE] print("story telling starts here")
                print("LLBOT" + ": " + orsen_response)
                print("=========================================================")
                Logger.log_conversation("LLBOT" + ": " + str(orsen_response))
                bot.reply_to(message, orsen_response)
                # is_end_story = orsen.is_end_story(user_input)
        #elif CURR_ORSEN_VERSION == EDEN:
            """EDEN"""
            # orsen_response = orsen.get_response("", move_to_execute = DIALOGUE_TYPE_E_END)
            #orsen_response = orsen.get_response("", move_to_execute = DIALOGUE_TYPE_RECOLLECTION)
            # orsen_response = orsen_response + orsen.get_response("", move_to_execute = DIALOGUE_TYPE_RECOLLECTION)
            #print("=========================================================")
            #print(CURR_ORSEN_VERSION + ": " + orsen_response)
            #print("=========================================================")
            #Logger.log_conversation(CURR_ORSEN_VERSION + ": " + str(orsen_response))
        elif CURR_ORSEN_VERSION == ORSEN1 or CURR_ORSEN_VERSION == ORSEN2:
            # """ORSEN"""
            is_engaged= False
            orsen_response = "Thank you for the story! Let's meet again next time!"
            bot.reply_to(message, orsen_response)
            print("=========================================================")
                #[TRACE] print("story telling ends here")
            print("LLBOT" + ": " + orsen_response)
            print("=========================================================")
            Logger.log_conversation("LLBOT" + ": " + str(orsen_response))
            
            #user_input = get_input()
            #if user_input.lower() in IS_AFFIRM:
                #print(orsen.repeat_story())

    else:
        print('user attempting to start')


        

    #save story world
    #else:
        #try:
            #Pickle.pickle_world_wb(pickle_filepath, orsen.world.get_pickled_world())
        #except Exception as e:
            #Logger.log_conversation("ERROR: " + str(e))

        #print("=========================================================")
        #print("LLBOT" + ": " + "Do you want to make another story?")
        #rint("=========================================================")
        #user_input = get_input()
        #if user_input.lower() in IS_DENY:
            #is_engaged = False

bot.polling()