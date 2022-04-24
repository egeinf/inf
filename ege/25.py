################# Цифры - сумма
def sumNumber(x):
    s = 0
    while x > 0:
        s = s + x % 10
        x = x // 10
    return s
################# Делители - количество (выводится МИН и МАК, кроме единицы!)
def CountNOD(x):
    k = 0
    d = 2
    while d * d < x:
        if x % d == 0:
            k += 2
        d += 1
    if d * d == x:
        k += 1
    if k == 2:
        print(d , x // d)
        return k

def F(x): # Разность МАК и МИН делителя целого числа, не считая единицы и самого числа
    d = 2
    while d * d < x:
        if x % d == 0:
            return x // d - d
        d += 1
    return 0




################# Какой-то старый архивный код
a = []
N = 5
for i in range(N):
    a.append(int(input()))

k = 0
for i in range(N):
    for j in range(N):
        if (a[i] + a[j]) % 2 != 0:
            k += 1

print(k)

![image](https://user-images.githubusercontent.com/70198995/154704674-e07575cd-199a-433e-97fd-ee55ca983661.png)

![image](https://user-images.githubusercontent.com/70198995/154717958-17286ca1-1c0b-423f-a88c-21739edb1c69.png)

![image](https://user-images.githubusercontent.com/70198995/154719499-bd24dace-c884-4413-b3f6-e66a75ad891c.png)
