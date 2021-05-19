import requests
import spacy
from spacy.symbols import amod, nsubj, VERB, ADJ, conj, acomp, ADV, advmod

URL = ""
API_KEY = ""
USERNAME = ""
txt = ""

currmsg=""
currrule=""
currdesc=""
currrep=""
curroffset=""
currlength=""

#THIS CLASS CHECKS IF THERE IS AN ERROR OR NOT & WHAT TYPE OF ERROR USING LANGUAGE TOOL
class languagetool():

    def __init__(self): #initializes everything
        self.URL = 'https://api.languagetoolplus.com/v2/check'
        self.API_KEY = 'da2d621e9db94f61'
        self.USERNAME = 'patricknarvasa19@gmail.com'

    def startLT(self, txt):
        self.txt = txt
        params = {'username': self.USERNAME,'apiKey': self.API_KEY, 'text': self.txt, 'language':'en-US'}
        response = requests.post(url = self.URL, params=params)

        data = response.json()

        if(len(data['matches']) == 0): #IF NO ERROR
            print("YOU ARE IN NO ERROR")
            return 0," "

        else: #THERE IS AN ERROR
            print("YOU ARE IN ERROR")

            msg = data['matches'][0]['message']
            rule = data['matches'][0]['rule']['id']
            desc = data['matches'][0]['rule']['description']
            rep = data['matches'][0]['replacements'][0]['value']
            offset= int(data['matches'][0]['offset'])
            length = int(data['matches'][0]['length'])
            self.setCorrectionParam(msg,rule,desc,rep,offset,length)

            #can add DB response for Indirect/Direct Correction here
            print()
            print("=========================================================")
            print('String violates the rule ' + rule)
            print('Note: ' + msg)
            print('Try: ' + rep)
            print("=========================================================")

            #Add detector for which type of error to -1 in grades
            words = rule.split()

            if rule == "SINGULAR_NOUN_VERB_AGREEMENT":
                print("YOU ARE IN SVA ERROR -1")
            elif rule == "EN_ADJ_ORDER":
                print("YOU ARE IN OOA ERROR -1")
            elif "superlatives" or "superlative" or "comparative" or "comparatives" in words:
                print("YOU ARE IN DOA ERROR -1")
            return 1,rule
        
    # def errorDetector(self, txt):
    #     self.txt = txt
    #     params = {'username': self.USERNAME,'apiKey': self.API_KEY, 'text': self.txt, 'language':'en-US'}
    #     response = requests.post(url = self.URL, params=params)

    #     data = response.json()
    
    #     msg = data['matches'][0]['message']
    #     rule = data['matches'][0]['rule']['id']
    #     desc = data['matches'][0]['rule']['description']
    #     rep = data['matches'][0]['replacements'][0]['value']
    #     self.setCorrectionParam(msg,rule,desc,rep)

    #     #can add DB response for Indirect/Direct Correction here
    #     print()
    #     print("=========================================================")
    #     print('String violates the rule ' + rule)
    #     print('Note: ' + msg)
    #     print('Try: ' + rep)
    #     print("=========================================================")

    #     #Add detector for which type of error to -1 in grades
    #     words = rule.split()

    #     if rule == "SINGULAR_NOUN_VERB_AGREEMENT":
    #         print("YOU ARE IN SVA ERROR -1")
    #     elif rule == "EN_ADJ_ORDER":
    #         print("YOU ARE IN OOA ERROR -1")
    #     elif "superlatives" or "superlative" or "comparative" or "comparatives" in words:
    #         print("YOU ARE IN DOA ERROR -1")


    def setCorrectionParam(self,msg,rule,desc,rep,offset,length):
        self.currmsg= msg
        self.currrule= rule
        self.currdesc=desc
        self.currrep=rep
        self.curroffset= offset
        self.currlength= length
    
    def getmsg(self):
        return self.currmsg
    def getrule(self):
        return self.currrule
    def getdesc(self):
        return self.currdesc
    def getrep(self):
        return self.currrep
    def getoffset(self):
        return self.curroffset
    def getlength(self):
        return self.currlength