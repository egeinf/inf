s = '2' * 52
while '222' in s or '000' in s:
    if '000' in s:
        s = s.replace('000', '2', 1)
    else:
        s = s.replace('222', '02', 1)
print(s)

## 22