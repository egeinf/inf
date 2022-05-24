def defCount(N):
  N = int(N)
  result = 0
  while N != 0:
    result = result + (N % 10)
    N //= 10
  return result

for N in range(30):
  res_N = N
  two_N = bin(N)[2:]
  
  if res_N % 2 == 0:
    two_N += str(res_N)
  else: two_N = '1' + two_N + '00'
  
  if int(two_N) > 11010111:
    print(res_N)
    break

## 23