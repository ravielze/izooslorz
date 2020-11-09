from DocProcessing import DocumentManager, Language

def binary_search(D: list, a: int, b: int, s: str):
    if(D[b][0] == s):
        result = b
    elif(b-a==1):
        if(D[a][0] == s):
            result = a
        else:
            result = -1
    else:
        c = (a+b)//2
        if(D[c][0]>s):
            result = binary_search(D, a, c, s)
        else:
            result = binary_search(D, c, b, s)
    return result

def cosine_dict(q: dict, d: dict):
    result = 0
    for k in q.keys():
        if (k in d.keys()):
            result += (q[k]*d[k])
    denom = q["_norm"]*d["_norm"]
    result -= q["_total"]*d["_total"]
    result = result/denom - 1
    return result

def cosine_array(q: list, d: list):
    result = 0
    for i in range(2, len(q)):
        idx = binary_search(d, 2, len(d)-1, q[i][0])
        if(idx>0):
            result += (q[i][1]*d[idx][1])
    result /= (q[0][1]*d[0][1])
    return result

