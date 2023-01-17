import numpy as np


def getAll2partitions(w):
    if len(w) == 0:
        return np.ones((1,1), dtype=int)
    w_sum = int(np.sum(w))
    n = len(w)
    
    arr_res = np.ones((n, n+1, w_sum+1), dtype=int)*-1
    
    def getCell(i, n1i, w1i):
        if n1i < 0 or w1i < 0:
            return 0
        if n1i == 0 and w1i == 0:
            return 1
        if i == n:
            return 0
        if arr_res[i, n1i, w1i] >= 0:
            return arr_res[i, n1i, w1i]
        else:
            s = 0
            s += getCell(i+1, n1i - 1, w1i - int(w[i]))
            s += getCell(i+1, n1i, w1i)
            arr_res[i, n1i, w1i] = s
            return s
        
    for n1 in range(n+1):
        for w1 in range(w_sum+1):
            arr_res[0, n1, w1] = getCell(0, n1, w1)
    
    return arr_res[0]


def getAll3partitions(w):
    if len(w) == 0:
        return np.ones((1,1,1,1), dtype=int)
    w_sum = int(np.sum(w))
    n = len(w)
    
    arr_res = np.ones((n, n+1, n+1, w_sum+1, w_sum+1), dtype=int)*-1
    
    def getCell(i, n1i, n2i, w1i, w2i):
        if n1i < 0 or n2i < 0 or w1i < 0 or w2i < 0:
            return 0
        if n1i == 0 and n2i == 0 and w1i == 0 and w2i == 0:
            return 1
        if i == n:
            return 0
        if arr_res[i, n1i, n2i, w1i, w2i] >= 0:
            return arr_res[i, n1i, n2i, w1i, w2i]
        else:
            s = 0
            s += getCell(i+1, n1i - 1, n2i, w1i - w[i], w2i)
            s += getCell(i+1, n1i, n2i - 1, w1i, w2i - w[i])
            s += getCell(i+1, n1i, n2i, w1i, w2i)
            arr_res[i, n1i, n2i, w1i, w2i] = s
            return s
        
    for n1 in range(n+1):
        for n2 in range(n+1-n1):
            for w1 in range(w_sum+1):
                for w2 in range(w_sum+1-w1):
                    arr_res[0, n1, n2, w1, w2] = getCell(0, n1, n2, w1, w2)
    
    return arr_res[0]


           
def getAll4partitions(w):
    w_sum = int(np.sum(w))
    n = len(w)
    
    arr_res = np.ones((n, n+1, n+1, n+1, w_sum+1, w_sum+1, w_sum+1), dtype=int)*-1
  
    def getCell(i, n1i, n2i, n3i, w1i, w2i, w3i):
        if n1i < 0 or n2i < 0 or n3i < 0 or w1i < 0 or w2i < 0 or w3i < 0:
            return 0
        if n1i == 0 and n2i == 0 and n3i == 0 and w1i == 0 and w2i == 0 and w3i == 0:
            return 1
        if i == n:
            return 0
        if arr_res[i, n1i, n2i, n3i, w1i, w2i, w3i] >= 0:
            return arr_res[i, n1i, n2i, n3i, w1i, w2i, w3i]
        else:
            s = 0
            s += getCell(i+1, n1i - 1, n2i, n3i, w1i - int(w[i]), w2i, w3i)
            s += getCell(i+1, n1i, n2i - 1, n3i, w1i, w2i - int(w[i]), w3i)
            s += getCell(i+1, n1i, n2i, n3i - 1, w1i, w2i, w3i - int(w[i]))
            s += getCell(i+1, n1i, n2i, n3i, w1i, w2i, w3i)
            arr_res[i, n1i, n2i, n3i, w1i, w2i, w3i] = s
            return s
        
    for n1 in range(n+1):
        for n2 in range(n+1-n1):
            for n3 in range(n+1-n1-n2):
                for w1 in range(w_sum+1):
                    for w2 in range(w_sum+1-w1):
                        for w3 in range(w_sum+1-w1-w2):
                            arr_res[0, n1, n2, n3, w1, w2, w3] = getCell(0, n1, n2, n3, w1, w2, w3)
    
    return arr_res[0]