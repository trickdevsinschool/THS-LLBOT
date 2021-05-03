import requests
import spacy
from spacy.symbols import amod, nsubj, VERB, ADJ, conj, acomp

URL = ""
API_KEY = ""
USERNAME = ""
txt = ""
nlp = spacy.load("en_core_web_sm")

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
                print("+1 FOR SVA")
                print("=========================================================")
                return 0

    def OOA(self, txt):
        doc = nlp(txt)
        # print("=========================================================")
        # print('Adjectives in compliance with OOA: ')
        for possible_adj in doc:
            if (possible_adj.dep == amod or possible_adj.dep == conj or possible_adj.dep == acomp) and possible_adj.pos == ADJ:
                print(possible_adj.text)
                # print("+1 FOR OOA")
                # print("=========================================================")
            # elif possible_adj.dep == nummod and possible_adj.head.pos == ADJ:
            #     print('try')
                return 0
