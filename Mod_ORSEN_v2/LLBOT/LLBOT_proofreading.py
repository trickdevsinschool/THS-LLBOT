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

def call(txt,studentid):
    lt = languagetool.languagetool()
    td = topicDetector.topicDetector()
    grader= grades.grades("yes", studentid)
    isSVA= 0
    isOOA=0

    # tdResponse = td.startTD(txt)
    # ltResponse = lt.startLT(txt)
    # svaResponse = td.SVA(txt)
    # ooaResponse = td.OOA(txt)

    if td.SVA(txt) is 0: #if SVA is detected
        ltResponse = lt.startLT(txt)
        isSVA=1

    elif td.OOA(txt) is 0: #if OOA is detected
        ltResponse = lt.startLT(txt)
        isOOA=1
    else: #no topics detected, continue
        print("=========================================================")
        print("YOU ARE IN NO TOPICS DETECTED")
        print("=========================================================")
        return 0

    #check error through lt
    if ltResponse is 0: #no error
        if isSVA==1:
            grader.inc_Score(studentid,"1")
            isSVA=0
        elif isOOA==1:
            grader.inc_Score(studentid,"2")
            isOOA=0

        return 0
    else: #there were errors detected
        print("=========================================================")
        print("ERRORS MATCHED")
        print("=========================================================")
        currmsg= lt.getmsg()
        currdesc =lt.getdesc()
        currrule= lt.getrule()
        currrep=lt.getrep()
        curroffset= lt.getoffset()
        currlength= lt.getlength()
        
        correction_response.start(currmsg,currdesc,currrule,currrep,curroffset,currlength,txt)
        if isSVA==1:
            grader.dec_Score(studentid,1)
            isSVA=0
        elif isOOA==1:
            grader.dec_Score(studentid,2)
            isOOA=0
    
    # if ltResponse is 0: #NO ERROR; check which topic applies for grading and continue to ORSEN
    #     #TO CHECK WHICH TOPICS ARE APPLICABLE FOR GRADING
    #     td.SVA(txt)
    #     td.OOA(txt)
    #     #td.DOA(txt)
        
    #     return 0
    # else: #WITH ERROR
        #lt.errorDetector(txt)
         
    