k = 0
for i in range(123450000, 123459999):
    i = str(i)
    if i[6] == '6' and i[8] == '8':
        i = int(i)
        if i % 17 == 0:
            print(i, i // 17)