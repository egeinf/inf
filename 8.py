a = 'АЕЖЙМУ'
k = 0
for a1 in a:
  for a2 in a:
    for a3 in a:
      for a4 in a:
        for a5 in a:
          # две буквы рядом не одинаковые
          if a1 != a2:
            if a2 != a3:
              if a3 != a4:
                if a4 != a5:
                  k += 1
print(k/2) # четные места

# 1875