import numpy as np
import pickle


# def create_vector():




if __name__ == '__main__':
    d1file = open('factorizeDict03', 'rb')
    fact = pickle.load(d1file)
    d1file.close()

    keys = fact.keys()
    for k in keys:
        # vec1 = create_vector(fact[k])
        print(len(fact[k].values()))
        break


    print(len(fact))