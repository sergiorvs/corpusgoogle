import pickle
import numpy as np


def takeSecond(elem):
    return elem[1]

def find_pos(key, theDict):
    theList = list(theDict.keys())
    if key in theDict:
        return theList.index(key)
    theDict[key] = {}
    return len(theDict)-1

def new_dict(fact):
    res = list(fact.keys())
    data_base = {}
    for r in res:
        print(r)
        if(not r in fact):
            keys = []
        else:
            keys = list(fact[r].keys())
        positions = []
        for k in keys:
            pos = find_pos(k, fact)
            # print(pos, ": ", k)
            positions.append(pos)
        # data_base[r] = 2
        # print(keys)
        data_base[r] = positions

    return data_base    


def createBooleanArray(positions, size):
    vec = np.zeros(size,dtype=bool)
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
        vect2 = createBooleanArray(pos,size)

        # vecRes = np.invert(np.logical_xor(vect1,vect2))
        # concur = np.count_nonzero(vecRes)
        # result = concur/size
        result = (np.logical_and(vect1, vect2)).sum() / float((np.logical_or(vect1, vect2)).sum())
        allPorcentages.append((k, result))
        allPorcentages.sort(key=takeSecond, reverse=True)
    
    return allPorcentages




    


if __name__ == '__main__':
    ##### Para cargar los datos del diccionario que se encuentran en el fichero
    afile = open('factorizeDict03', 'rb')
    fact = pickle.load(afile)
    afile.close()

    # fact['magic'] = {'scuba': 1, 'prompt':43, 'property':63}

    res = list(fact.keys())
    # print(len(fact))
    # print(res[0])
    # print(fact[res[0]])
    # db = new_dict(fact)

    ###### Para guardar el diccionario en un bitmap
    # afile = open('db03', 'wb')
    # pickle.dump(db, afile)
    # afile.close()

    afile = open('db03', 'rb')
    db = pickle.load(afile)
    afile.close()

    print("finalizo")
    # print(fact)

    # print(db)
    print(len(fact))
    axl = compareVectors('capricornus', db, 500000)
    for i in range(0,10):
        print(axl[i])

