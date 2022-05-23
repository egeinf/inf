a = [1] * 3 + [0] * 101
for i in range(3,101):
  if sum(map(int, str(i))) % 2 == 0:
    a[i] = a[i-1] - a[i-2]
  else:
    a[i] = a[i-1] + a[i//2]
print(a[100])
# 23