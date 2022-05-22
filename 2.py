for z in 0,1:
  for y in 0,1:
    for x in 0,1:
      for w in 0,1:
        F = not(x <= z ) or (y == w) or not y
        if F == 0:
          print(x,z,y,w)


# x z y w
# 0 0 1 0
# 0 1 1 0
# 1 1 1 0

# 0 0 X X
# 0 X X X 
# 1 1 X 0 
