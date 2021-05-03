import requests
import spacy
from spacy.symbols import amod, nsubj, VERB, ADJ, conj, acomp

URL = ""
API_KEY = ""
USERNAME = ""
txt = ""

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
            # doc = nlp(txt)
            # token = doc[1]
            # for token in doc:
            #     print(token, token.pos_, token.dep_)
            # print()

            # SVA(txt)
            # OOA(txt)
            print("YOU ARE IN NO ERROR")
            return 0

        else: #THERE IS AN ERROR
            print("YOU ARE IN ERROR")
            return 1
        
    def errorDetector(self, txt):
        self.txt = txt
        params = {'username': self.USERNAME,'apiKey': self.API_KEY, 'text': self.txt, 'language':'en-US'}
        response = requests.post(url = self.URL, params=params)

        data = response.json()
    
        msg = data['matches'][0]['message']
        rule = data['matches'][0]['rule']['id']
        desc = data['matches'][0]['rule']['description']
        rep = data['matches'][0]['replacements'][0]['value']

        print()
        print("=========================================================")
        #can add DB response for Indirect/Direct Correction here
        print('String violates the rule ' + rule)
        print('Note: ' + msg)
        print('Try: ' + rep)
        print("=========================================================")
