x = 6 * 512 ** 180 + 7 * 64 ** 181 + 3 * 8 ** 184 + 5 * 8 ** 125 - 65
result = ''
while x != 0:
    result += str(x % 64)
    x //= 64
print(result.count('0'))