import nltk
from nltk.corpus import wordnet
from time import time

nltk.download('wordnet')



def isEnglish(sline):
    if ( sline[0].isalpha() and sline[1].isalpha() and wordnet.synsets(sline[0]) and wordnet.synsets(sline[1]) ):
        return True
    return False


f = open("/home/sergio/Topicos/Corpusgoogle/fieleseng/2gm-0031.eng" ,"w")
to_read = open("/home/sergio/Topicos/Corpusgoogle/corpus de google-20200508T221219Z-001/corpus de google/2gm-0031", "r")

line = to_read.readline()[:-1]  # Elimina el salto de linea

time_start = time()
# cont = 0
while(line):
    sline = line.split()    #tokens
    if(isEnglish(sline)):
        for w in sline:
            f.write(w + '\t')
        f.write('\n')
    line = to_read.readline()[:-1]
    # cont+=1
    # if(cont%100 == 0):
    #     print(cont)
final_time = time()
tiempo_ejecucion = final_time - time_start
print ('El tiempo de ejecucion fue: ', tiempo_ejecucion)