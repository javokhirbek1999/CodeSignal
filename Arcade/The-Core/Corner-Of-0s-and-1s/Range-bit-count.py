def rangeBitCount(a, b):
  bits = ""
  for i in range(a,b+1):
    bits+=bin(i)[2:]
  return list(bits).count('1')
