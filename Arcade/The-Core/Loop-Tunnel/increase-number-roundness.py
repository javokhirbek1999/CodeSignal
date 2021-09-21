def increaseNumberRoundness(n):
    s = list(str(n))
    for i in range(len(s)):
        if s[::-1][i] in ['1','2','3','4','5','6','7','8','9']:
            return '0' in s[::-1][i:]
