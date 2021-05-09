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

    ltResponse = lt.startLT(txt)
    # svaResponse = td.SVA(txt)
    # ooaResponse = td.OOA(txt)

    if ltResponse is 0: #NO ERROR; check which topic applies for grading and continue to ORSEN
        #TO CHECK WHICH TOPICS ARE APPLICABLE FOR GRADING
        td.SVA(txt)
        td.OOA(txt)
        #td.DOA(txt)
        
        return 0
    else: #WITH ERROR
        lt.errorDetector(txt)
        currmsg= lt.getmsg()
        currdesc =lt.getdesc()
        currrule= lt.getrule()
        currrep=lt.getrep()
        correction_response.start(currmsg,currdesc,currrule,currrep)
    
    