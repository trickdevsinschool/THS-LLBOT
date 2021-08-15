import requests
import spacy
from spacy.symbols import amod, nsubj, VERB, ADJ, conj, acomp, ADV, advmod, SCONJ, prep

URL = ""
API_KEY = ""
USERNAME = ""
txt = ""
nlp = spacy.load("en_core_web_sm")
adjCtr = 0

#IF INPUT HAS NO MATCHES, THIS CLASS CHECKS WHICH TOPICS ARE APPLICABLE FOR GRADING USING SPACY
class topicDetector():

    def __init__(self): #initializes everything
        self.URL = 'https://api.languagetoolplus.com/v2/check'
        self.API_KEY = '68a78e9628562f69'
        self.USERNAME = 'jan_silverio@dlsu.edu.ph'

    # def startTD(self, txt):
    #     if SVA(self, txt) is 0:
    #         print("CURRENT TOPIC IS SVA")
    #         return 0
    #     elif OOA(self, txt) is 0:
    #         print("CURRENT TOPIC IS OOA")
    #         return 0
    #     else:
    #         print("no topic")
    
    def SVA(self, txt):
        doc = nlp(txt)
        for possible_subject in doc:
            if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
                print("=========================================================")
                print('Complies with SVA between subject ' + possible_subject.text + ' and verb ' + possible_subject.head.text)
                print("=========================================================")
                return 0

    def OOA(self, txt):
        ctr = 0
        doc = nlp(txt)
        List = []

        for possible_adj in doc:
            if (possible_adj.dep == amod or possible_adj.dep == conj or possible_adj.dep == acomp) and possible_adj.pos == ADJ and possible_adj.tag_ == "JJ":
                ctr+=1
                List.insert(ctr, possible_adj.text)

        if ctr > 1:
            print(List)
            print("ADDED ADJ")
            #LIST OF ADJECTIVES ARE CONSIDERED OOA (HAS TO BE MORE THAN ONE)
            #CAN CONTTINUE FROM HERE
        # elif ctr == 1:
        #     DOA(txt)
            return 0

    def DOA(self, txt):
        count = 0
        doc = nlp(txt)
        for possible_adj in doc:
        
            if possible_adj.tag == "JJ" or possible_adj.tag_ == "JJR" or possible_adj.tag_ == "JJS": # JJR comparative / JJS superlative
                print("=========================================================")
                print("DOA comparative/superlative adj: " + possible_adj.text)
                print("=========================================================")
                return 0
            elif (possible_adj.dep == amod or possible_adj.dep == conj or possible_adj.dep == acomp) and possible_adj.pos == ADJ and possible_adj.tag_ == "JJ": # JJ positive
                count+=1
                if count == 1:
                    print("=========================================================")
                    print("DOA positive adj: " + possible_adj.text)
                    print("=========================================================")
                    return 0
