a = 'АПРСУ'
count = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    b = a1+a2+a3+a4+a5
                    count += 1
                    # проверка условий
                    if a1 == 'У' and 'АА' not in b:
                      print(count,b)
                      break