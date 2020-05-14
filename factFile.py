import pickle
from time import time
import os



def saveData(file_name):
    to_read = open(file_name, "r")
    fact = {}
    line = to_read.readline()[:-1]
    while(line):
        sline = line.split()
        w1 = sline[0]
        w2 = sline[1]
        try:
            num = int(sline[2])
        except:
            num = 0

        if w1 in fact:
            if w2 in fact[w1]:
                fact[w1][w2] = str(int(fact[w1][w2]) + num)
            else:
                fact[w1][w2] = str(num)
        else:
            fact[w1] = {}
            fact[w1][w2] = str(num)
        line = to_read.readline()[:-1]

    ###### Para guardar el diccionario en un bitmap
    afile = open('factorizeDict2', 'wb')
    pickle.dump(fact, afile)
    afile.close()

def updateData(file_name, fact):
    to_read = open(file_name, "r")
    line = to_read.readline()[:-1]
    while(line):
        sline = line.split()
        w1 = sline[0]
        w2 = sline[1]
        try:
            num = int(sline[2])
        except:
            num = 0

        if w1 in fact:
            if w2 in fact[w1]:
                fact[w1][w2] = str(int(fact[w1][w2]) + num)
            else:
                fact[w1][w2] = str(num)
        else:
            fact[w1] = {}
            fact[w1][w2] = str(num)
        line = to_read.readline()[:-1]

    ###### Para guardar el diccionario en un bitmap
    afile = open('factorizeDict2', 'wb')
    pickle.dump(fact, afile)
    afile.close()








if __name__ == '__main__':
    entries = os.listdir('filesLem/')
    entries.sort()
    cont = 0
    for f_name in entries:
        file_name = "/home/sergio/Topicos/Corpusgoogle/filesLem/"+f_name
        print("this is the file ", cont)
        time_start = time()
        if(cont == 13):
            saveData(file_name)
        elif(cont > 13):
            afile = open('factorizeDict2', 'rb')
            fact = pickle.load(afile)
            afile.close()
            updateData(file_name, fact)
        cont+=1
        final_time = time()
        tiempo_ejecucion = final_time - time_start
        print ('El tiempo de ejecucion para el archivo ', f_name,' fue: ', tiempo_ejecucion)

    print("todos los archivos fueron almacenados en el diccionario!")
    
    print("escribiendo archivos ...")
    afile = open('factorizeDict2', 'rb')
    fact = pickle.load(afile)
    afile.close()
    f = open("file13-26.fact", "w")
    time_start = time()
    for k in fact.keys():
        w1 = k
        for x in fact[k].keys():
            w2 = x
            num = fact[k][w2]
            f.write(w1 + '\t' + w2 + '\t' + num + '\n')
    
    final_time = time()
    tiempo_ejecucion = final_time - time_start
    print ('El tiempo de ejecucion fue: ', tiempo_ejecucion)
    f.close()















    # f = open("file.fact", "w")

    # file_name = "2gm-0010.lem"
    # # saveData(file_name)

    # ##### Para cargar los datos del diccionario que se encuentran en el fichero
    # afile = open('factorizeDict', 'rb')
    # fact = pickle.load(afile)
    # afile.close()
    # # updateData(file_name, fact)


    # time_start = time()
    # for k in fact.keys():
    #     w1 = k
    #     for x in fact[k].keys():
    #         w2 = x
    #         num = fact[k][w2]
    #         f.write(w1 + '\t' + w2 + '\t' + num + '\n')
    
    # final_time = time()
    # tiempo_ejecucion = final_time - time_start
    # print ('El tiempo de ejecucion fue: ', tiempo_ejecucion)

