def tennisSet(score1, score2):
    p1,p2 = min(score1, score2), max(score1,score2)
    if(p2==6):
        return p1<5
    return p2==7 and p1>=5 and p1<p2
    
