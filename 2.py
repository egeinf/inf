for a in 0,1:
  for b in 0,1:
    for c in 0,1:
      for d in 0,1:
        F = (a <= b) and (c <= d) or not c
        if F == 0:
          print(b,d,c,a)

# 1 0 1 0
# 0 0 1 1
# 0 1 1 1
# 1 0 1 1