from time import time

import pickle
import numpy as np
import bisect
from scipy import spatial

#result = 1 - spatial.distance.cosine(dataSetI, dataSetII)


SIZE = 75000

def createOcurrArray(positions, size=SIZE):
    # vec = np.zeros(size,dtype=int)
    vec = [0]*size
    for p in positions:
        # print(p)
        vec[p[0]] = p[1]
    return vec

def compareVectors(theDict, word):
    positions = theDict[word]
    keys = theDict.keys()
    vect1 = createOcurrArray(positions, SIZE)

    allPorcentages = []
    cont=1
    for k in keys:
        if cont%100 == 0: 
            print(cont, " of ", len(keys))
        cont+=1
        pos = theDict[k]
        vect2 = createOcurrArray(pos,SIZE)

        # result = np.dot(vect1, vect2) / (np.sqrt(np.dot(vect1,vect2)) * np.sqrt(np.dot(vect1,vect2)))
        result = 1-spatial.distance.cosine(vect1, vect2)
        bisect.insort(allPorcentages, (result, k))

    return allPorcentages

def getNumeratorOf(listA, listB):
    sum = 0
    for a in listA:
        for b in listB:
            if a[0]==b[0]:
                sum += a[1]*b[1]
    return sum

def cuadraticSum(_list):
    res = 0
    for i in _list:
        res += i[1]**2
    return res

def getDenominatorOf(listA, listB):
    a = cuadraticSum(listA)**(1/2)
    b = cuadraticSum(listB)**(1/2)
    return a*b

def softCosine(listA, listB):
    num = getNumeratorOf(listA,listB)
    den = getDenominatorOf(listA, listB)
    return num/den

def compareAll(dbw, word):
    keys = dbw.keys()
    a = dbw[word]
    da = cuadraticSum(a)**(1/2)

    theList = []
    for k in keys:
        b = dbw[k]
        num = getNumeratorOf(a,b)
        db = cuadraticSum(b)**(1/2)

        softCos = num/(da*db)
        bisect.insort(theList, (softCos, k))

    return theList[100:]





if __name__ == '__main__':
    afile = open('dbWeight29', 'rb')
    # afile = open('dbWeight', 'rb')
    dbw = pickle.load(afile)
    afile.close()

    print("comenzando")
    keys = dbw.keys()
    print("similarity between apple")
    
    time_start = time()
    # print(softCosine(dbw['cat'], dbw['box']))
    c = compareVectors(dbw, 'apple')
    c.reverse()
    print(c[:50])

    # print(compareAll(dbw,'cat'))
    tiempo_ejecucion = time() - time_start
    print ('El tiempo de ejecucion fue: ', tiempo_ejecucion)


    # a = createOcurrArray(dbw['cat'])
    # b = createOcurrArray(dbw['box'])
    # print(a)
    # print(b)

    # time_start = time()
    # res = 1.0 - spatial.distance.cosine(a, b)
    # print(res)
    # tiempo_ejecucion = time() - time_start
    # print ('El tiempo de ejecucion fue: ', tiempo_ejecucion)


    # a = [(8,0.13),(15,0.14),(18,0.8)]
    # b = [(8,0.7),(12,0.73),(15,0.41)]
    # print(softCosine(a,b))    