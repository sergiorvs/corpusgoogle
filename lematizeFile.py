import nltk
from nltk.stem import WordNetLemmatizer
from time import time
import os


nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

entries = os.listdir('fieleseng/')
for f_name in entries:
    to_read = open("/home/sergio/Topicos/Corpusgoogle/fieleseng/"+f_name,"r")
    new_name = f_name[:-3]+"lem"
    f = open("/home/sergio/Topicos/Corpusgoogle/filesLem/"+new_name,"w")
    print(new_name)

    line = to_read.readline()[:-1]  # Elimina el salto de linea
    time_start = time()
    while(line):
        sline = line.split()    #tokens
        for w in sline:
            actualWord = w.lower()
            lemWord = lemmatizer.lemmatize(actualWord, pos="v") # Lematiza Sustantivos
            if(actualWord == lemWord):
                lemWord = lemmatizer.lemmatize(lemWord, pos="n")    # Lematiza Verbos
            f.write(lemWord + '\t')
        f.write('\n')
        line = to_read.readline()[:-1]
        # cont+=1
        # if(cont%100 == 0):
        #     print(cont)

    final_time = time()
    tiempo_ejecucion = final_time - time_start
    print ('El tiempo de ejecucion para ', new_name,'fue: ', tiempo_ejecucion)


    to_read.close()
    f.close()


# f = open("2gm-0010.lem", "w")
# to_read = open("2gm-0010.eng", "r")


# line = to_read.readline()[:-1]  # Elimina el salto de linea

# time_start = time()
# # cont = 0
# while(line):
#     sline = line.split()    #tokens
#     for w in sline:
#         actualWord = w.lower()
#         lemWord = lemmatizer.lemmatize(actualWord, pos="v") # Lematiza Sustantivos
#         if(actualWord == lemWord):
#             lemWord = lemmatizer.lemmatize(lemWord, pos="n")    # Lematiza Verbos
#         f.write(lemWord + '\t')
#     f.write('\n')
#     line = to_read.readline()[:-1]
#     # cont+=1
#     # if(cont%100 == 0):
#     #     print(cont)

# final_time = time()
# tiempo_ejecucion = final_time - time_start
# print ('El tiempo de ejecucion fue: ', tiempo_ejecucion)

