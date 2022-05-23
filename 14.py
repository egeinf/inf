x = abs(3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 ** 666 - 404)
res = ''
while x > 0:
  res += str(x % 5)
  x //= 5
print(res.count('2'))

# 3