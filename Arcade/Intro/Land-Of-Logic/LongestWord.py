import re
def longestWord(text):
    rs = re.sub("[^\w]",",",text)
    res = re.sub("[_]",",",rs)
    words = [[]]
    for i in res:
        if i == ',':
            words.append([])
        else:
            words[-1].append(i)
    
    
    for i in words:
        if len(i)==0:
            words.pop(words.index(i))
    
    word_list = []
    for i in words:
        if len(i) > 0:
            word_list.append(",".join(i))
    
    wr = []
    for i in word_list:
        wr.append(re.sub('[,]','',i))
    wr.sort(key=len)
    print(wr)
    return wr[-1]
