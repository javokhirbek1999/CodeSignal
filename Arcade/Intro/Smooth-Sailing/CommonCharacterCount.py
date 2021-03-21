def commonCharacterCount(s1, s2):
    chars = list()
    for i in s1:
        if i in chars:
            pass
        else:
            if s1.__contains__(i) and s2.__contains__(i) and s1.count(i) >= s2.count(i):
                for j in range(s2.count(i)):
                    chars.append(i)
            elif s1.__contains__(i) and s2.__contains__(i) and s1.count(i) <= s2.count(i):
                for j in range(s1.count(i)):
                    chars.append(i)
    return len(chars)
