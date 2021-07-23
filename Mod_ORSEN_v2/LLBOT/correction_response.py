from .correctionmodule import annoyanceChecker
from .correctionmodule import directCorrection as DC
from .correctionmodule import indirectCorrection as IC

def start(msg,desc,rule,rep,offset,length,txt,level,lessonID,bot,message):

    print("ENTERED CORRECTION RESPONSE")
    correction=1#annoyanceChecker.check(level)

    if correction== 0:
        DC.start(msg,desc,rule,rep,offset,length,txt,bot,message)

    elif correction== 1:
        IC.start(msg,desc,rule,rep,offset,length,txt,level,lessonID,bot,message)
        

        