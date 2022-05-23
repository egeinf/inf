for A in range(20,30):
  flag = 1
  for x in range(1,1000):
    for p in range(117,158):
      for q in range(129,180):
        flag *= (not p or not q or A)
  if flag:
    print(A)
    break

# 29