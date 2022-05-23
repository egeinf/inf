for s in range(40900000, 50000000):
  res = s
  n = 50
  while n > 0:
    n = s // n
    s = s // 2
  if s == 10000:
    print(res)
    break


# 40960000