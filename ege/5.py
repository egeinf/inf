## Найти число которое может получиться в алгоритме больше 55 если добавляется 2 цифры справа по правилам суммы чисел и остатка делении на два
for N in range(100):
    res = N
    N = N - (N % 4)
    N = bin(N)[2:]
    a = []
    for i in range(len(N)): # складываются все числа
        a.append(int(N[i]))
        
        sumN = sum(a) % 2 # сумма делится на два
    N = N + str(sumN) # сумма добавляется в число
    a = []
    for i in range(len(N)): # складываются все числа
        a.append(int(N[i]))
        sumN = sum(a) % 2 # сумма делится на два
    N = N + str(sumN) # сумма добавляется в число
 
    N = int(N, 2)
    if int(N) > 55:
        print(N)
    
## ЗАПИСЬ ПЕРЕВОРАЧИВАЕМ
for N in range(1,88):
  res_N = N # ЗАПОМИНАЕМ РЕЗУЛЬТАТ
  two_N = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ
  two_N = two_N[::-1] # ПЕРЕВОРАЧИВАЕМ
  
  N = int(two_N, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if N == 21:
    print(res_N)

## БИТ ЧЕТНОСТИ
for N in range(10000):
  res_N = N # ЗАПОМИНАЕМ РЕЗУЛЬТАТ
  two_N = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ

  if two_N.count('1') % 2 == 0: # Если в двоичном коде четное количество единиц
    two_N += '0'
  else: two_N += '1' # 1 если нечетное количество единиц
  if two_N.count('1') % 2 == 0: # 2 БИТ ЧЕТНОСТИ
    two_N += '0'
  else: two_N += '1'

  N = int(two_N, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if N > 68:
    print(res_N)
    break

## Последняя цифра удаляется
for N in range(10000):
  res_N = N # ЗАПОМИНАЕМ РЕЗУЛЬТАТ
  two_N = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ
  two_N = two_N[:-1] # Последняя цифра удаляется
  if res_N % 2 == 0: # Если исходное число N было нечётным то 10, четным - 01
    two_N += '01'
  else: two_N += '10'

  N = int(two_N, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if N == 86:
    print(res_N)
    break

## БИТ ЧЕТНОСТИ
for N in range(10000):
  res_N = N # ЗАПОМИНАЕМ РЕЗУЛЬТАТ
  two_N = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ

  if two_N.count('1') % 2 == 0: # 1 БИТ ЧЕТНОСТИ
    two_N += '1'
  else: two_N += '0'
  temp = two_N.count('1') % 2 # ОСТАТОК ОТ ДЕЛЕНИЯ КОЛ-ВА 1 НА 2
  two_N += str(temp)
  
  N = int(two_N, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if N > 37:
    print(N)
    break
  
## Складываются все цифры и остаток отделения на 2
for N in range(10000):
  res_N = N # ЗАПОМИНАЕМ РЕЗУЛЬТАТ
  two_N = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ
  # ПЕРВЫЙ РАЗ
  sum_N = sum(map(int, list(two_N))) % 2 # СУММА ВСЕХ ЧИСЕЛ И ОСТАТОК ИХ ДЕЛЕНИЯ НА 2
  two_N += str(sum_N)
  # ВТОРОЙ РАЗ
  sum_N = sum(map(int, list(two_N))) % 2 # СУММА ВСЕХ ЧИСЕЛ И ОСТАТОК ИХ ДЕЛЕНИЯ НА 2
  two_N += str(sum_N)

  N = int(two_N, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if N > 305:
    print(res_N // 4) # 4N ЗАПИСЬ
    break

# https://user-images.githubusercontent.com/70198995/149659690-e29626c6-91e1-4854-8cf8-ccbcd9625a2c.png

## Складываются 1+2, 3+4 исходного числа
# Алгоритм. ЕГЭ. №101, 102
for x in range(1000,9999+1):
  x = str(x)
  sum12 = int(x[:1]) + int(x[1:2]) # СКЛАДЫВАЕТСЯ 1 И 2
  sum34 = int(x[2:3]) + int(x[3:4]) # СКЛАДЫВАЕТСЯ 3 И 4
  
  sum12 = str(sum12) # ПЕРЕВОД ДЛЯ ПРОВЕРКИ СТРОК
  sum34 = str(sum34)
  if sum12 + sum34 == '1612':
    print(x)

## СКОЛЬКО СУЩЕСТВУЕТ ЧИСЕЛ: Складываются 1+2, 2+3 исходного числа
a = []
for x in range(100,999+1):
  x = str(x)
  sum12 = int(x[:1]) + int(x[1:2]) # СКЛАДЫВАЕТСЯ 1 И 2
  sum23 = int(x[1:2]) + int(x[2:3]) # СКЛАДЫВАЕТСЯ 2 И 3
  
  sum12 = str(sum12) # ПЕРЕВОД ДЛЯ ПРОВЕРКИ СТРОК
  sum23 = str(sum23)
  if sum12 + sum23 == '1610' or sum12 + sum23 == '1016':
    a.append(x)
  
print(len(a))

# https://user-images.githubusercontent.com/70198995/149659892-c47673bd-888b-4137-b031-1f01787e8ddf.png

# Алгоритм. ЕГЭ. №103
for x in range(100,999+1):
  x = str(x) # ЕРЕВОД В СТРОКУ
  y = '723'
  a = [] #МАССИВ ДЛЯ ВЫВОДА В ПОРЯДКЕ НЕУБЫВАНИЯ
  sum1 = int(x[0]) + int(y[0]) #СКЛАДЫВАЮТСЯ РАЗРЯДЫ
  sum2 = int(x[1]) + int(y[1])
  sum3 = int(x[2]) + int(y[2])


  a.append(sum1) #ВВОД СУММ В МАССИВЕ
  a.append(sum2)
  a.append(sum3) 
  a.sort()  #ПОРЯДОК НЕУБЫВАНИЯ (ВОЗРАСТАНИЯ)
  if a == [4, 8, 10]:
    print(x)

## Отбрасывается наибольшая
# https://user-images.githubusercontent.com/70198995/150287695-ed3c29eb-85d6-47fe-97d0-0c1e8c38310c.png


for x in range(1000,9999+1):
  x = str(x)
  a = [] #МАССИВ ДЛЯ ВЫВОДА
  sum12 = int(x[:1]) + int(x[1:2]) # СКЛАДЫВАЕТСЯ 1 И 2
  sum23 = int(x[1:2]) + int(x[2:3]) # СКЛАДЫВАЕТСЯ 2 И 3
  sum34 = int(x[2:3]) + int(x[3:4]) # СКЛАДЫВАЕТСЯ 3 И 4
  a.append(sum12) #ВВОД СУММ В МАССИВЕ
  a.append(sum23)
  a.append(sum34)
  a = sorted(a, reverse=True) #ПОРЯДОК УБЫВАНИЯ
  a.pop(0) # УДАЛИТЬ МАКСИМАЛЬНЫЙ
  if a == [5, 5]:
    print(x)

## Пятизначное число
for x in range(10000,99999+1):
  x = str(x)
  a = [] #МАССИВ ДЛЯ ВЫВОДА
  sum135 = int(x[:1]) + int(x[2:3]) + int(x[4:5]) # СКЛАДЫВАЕТСЯ 1 И 3 И 5
  sum24 = int(x[1:2]) + int(x[3:4]) # СКЛАДЫВАЕТСЯ 2 И 4
  

  a.append(sum135) #ВВОД СУММ В МАССИВЕ
  a.append(sum24)
  a = sorted(a, reverse=True) #ПОРЯДОК ВОЗРАСТАНИЯ
  if a == [18, 14]:
    print(x)

# https://user-images.githubusercontent.com/70198995/149662407-b3a0ce4f-9840-4994-91a7-99ecdb8b72e9.png


for N in range(255+1):
  res_N = N # ЗАПОМИНАЕМ РЕЗУЛЬТАТ
  two_N = bin(N)[2:].zfill(8) # ДВОИЧНАЯ ЗАПИСЬ

  two_N = two_N.replace('0', 'A') # ПЕРЕВОРАЧИВАЕМ ВСЕ ЦИФРЫ В ЗАПИСИ
  two_N = two_N.replace('1', 'B')
  two_N = two_N.replace('A', '1')
  two_N = two_N.replace('B', '0')
  N = int(two_N, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ

  if N - res_N == 173: # ИЗ НОВОГО ВЫЧИТАЕТСЯ ИСХОДНОЕ
    print(res_N)
    break

# https://user-images.githubusercontent.com/70198995/149662444-dc92c1d9-c5b5-4f21-80d4-f2cbb9f38eab.png

a = []
for N in range(220, 2800+1):
  res_N = N # ЗАПОМИНАЕМ РЕЗУЛЬТАТ
  two_N = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ

  two_N = two_N[1:]
  N = int(two_N, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  result = N - res_N # ИЗ НОВОГО ВЫЧИТАЕТСЯ ИСХОДНОЕ
  if result not in a: # ЕСЛИ НЕТ ЗНАЧЕНИЯ ВНЕСТИ ЕГО В МАССИВ
    a.append(result)

print(len(a)) # СКОЛЬКО РАЗНЫХ ЗНАЧЕНИЙ

# https://user-images.githubusercontent.com/70198995/149662774-222d1c93-489d-47ae-84b2-8dbd2b54b438.png

a = []
for N in range(100000):
  R = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ

  if N % 4 == 0:
    R += '00'
  if N % 4 == 1:
    R += '01'
  if N % 4 == 2:
    R += '10'
  if N % 4 == 3:
    R += '11'

  result = int(R, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if result < 100:
    print(result)

# https://user-images.githubusercontent.com/70198995/149663156-5db43bcc-bb1c-4b6d-88e0-2336c0529ec5.png

a = []
for N in range(100000):
  res_N = N
  R = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ

  R = R + R[:2][::-1] # В КОНЦЕ ДОБАВЛЯЮТСЯ 2 ПЕРВЫЕ ЦИФРЫ В ПЕРЕВЁРНУТОМ ВИДЕ

  result = int(R, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if result < 70:
    print(res_N)

# https://user-images.githubusercontent.com/70198995/149663361-d6d49c1e-75bf-49cc-a3f5-502eadba37cb.png

a = []
for N in range(100000):
  res_N = N
  R = bin(N)[2:] # ДВОИЧНАЯ ЗАПИСЬ
  R += R[-2:-1] # ВТОРАЯ СПРАВА
  R += R[1:2] # ВТОРАЯ СЛЕВА
  R = int(R, 2) # ДЕСЯТИЧНАЯ ЗАПИСЬ
  if R > 75:
    print(res_N)
    break

# УЗНАТЬ КАКАЯ СТЕПЕНЬ 2 МАК. В ЧИСЛЕ
x1 = 10000
two_x = bin(x1)[2:] # ДВОИЧНАЯ ЗАПИСЬ
two_x = two_x[1:] # УДАЛЯЕТСЯ 1 СЛЕВА ЦИФРА
x2 = int(two_x, 2)
print(x1 - x2)
