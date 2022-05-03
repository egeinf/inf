# Определите, при каком наименьшем / наибольшем значении s
for n in range(100000):
  res = n

  s = 460
  while s - n > 0:
     s = s - 50
     n = n - 10

  if s == 10:
    print(res)
