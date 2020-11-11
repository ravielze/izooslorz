import pandas as pd
import json
from DocProcessing import DocumentManager, Language
df = pd.read_csv("documents.csv")

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

def cosine_array(q: list, d: list):
    result = 0
    for i in range(2, len(q)):
        idx = binary_search(d, 2, len(d)-1, q[i][0])
        if(idx>0):
            result += (q[i][1]*d[idx][1])
    result /= (q[0][1]*d[0][1])
    return result

def query_word_count(query: str): #query needs to be naturalized first
    words = query.split()
    result = {}
    for w in words:
        if w in result.keys():
            result[w][0] += 1
        else:
            result[w] = [1, 0]
    norm = 0
    for k in result.keys():
        for i in range (len(df)):
            test_string = df['data'].loc[i]
            test_string = test_string.replace("\'", "\"")
            d = json.loads(test_string)
            if k in d.keys():
                result[k][1] += 1
        result[k][1] = math.log(len(df)/result[k][1], 10)
        norm += (result[k][0]*result[k][1])**2
    norm **= 0.5
    result["_norm"] = norm
    result["_total"] = len(words)
    return result

def cosine_dict(q: dict, d: dict):
    result = 0
    denom = 0
    for k in q.keys():
        if (k!="_norm" and k!="_total" and k in d.keys()):
            result += (q[k][0]*q[k][1]*q[k][1]*d[k])
            denom += (q[k][1]*d[k])**2
    result = result/(q["_norm"] * (denom**0.5))
    return result

def search_sort(query: str):
    q = query_word_count(query)
    sorter = [[0, df['filename'].loc[i], 0, ""] for i in range (len(df))]
    for i in range (len(df)):
        test_string = df['data'].loc[i]
        test_string = test_string.replace("\'", "\"")
        d = json.loads(test_string)
        sorter[i][0] = cosine_dict(q, d)
        sorter[i][2] = d["_total"]
    sorter.sort(reverse = True)
    result = [{
            "Nama file": sorter[i][1],
            "Tingkat kemiripan": sorter[i][0],
            "Jumlah kata": sorter[i][2],
            "Kalimat pertama": sorter[i][3]
        } for i in range (len(sorter))]
    return result

