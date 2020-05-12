import nltk
from nltk.corpus import wordnet


nltk.download('wordnet')



def isEnglish(sline):
    flag = False
    if ( wordnet.synsets(sline[0]) and wordnet.synsets(sline[1]) ):
        flag = True
    return flag


f = open("file.eng" ,"w")
to_read = open("g1n-001", "r")

line = to_read.readline()[:-1]  # Elimina el salto de linea


while(line):
    sline = line.split()    #tokens
    if(isEnglish(sline)):
        for w in sline:
            f.write(w + '\t')
        f.write('\n')
    line = to_read.readline()[:-1]
