for a in range(1,500):
    flag = 1
    for x in range(1,1000):
        flag *= ((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 70)
    if flag:
        print(a)
        break
