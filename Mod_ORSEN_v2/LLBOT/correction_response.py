from .correctionmodule import annoyanceChecker
from .correctionmodule import directCorrection as DC
from .correctionmodule import indirectCorrection as IC
import regex

class correction_response:
    IC_counter=0

    def start(self,msg,desc,rule,rep,offset,length,txt,level,lessonID,bot,message):

        print("ENTERED CORRECTION RESPONSE")
        count= self.IC_counter
        print("IC_counter:" + str(count))
        if self.IC_counter==3:
            correction=0
            self.IC_counter=0
            print("Correction Sensitivity Initiated")
        else:
            correction= annoyanceChecker.check(level)

        if correction== 0:
            DC.start(msg,desc,rule,rep,offset,length,txt,bot,message)

        elif correction== 1:
            IC.start(msg,desc,rule,rep,offset,length,txt,level,lessonID,bot,message)
            self.IC_counter+=1
            
    def start_ooa(self,msg,desc,rule,rep,offset,length,txt,level,lessonID,bot,message,indices):

        print("ENTERED CORRECTION RESPONSE")
        count= self.IC_counter
        print("IC_counter:" + str(count))
        if self.IC_counter==3:
            correction=0
            self.IC_counter=0
            print("Correction Sensitivity Initiated")
        else:
            correction= annoyanceChecker.check(level)

        if correction== 0:
            DC.start(msg,desc,rule,rep,offset,length,txt,bot,message)

        elif correction== 1:
            IC.start(msg,desc,rule,rep,offset,length,txt,level,lessonID,bot,message,indices)
            self.IC_counter+=1

        