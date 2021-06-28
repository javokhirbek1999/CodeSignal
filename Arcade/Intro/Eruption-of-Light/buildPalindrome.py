def buildPalindrome(st):
    for i in range(len(st)):
        subString = st[i:len(st)]
        if subString == subString[::-1]:
            nonPalindrome = st[0:i]
            return st + nonPalindrome[::-1]
