from LLBOT.proofreadingmodule import languagetool
from LLBOT.proofreadingmodule import topicDetector
from LLBOT import correction_response

currmsg=""
currrule=""
currdesc=""
currrep=""

def call(txt):
    lt = languagetool.languagetool()
    td = topicDetector.topicDetector()

    # tdResponse = td.startTD(txt)
    # ltResponse = lt.startLT(txt)
    # svaResponse = td.SVA(txt)
    # ooaResponse = td.OOA(txt)

    if td.SVA(txt) is 0: #if SVA is detected
        ltResponse = lt.startLT(txt)
    elif td.OOA(txt) is 0: #if OOA is detected
        ltResponse = lt.startLT(txt)
    else: #no topics detected, continue
        print("=========================================================")
        print("YOU ARE IN NO TOPICS DETECTED")
        print("=========================================================")
        return 0

    #check error through lt
    if ltResponse is 0: #no error
        return 0
    else: #there were errors detected
        print("=========================================================")
        print("ERRORS MATCHED")
        print("=========================================================")
        
    # if ltResponse is 0: #NO ERROR; check which topic applies for grading and continue to ORSEN
    #     #TO CHECK WHICH TOPICS ARE APPLICABLE FOR GRADING
    #     td.SVA(txt)
    #     td.OOA(txt)
    #     #td.DOA(txt)
        
    #     return 0
    # else: #WITH ERROR
    #     lt.errorDetector(txt)
    #     currmsg= lt.getmsg()
    #     currdesc =lt.getdesc()
    #     currrule= lt.getrule()
    #     currrep=lt.getrep()
    #     correction_response.start(currmsg,currdesc,currrule,currrep)
    
    