# Определите, при каком наименьшем / наибольшем значении s
for n in range(100000):
  res = n

  s = 460
  while s - n > 0:
    s = s - 50
    n = n - 10

  if s == 10:
    print(res)


# Наименьший x, при котором алгоритм напечатает трёхзначное
for x in range(1, 1000):
    res = x
    x0 = x
    N = 0
    while x > 0:
        d = x % 2
        N = 10 * N + d
        x = x // 2
    N = N + x0
    if len(str(N)) == 3:
        print(res)
        break