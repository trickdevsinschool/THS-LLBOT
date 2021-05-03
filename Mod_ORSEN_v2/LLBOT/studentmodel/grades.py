#set, get , and update grades here

class grades():
    curr_lesson=" " 
    curr_level= " "
    curr_score="0"
    prereq="0"
    def __init__(self,studentid):
       
        self.studentid= studentid #this shouldn't be an assignment, rather it should be finding a match of the studentid in the db
        self.curr_lesson="OOA"
        self.curr_level= "1"
        self.curr_score="0"
        self.prereq="0"
        #TO Broqz: these should be SQL fetches thanks! -Trick 
        
   #additional methods below
   
    def getcurr_lesson(self):
       return self.curr_lesson     