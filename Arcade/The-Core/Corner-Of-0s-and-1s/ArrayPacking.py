def twosCom_binDec(bin, digit):
  while len(bin)<digit :
    bin = '0'+bin
    if bin[0] == '0':
      return int(bin, 2)
    else:
      return -1 * (int(''.join('1' if x == '0' else '0' for x in bin), 2) + 1)

def twosCom_decBin(dec, digit):
  if dec>=0:
    bin1 = bin(dec).split("0b")[1]
    while len(bin1)<digit :
      bin1 = '0'+bin1
    return bin1
  else:
    bin1 = -1*dec
    return bin(dec-pow(2,digit)).split("0b")[1]

def arrayPacking(a):
  t = []
  for i in a:
    t.append(twosCom_decBin(i,8))

  return int("".join(reversed(t)),2)
