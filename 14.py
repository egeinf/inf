x = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 110 - 2 ** 1050 - 2022
result = ''
while x:
    result += str(x % 4)
    x //= 4
print(result.count('3'))
