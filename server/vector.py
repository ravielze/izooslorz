from DocProcessing import DocumentManager, Language

def cosineDict(q: dict, d: dict):
    result = 0
    for k in q.keys():
        if (k in d.keys()):
            result += (q[k]*d[k])
    denom = q["_norm"]*d["_norm"]
    result = result/denom - 1
    return result
