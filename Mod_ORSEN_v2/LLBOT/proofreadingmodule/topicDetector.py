import requests
import spacy
from spacy.symbols import amod, nsubj, VERB, ADJ, conj, acomp, ADV, advmod

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
        self.API_KEY = 'da2d621e9db94f61'
        self.USERNAME = 'patricknarvasa19@gmail.com'
    
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
            if (possible_adj.dep == amod or possible_adj.dep == conj or possible_adj.dep == acomp) and possible_adj.pos == ADJ:
                ctr+=1
                List.insert(ctr, possible_adj.text)

        if ctr > 1:
            print(List)
            print("ADDED")
            #LIST OF ADJECTIVES ARE CONSIDERED OOA (MORE THAN ONE)
            #CAN CONTTINUE FROM HERE
        # elif ctr == 1:
        #     DOA(txt)
        return 0

    def DOA(self, txt):
        doc = nlp(txt)
        if possible_adj.dep == advmod and possible_adj.pos == ADJ :
            print("=========================================================")
            print("DOA: " + possible_adj.text)
            print("=========================================================")
            return 0
