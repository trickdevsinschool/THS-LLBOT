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
        self.API_KEY = '68a78e9628562f69'
        self.USERNAME = 'jan_silverio@dlsu.edu.ph'

    def startLT(self, txt):
        self.txt = txt
        params = {'username': self.USERNAME,'apiKey': self.API_KEY, 'text': self.txt, 'language':'en-US'}
        response = requests.post(url = self.URL, params=params)

        data = response.json()

        if(len(data['matches']) == 0): #IF NO ERROR
            print("YOU ARE IN NO ERROR")
            return 0," "

        elif(len(data['matches']) == 1): #ONLY ONE ERROR
        # else: #THERE IS AN ERROR
            print("YOU ARE IN ERROR")
            rule = data['matches'][0]['rule']['id']
            words = rule.split()
            msg = " "
            desc = " "
            rep = " "
            offset= " "
            length = " "

            if rule == "SINGULAR_NOUN_VERB_AGREEMENT" or rule == "HE_VERB_AGR" or rule == "IT_VBZ" or rule == "PERS_PRONOUN_AGREEMENT": #SVA
                print("YOU ARE IN SVA ERROR -1")
                msg = data['matches'][0]['message']
                desc = data['matches'][0]['rule']['description']
                rep = data['matches'][0]['replacements'][0]['value']
                offset= int(data['matches'][0]['offset'])
                length = int(data['matches'][0]['length'])
                self.setCorrectionParam(msg,rule,desc,rep,offset,length)
                print()
                print("=========================================================")
                print('String violates the rule ' + rule)
                print('Note: ' + msg)
                print('Try: ' + rep)
                print("=========================================================")
                return 1,rule
            elif rule == "EN_ADJ_ORDER": #OOA
                print("YOU ARE IN OOA ERROR -1")
                msg = data['matches'][0]['message']
                desc = data['matches'][0]['rule']['description']
                rep = data['matches'][0]['replacements'][0]['value']
                offset= int(data['matches'][0]['offset'])
                length = int(data['matches'][0]['length'])
                self.setCorrectionParam(msg,rule,desc,rep,offset,length)
                print("YOU ARE IN OOA ERROR -1")
                print()
                print("=========================================================")
                print('String violates the rule ' + rule)
                print('Note: ' + msg)
                print('Try: ' + rep)
                print("=========================================================")
                return 1,rule
            elif rule== "SUPERLATIVE_THAN" or rule=="THE_WORSE_OF" or rule=="COMPARATIVE_THAN" or rule == "DIFFICULT_THAN": #DOA
                # ("superlatives" or "superlative" or "comparative" or "comparatives" in words)
                print("YOU ARE IN DOA ERROR -1")
                msg = data['matches'][0]['message']
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

                return 1,rule
            elif rule!= "SINGULAR_NOUN_VERB_AGREEMENT" or rule!="EN_ADJ_ORDER" or rule!= "SUPERLATIVE_THAN" or rule!="THE_WORSE_OF" or rule!= "COMPARATIVE_THAN": #take note of these two
                print()
                print("=========================================================")
                print('String violates the rule ' + rule)
                print('Note: ' + msg)
                print('Try: ' + rep)
                print("=========================================================")
                return 0," "

        elif(len(data['matches']) > 1): # MORE THAN ONE ERROR
            lenmatch = len(data['matches'])
            print("NUMBER OF ERROR MATCHES: ", lenmatch)

            while lenmatch != 0:
                rule = data['matches'][lenmatch - 1]['rule']['id']
                words = rule.split()
                msg = " "
                desc = " "
                rep = " "
                offset= " "
                length = " "

                if rule == "SINGULAR_NOUN_VERB_AGREEMENT" or rule == "HE_VERB_AGR" or rule == "IT_VBZ" or rule == "PERS_PRONOUN_AGREEMENT": #SVA
                    print("YOU ARE IN SVA ERROR -1")
                    msg = data['matches'][lenmatch - 1]['message']
                    desc = data['matches'][lenmatch - 1]['rule']['description']
                    rep = data['matches'][lenmatch - 1]['replacements'][0]['value']
                    offset= int(data['matches'][lenmatch - 1]['offset'])
                    length = int(data['matches'][lenmatch - 1]['length'])
                    self.setCorrectionParam(msg,rule,desc,rep,offset,length)
                    print()
                    print("=========================================================")
                    print('String violates the rule ' + rule)
                    print('Note: ' + msg)
                    print('Try: ' + rep)
                    print("=========================================================")
                    return 1,rule
                elif rule == "EN_ADJ_ORDER": #OOA
                    print("YOU ARE IN OOA ERROR -1")
                    msg = data['matches'][lenmatch - 1]['message']
                    desc = data['matches'][lenmatch - 1]['rule']['description']
                    rep = data['matches'][lenmatch - 1]['replacements'][0]['value']
                    offset= int(data['matches'][lenmatch - 1]['offset'])
                    length = int(data['matches'][lenmatch - 1]['length'])
                    self.setCorrectionParam(msg,rule,desc,rep,offset,length)
                    print("YOU ARE IN OOA ERROR -1")
                    print()
                    print("=========================================================")
                    print('String violates the rule ' + rule)
                    print('Note: ' + msg)
                    print('Try: ' + rep)
                    print("=========================================================")
                    return 1,rule
                elif rule== "SUPERLATIVE_THAN" or rule=="THE_WORSE_OF" or rule=="COMPARATIVE_THAN" or rule == "DIFFICULT_THAN": #DOA
                    # ("superlatives" or "superlative" or "comparative" or "comparatives" in words)
                    print("YOU ARE IN DOA ERROR -1")
                    msg = data['matches'][lenmatch - 1]['message']
                    desc = data['matches'][lenmatch - 1]['rule']['description']
                    rep = data['matches'][lenmatch - 1]['replacements'][0]['value']
                    offset= int(data['matches'][lenmatch - 1]['offset'])
                    length = int(data['matches'][lenmatch - 1]['length'])
                    self.setCorrectionParam(msg,rule,desc,rep,offset,length)
                    #can add DB response for Indirect/Direct Correction here
                    print()
                    print("=========================================================")
                    print('String violates the rule ' + rule)
                    print('Note: ' + msg)
                    print('Try: ' + rep)
                    print("=========================================================")

                    return 1,rule
                
                
                lenmatch = lenmatch - 1

            if rule!= "SINGULAR_NOUN_VERB_AGREEMENT" or rule!="EN_ADJ_ORDER" or rule!= "SUPERLATIVE_THAN" or rule!="THE_WORSE_OF" or rule!= "COMPARATIVE_THAN"or rule != "DIFFICULT_THAN" or rule != "HE_VERB_AGR" or rule != "IT_VBZ" or rule != "PERS_PRONOUN_AGREEMENT": #take note of these two
                    print()
                    print("=========================================================")
                    print('String violates the rule ' + rule)
                    print('Note: ' + msg)
                    print('Try: ' + rep)
                    print("=========================================================")
                    return 0," "

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