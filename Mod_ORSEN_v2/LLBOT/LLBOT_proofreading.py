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


def detectSVA(txt,td):
    if td.SVA(txt) is 0: 
        return 1 #SVA is detected               
    else:
        return 0      
            

def detectOOA(txt,td):
    if td.OOA(txt) is 0: 
        return 1 #OOA is detected               
    else:
        return 0 

def detectDOA(txt,td):
    if td.DOA(txt) is 0: 
        return 1 #OOA is detected               
    else:
        return 0 

def call(txt,studentid):
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
        evaluationSVA= detectSVA(txt,td) #DETECT IF IT HAS SVA
        if evaluationSVA==1: #FOUND SVA
            ltResponse,ltrule = lt.startLT(txt)
            if ltResponse==1:#ERROR
                print("=========================================================")
                print("ERRORS MATCHED")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"1")
                return 1
            elif ltResponse==0:#NO ERROR
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                grader.inc_Score(studentid,"1")
                return 0
        else:          #NO SVA FOUND
            print("=========================================================")
            print("YOU ARE IN NO TOPICS DETECTED")
            print("=========================================================")
            return 0

    elif lessonID==2:
        evaluationOOA= detectOOA(txt,td)
        evaluationSVA= detectSVA(txt,td)
        if evaluationOOA==1 and evaluationSVA==0:
            ltResponse,ltrule = lt.startLT(txt)
            if ltResponse==1:
                print("=========================================================")
                print("ERRORS MATCHED")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"2")
                return 1
            elif ltResponse==0:
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                grader.inc_Score(studentid,"2") 
                return 0

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
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"2")
                return 1
            elif ltResponse==0 and ltrule== "EN_ADJ_ORDER":
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.inc_Score(studentid,"2")
                return 0
            if ltResponse==1 and ltrule== "SINGULAR_NOUN_VERB_AGREEMENT":
                print("=========================================================")
                print("ERRORS MATCHED")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"1")
                return 1
            elif ltResponse==0 and ltrule== "SINGULAR_NOUN_VERB_AGREEMENT":
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.inc_Score(studentid,"1")
                return 0
        elif evaluationOOA==0 and evaluationSVA==1:
            ltResponse, ltrule =lt.startLT(txt)
            if ltResponse==1:
                print("=========================================================")
                print("ERRORS MATCHED")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"1")
                return 1
            elif ltResponse==0:
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                grader.inc_Score(studentid,"1")
                return 0
        
            
        elif evaluationOOA==0 and evaluationSVA==0:
            print("=========================================================")
            print("YOU ARE IN NO TOPICS DETECTED")
            print("=========================================================")
            return 0


    elif lessonID==3:
        evaluationDOA= detectDOA(txt,td)
        evaluationOOA= detectOOA(txt,td)
        evaluationSVA= detectSVA(txt,td)
        if evaluationDOA==1 and evaluationOOA==0 and evaluationSVA==0:
            ltResponse,ltrule = lt.startLT(txt)
            if ltResponse==1:
                print("=========================================================")
                print("ERRORS MATCHED")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"3")
            elif ltResponse==0:
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                grader.inc_Score(studentid,"3") 
        elif evaluationDOA==0 and evaluationOOA==1 and evaluationSVA==0:
            ltResponse,ltrule = lt.startLT(txt)
            if ltResponse==1:
                print("=========================================================")
                print("ERRORS MATCHED")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"2")
            elif ltResponse==0:
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                grader.inc_Score(studentid,"2") 
        elif evaluationDOA==0 and evaluationOOA==0 and evaluationSVA==1:
            ltResponse,ltrule = lt.startLT(txt)
            if ltResponse==1:
                print("=========================================================")
                print("ERRORS MATCHED")
                print("=========================================================")
                currmsg= lt.getmsg()
                currdesc= lt.getdesc()
                currrule= lt.getrule()
                currrep=lt.getrep()
                curroffset= lt.getoffset()
                currlength= lt.getlength()
                correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt,level,lessonID)
                grader.dec_Score(studentid,"1")
            elif ltResponse==0:
                print("=========================================================")
                print("NO ERRORS")
                print("=========================================================")
                grader.inc_Score(studentid,"1") 
        



        
        

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
         

