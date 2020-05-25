from django.shortcuts import render
from django.views import View

import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np


# Create your views here.
nltk.download('wordnet')


afile = open('/home/sergio/Topicos/Corpusgoogle/corpusgoogledjango/PROJECT/APP/db03', 'rb')
db = pickle.load(afile)
afile.close()

def takeSecond(elem):
    return elem[1]

def createBooleanArray(positions, size):
    vec = np.zeros(size, dtype=bool)
    for p in positions:
        # print(p)
        vec[p] = 1
    return vec


def compareVectors(word, theDict, size):
    positions = theDict[word]
    keys = theDict.keys()
    vect1 = createBooleanArray(positions, size)

    allPorcentages = []

    for k in keys:
        pos = theDict[k]
        vect2 = createBooleanArray(pos, size)

        # vecRes = np.invert(np.logical_xor(vect1,vect2))
        # concur = np.count_nonzero(vecRes)
        # result = concur/size
        result = (np.logical_and(vect1, vect2)).sum() / float((np.logical_or(vect1, vect2)).sum())
        allPorcentages.append((k, result))
        allPorcentages.sort(key=takeSecond, reverse=True)

    return allPorcentages

class Index(View):
    template_name = "index.html"

    lemmatizer = WordNetLemmatizer()
    context = {}

    def post(self, request):
        text = request.POST.get('my_textarea')
        self.context['txt'] = text
        # print(cleanner(tokens))
        actualword = text.lower()
        lemword = self.lemmatizer.lemmatize(actualword, pos="v")
        if(actualword == lemword):
            lemword = self.lemmatizer.lemmatize(lemword, pos="n")

        all = compareVectors(text, db, 500000)

        self.context['answer'] = all[0:100]
        # print(stems)

        return render(request, self.template_name, self.context)

    def get(self, request):
        return render(request, self.template_name)