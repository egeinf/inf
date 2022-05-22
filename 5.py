for N in range(10000):
  res_N = N
  N = bin(N)[2:]
  if res_N % 2 == 0:
    N = str(N) + '10'
  if res_N % 2 != 0:
    N = '1' + str(N) + '01'
  N = int(N)
  if N > 1000000100:
    print(res_N)
    break
