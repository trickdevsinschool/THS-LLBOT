from .correctionmodule import annoyanceChecker
from .correctionmodule import directCorrection as DC
from .correctionmodule import indirectCorrection as IC

def start(msg,desc,rule,rep,offset,length,txt,level,lessonID):

    print("ENTERED CORRECTION RESPONSE")
    correction=annoyanceChecker.check("Beginner")

    if correction== 0:
        DC.start(msg,desc,rule,rep,offset,length,txt)

    elif correction== 1:
        IC.start(msg,desc,rule,rep,offset,length,txt,level,lessonID)
        

        