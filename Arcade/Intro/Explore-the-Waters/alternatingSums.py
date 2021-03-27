def alternatingSums(a):
    team1 = a[::2]
    team2 = a[1::2] 
    return [sum(team1),sum(team2)]    
