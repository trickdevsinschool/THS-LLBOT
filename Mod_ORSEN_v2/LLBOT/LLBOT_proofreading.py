from LLBOT.proofreadingmodule import languagetool
from LLBOT.proofreadingmodule import topicDetector

def call(txt):
    lt = languagetool.languagetool()
    td = topicDetector.topicDetector()

    ltResponse = lt.startLT(txt)
    svaResponse = td.SVA(txt)
    ooaResponse = td.OOA(txt)

    if ltResponse is 0: #NO ERROR; check which topic applies for grading and continue to ORSEN
        if svaResponse is 0:
            print("YOU ARE IN SVA RESPONSE")
        
        if ooaResponse is 0:
            print("YOU ARE IN OOA RESPONSE")

        #Calling the counter for grade can be added here
        return 0
    else: #WITH ERROR
        lt.errorDetector(txt)