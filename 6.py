for s in range(1,10000):
  res_s = s
  n = 1
  while s <= 70:
    s = s + 9
    n = n * 7
  if n == 343:
    print(res_s)
    break


## 44