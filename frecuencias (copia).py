import pickle
import numpy as np


SIZE = 75000


def createBooleanArray(positions):
    vec = np.zeros(SIZE, dtype=bool)
    for p in positions:
        # print(p)
        vec[p[0]] = 1
    return vec


# Ayuda a ordenar vectores de pares tomando su segundo elemento por cada par
def takeSecond(elem):
    return elem[1]

# Encuentra la posicion del elemento en la BD
def find_pos(key, theDict):
    theList = list(theDict.keys())
    if key in theDict:
        return theList.index(key)
    theDict[key] = {}
    return len(theDict)-1


def createOcurrArray(positions, size):
    vec = np.zeros(size,dtype=int)
    for p in positions:
        # print(p)
        vec[p[0]] = p[1]
    return vec

def getVector(arr):
    return [i[0] for i in arr]

def maximos(theDict):
    maxValues = np.zeros(SIZE, dtype=int)
    keys = theDict.keys()

    for k in keys:
        positions = theDict[k]
        vecTem = createOcurrArray(positions,SIZE)
        maxValues = np.maximum(maxValues,vecTem)

    return maxValues


# Divide cada valor entre su maximo para calcular la frecuencia normalizada
def dividirVector(tuplas , maximos):
    res = []
    for t in tuplas:
        aux_t = list(t)
        aux_t[1] /= maximos[t[0]]
        t = tuple(aux_t)
        res.append(t)
    return res


def NormFrec(theDict,maximos):
    keys = theDict.keys()

    for k in keys:
        theDict[k] = dividirVector(theDict[k],maximos)
    
    return theDict



def InvFrecuency(theDict):
    keys = theDict.keys()
    N = len(keys)
    inverseFrecuency = np.zeros(N, dtype=float)
    
    cont = 0
    for k in keys:
        auxArr = createBooleanArray(theDict[k])
        inverseFrecuency[cont] = np.log(SIZE/auxArr.sum())
        cont+=1
    return inverseFrecuency

def WeightDict(theDict, inverseFrecuency):
    keys = theDict.keys()
    # weightDict = {}

    cont = 0
    for k in keys:
        # print(k)
        theDict[k] = [(t[0], int(inverseFrecuency[cont]*t[1]*10000)) for t in theDict[k]]
    return theDict


def saveIn(file_name, data):
    print("Guardando en: ", file_name)
    afile = open(file_name, 'wb')
    pickle.dump(data, afile)
    afile.close()

if __name__ == '__main__':
    ##### Para cargar los datos del diccionario que se encuentran en el fichero
    afile = open('/home/sergio/Topicos/Corpusgoogle/backup/dbAuxCos', 'rb')
    dbcos = pickle.load(afile)
    afile.close()

    print("obteniendo valores máximos...")
    varMaximos = maximos(dbcos)
    print("obteniendo frecuencia inversa...")
    inverseFrecuency = InvFrecuency(dbcos)
    print("obteniendo frecuencia normalizada...")
    normDict = NormFrec(dbcos,varMaximos)
    print("obteniendo pesos...")
    weightDict = WeightDict(normDict, inverseFrecuency)

    saveIn('dbWeight', weightDict)
