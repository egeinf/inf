# Ниже записана программа. Укажите
otvet1 = int(input())
otvet2 = int(input())
otvets = []
for x in range(1000000):
  res = x
  
  a = 0
  b = 1
  while x>0:
      a = a + 1
      b = b * (x%10)
      x = x // 10

  if a == otvet1 and b == otvet2:
    otvets.append(res)
    print(res)
    
print(min(otvets), max(otvets))