from LLBOT.proofreadingmodule import languagetool
from LLBOT.proofreadingmodule import topicDetector
from LLBOT import correction_response
from LLBOT.studentmodel import grades

currmsg=""
currrule=""
currdesc=""
currrep=""
curroffset=""
currlength=""
level=""
score=""
lessonID=""


class LLBOT_proofreading:
    studentid=""
    correction_response_ob= correction_response.correction_response()
    

    def detectSVA(self,txt,td):
        if td.SVA(txt) is 0: 
            return 1 #SVA is detected               
        else:
            return 0      
                

    def detectOOA(self,txt,td):
        if td.OOA(txt) is 0: 
            return 1 #OOA is detected               
        else:
            return 0 

    def detectDOA(self,txt,td):
        if td.DOA(txt) is 0: 
            return 1 #OOA is detected               
        else:
            return 0 

    def call(self,txt,studentid,bot,message):
        lt = languagetool.languagetool()
        td = topicDetector.topicDetector()
        grader= grades.grades('n', studentid)
        isSVA = 0
        isOOA = 0
        lessonID= grader.getcurr_lesson(studentid) #returns lessonID, datatype int, 1=SVA 2=OOA 3=DOA
        level= grader.getcurr_level(studentid,lessonID) #returns level, datatype string, Beginner Intermediate Expert


        # tdResponse = td.startTD(txt)
        # ltResponse = lt.startLT(txt)
        # svaResponse = td.SVA(txt)
        # ooaResponse = td.OOA(txt)
        if lessonID==1:
            evaluationSVA= self.detectSVA(txt,td) #DETECT IF IT HAS SVA
            haserror=0
            if evaluationSVA==1: #FOUND SVA
                ltResponse,ltrule = lt.startLT(txt)
                if ltResponse==1 and ltrule== "SINGULAR_NOUN_VERB_AGREEMENT" or ltrule == "HE_VERB_AGR" or ltrule == "IT_VBZ" or ltrule == "PERS_PRONOUN_AGREEMENT":#ERROR
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID,bot,message)
                    grader.dec_Score(studentid,1)
                    haserror=1
                elif ltResponse==0:#NO ERROR
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,1,bot,message)
                    haserror=0
            else:          #NO SVA FOUND
                print("=========================================================")
                print("YOU ARE IN NO TOPICS DETECTED")
                print("=========================================================")
                haserror=0
            return haserror

        elif lessonID==2:
            evaluationOOA= self.detectOOA(txt,td)
            evaluationSVA= self.detectSVA(txt,td)
            haserror=0
            if evaluationOOA==1 and evaluationSVA==0:
                ltResponse,ltrule = lt.startLT(txt)
                if ltResponse==1 and ltrule=="EN_ADJ_ORDER":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID,bot,message)
                    grader.dec_Score(studentid,2)
                    haserror=1
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,2,bot,message) 
                    haserror=0
                else:
                    haserror=0

            elif evaluationOOA==1 and evaluationSVA==1:
                ltResponse,ltrule=lt.startLT(txt)
                if ltResponse==1 and ltrule== "EN_ADJ_ORDER":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID,bot,message)
                    grader.dec_Score(studentid,2)
                    haserror=1
                elif ltResponse==1 and ltrule== "SINGULAR_NOUN_VERB_AGREEMENT" or ltrule == "HE_VERB_AGR" or ltrule == "IT_VBZ" or ltrule == "PERS_PRONOUN_AGREEMENT":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,1,bot,message)
                    grader.dec_Score(studentid,1)
                    haserror=1
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,1,bot,message)
                    grader.inc_Score(studentid,2,bot,message)
                    haserror=0
                else:
                    haserror=0
            elif evaluationOOA==0 and evaluationSVA==1:
                print("IT ENTERED HERE")
                ltResponse, ltrule =lt.startLT(txt)
                if ltResponse==1 and ltrule=="SINGULAR_NOUN_VERB_AGREEMENT" or ltrule == "HE_VERB_AGR" or ltrule == "IT_VBZ" or ltrule == "PERS_PRONOUN_AGREEMENT":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,1,bot,message)
                    grader.dec_Score(studentid,1)
                    haserror=1
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,1,bot,message)
                    haserror=0
                else:
                    haserror=0
            
            elif evaluationOOA==0 and evaluationSVA==0:
                print("=========================================================")
                print("YOU ARE IN NO TOPICS DETECTED")
                print("=========================================================")
                haserror=0
            
            return haserror


        elif lessonID==3:
            haserror=0
            evaluationDOA= self.detectDOA(txt,td)
            print("evaluationDOA"+str(evaluationDOA))
            evaluationOOA= self.detectOOA(txt,td)
            print("evaluationOOA"+str(evaluationOOA))
            evaluationSVA= self.detectSVA(txt,td)
            print("evaluationSVA"+str(evaluationSVA))

            if evaluationDOA==1 and evaluationOOA==0 and evaluationSVA==0:
                ltResponse,ltrule = lt.startLT(txt)
                if ltResponse==1 and ltrule== "SUPERLATIVE_THAN" or ltrule=="THE_WORSE_OF" or ltrule=="COMPARATIVE_THAN" or ltrule=="DIFFICULT_THAN":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID,bot,message)
                    grader.dec_Score(studentid,3)
                    haserror=1
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,3,bot,message) 
                    haserror=0
            elif evaluationDOA==0 and evaluationOOA==1 and evaluationSVA==0:
                ltResponse,ltrule = lt.startLT(txt)
                if ltResponse==1 and ltrule == "EN_ADJ_ORDER":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,2,bot,message)
                    grader.dec_Score(studentid,2)
                    haserror=1
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,2,bot,message) 
                    haserror=0
            elif evaluationDOA==0 and evaluationOOA==0 and evaluationSVA==1:
                ltResponse,ltrule = lt.startLT(txt)
                if ltResponse==1 and ltrule== "SINGULAR_NOUN_VERB_AGREEMENT" or ltrule == "HE_VERB_AGR" or ltrule == "IT_VBZ" or ltrule == "PERS_PRONOUN_AGREEMENT":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,1,bot,message)
                    grader.dec_Score(studentid,1)
                    haserror=1
                    
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,1,bot,message)
                    haserror=0
            elif evaluationDOA==0 and evaluationOOA==1 and evaluationSVA==1:
                ltResponse,ltrule=lt.startLT(txt)
                if ltResponse==1 and ltrule== "EN_ADJ_ORDER":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,2,bot,message)
                    grader.dec_Score(studentid,2)
                    haserror=1
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,2,bot,message)
                    grader.inc_Score(studentid,1,bot,message)
                    haserror=0
                elif ltResponse==1 and ltrule== "SINGULAR_NOUN_VERB_AGREEMENT" or ltrule == "HE_VERB_AGR" or ltrule == "IT_VBZ" or ltrule == "PERS_PRONOUN_AGREEMENT":
                    print("=========================================================")
                    print("ERRORS MATCHED")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,1,bot,message)
                    grader.dec_Score(studentid,1)
                    haserror=0
                
            elif evaluationDOA==1 and evaluationOOA==0 and evaluationSVA==1:
                ltResponse,ltrule= lt.startLT(txt)
                if ltResponse==1 and ltrule== "SUPERLATIVE_THAN" or ltrule=="THE_WORSE_OF" or ltrule=="COMPARATIVE_THAN" or ltrule=="DIFFICULT_THAN":
                    print("=========================================================")
                    print("ERRORS MATCHED SITUATION 1")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,3,bot,message)
                    grader.dec_Score(studentid,3)
                    haserror=1
                elif ltResponse==0:
                    print("=========================================================")
                    print("NO ERRORS")
                    print("=========================================================")
                    grader.inc_Score(studentid,3,bot,message)
                    grader.inc_Score(studentid,1,bot,message)
                    haserror=0
                elif ltResponse==1 and ltrule=="SINGULAR_NOUN_VERB_AGREEMENT" or ltrule == "HE_VERB_AGR" or ltrule == "IT_VBZ" or ltrule == "PERS_PRONOUN_AGREEMENT":
                    print("=========================================================")
                    print("ERRORS MATCHED SITUATION 2")
                    print("=========================================================")
                    currmsg= lt.getmsg()
                    currdesc= lt.getdesc()
                    currrule= lt.getrule()
                    currrep=lt.getrep()
                    curroffset= lt.getoffset()
                    currlength= lt.getlength()
                    self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,1,bot,message)
                    grader.dec_Score(studentid,1)
                    haserror=1
                else:
                    haserror=1
            elif evaluationDOA==1 and evaluationOOA==1 and evaluationSVA==1:
                    ltResponse,ltrule= lt.startLT(txt)
                    if ltResponse==1 and ltrule== "SUPERLATIVE_THAN" or ltrule=="THE_WORSE_OF" or ltrule=="COMPARATIVE_THAN" or ltrule=="DIFFICULT_THAN":
                        print("=========================================================")
                        print("ERRORS MATCHED")
                        print("=========================================================")
                        currmsg= lt.getmsg()
                        currdesc= lt.getdesc()
                        currrule= lt.getrule()
                        currrep=lt.getrep()
                        curroffset= lt.getoffset()
                        currlength= lt.getlength()
                        self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,3,bot,message)
                        grader.dec_Score(studentid,3)
                        haserror=1
                    elif ltResponse==1 and ltrule== "EN_ADJ_ORDER":
                        print("=========================================================")
                        print("ERRORS MATCHED")
                        print("=========================================================")
                        currmsg= lt.getmsg()
                        currdesc= lt.getdesc()
                        currrule= lt.getrule()
                        currrep=lt.getrep()
                        curroffset= lt.getoffset()
                        currlength= lt.getlength()
                        self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID,bot,message)
                        grader.dec_Score(studentid,2)
                        haserror=1
                    elif ltResponse==1 and ltrule== "SINGULAR_NOUN_VERB_AGREEMENT" or ltrule == "HE_VERB_AGR" or ltrule == "IT_VBZ" or ltrule == "PERS_PRONOUN_AGREEMENT":
                        print("=========================================================")
                        print("ERRORS MATCHED")
                        print("=========================================================")
                        currmsg= lt.getmsg()
                        currdesc= lt.getdesc()
                        currrule= lt.getrule()
                        currrep=lt.getrep()
                        curroffset= lt.getoffset()
                        currlength= lt.getlength()
                        self.correction_response_ob.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID,bot,message)
                        grader.dec_Score(studentid,1)
                        haserror=1
                    elif ltResponse==0:
                        print("=========================================================")
                        print("NO ERRORS")
                        print("=========================================================")
                        grader.inc_Score(studentid,3,bot,message)
                        grader.inc_Score(studentid,1,bot,message)
                        grader.inc_Score(studentid,2,bot,message)
                        haserror=0 

                    
            
            
            return haserror



        
         
        



        
        

    #elif td.OOA(txt) is 0: #if OOA is detected
        #ltResponse = lt.startLT(txt)
        #isOOA=1
    #elif td.DOA(txt) is 0: #if DOA is detected
        #ltResponse = lt.startLT(txt)
    #else: #no topics detected, continue
        
        #return 0

    #check error through lt
    
            #isSVA=0
        #elif isOOA==1:
            #grader.inc_Score(studentid,"2")
            #isOOA=0
        #return 0
    #else: #there were errors detected
        
        #if isSVA==1:
            #grader.dec_Score(studentid,1)
            #isSVA=0
        #elif isOOA==1:
            #grader.dec_Score(studentid,2)
            #isOOA=0
    
    # if ltResponse is 0: #NO ERROR; check which topic applies for grading and continue to ORSEN
    #     #TO CHECK WHICH TOPICS ARE APPLICABLE FOR GRADING
    #     td.SVA(txt)
    #     td.OOA(txt)
    #     #td.DOA(txt)
        
    #     return 0
    # else: #WITH ERROR
        #lt.errorDetector(txt)
         

