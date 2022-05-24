count = 0
for a in range(7):
  for b in range(7):
    for c in range(7):
      for d in range(7):
        for e in range(7):
          for f in range(7):
            for g in range(7):
              a = str(a)
              b = str(b)
              c = str(c)
              d = str(d)
              e = str(e)
              f = str(f)
              g = str(g)
              s = a + b + c + d + e + f + g
              if (a != '3') and (a != '5') and ('22' not in s) and ('44' not in s):
                count += 1
print(count)

## 