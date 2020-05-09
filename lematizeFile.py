import nltk
from nltk.stem import WordNetLemmatizer


nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()


f = open("file.lem", "w")
to_read = open("file.eng", "r")


line = to_read.readline()[:-1]  # Elimina el salto de linea


while(line):
    sline = line.split()    #tokens
    for w in sline:
        actualWord = w.lower()
        lemWord = lemmatizer.lemmatize(actualWord, pos="n") # Lematiza Sustantivos
        if(actualWord == lemWord):
            lemWord = lemmatizer.lemmatize(lemWord, pos="v")    # Lematiza Verbos
        f.write(lemWord + '\t')
    f.write('\n')
    line = to_read.readline()[:-1]

