import itertools
count = 0
for x in itertools.product('ЛАГЕРЬ', repeat=6):
  # ПРОВЕРКА НА УНИКАЛЬНОСТЬ БУКВ И ОТСУТСТВИИ "Ь"
  if x.count('Л') == 1 and x.count('А') == 1 and x.count('Г') == 1 and x.count('Е') == 1 and x.count('Р') == 1 and x.count('Ь') == 1 and x[0] != 'Ь':
  # ПРОВЕРКА НА ЕА
    for i in range(len(x)):
      if x[i-1] != 'Е' and x[i] != 'А':
        count += 1
        print(count, ''.join(x))
################
import itertools
count = 0
for x in itertools.product('СУМКА', repeat=4):
  # ПРОВЕРКА НА "У" ХОТЯ БЫ 1 РАЗ
  if x.count('У') >= 1:
    count += 1
    print(count, ''.join(x))
################
import itertools
count = 0
for x in itertools.product('КУРИЦА', repeat=4):
  # ПРОВЕРКА НА "У" ХОТЯ БЫ 2 РАЗ
  if x.count('У') >= 2:
    count += 1
    print(count, ''.join(x))
################
import itertools
count = 0
for x in itertools.product('СЛОН', repeat=4):
  # ПРОВЕРКА НА УНИКАЛЬНОСТЬ БУКВ И ОТСУТСТВИИ В НАЧАЛЕ "Н"
  if x.count('С') == 1 and x.count('Л') == 1 and x.count('О') == 1 and x.count('Н') == 1 and x[0] != 'Н':
    count += 1
    print(count, ''.join(x))

              
# ЕГЭ
a = 'АПРСУ'
count = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    x = a1+a2+a3+a4+a5
                    count += 1
                  
                    if a1 == 'У' and 'АА' not in x:
                      print(count, x)
                      break
            
a = 'ИЕАУОЯ'
k = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    b = a1+a2+a3+a4+a5
                    if a5 == 'Е': # оканчивается на "Е"
                        if a1 != a3 and a2 != a4 and a3 != a5: # не совпадают буквы идущие через одну
                          if 'А' in b:
                            k += 1
                            print(k, b)