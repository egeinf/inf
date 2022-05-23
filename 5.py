k = 0

for N in range(100000000, 300000000):
  res = str(N)
  N = str(N)
  a = int(N[0]) + int(N[1]) + int(N[2]) + int(N[3]) + int(N[4]) + int(N[5]) + int(N[6]) + int(N[7]) + int(N[8])
  N = bin(a)[2:]
  if N.count('1') % 2 == 0: # 1 разряд
    N = '1' + N + '00'
  elif N.count('1') % 2 == 1: # 2 разряд
    N = '10' + N + '1'
  N = int(N, 2)
  if N == 21:
    k += 1
print(k)