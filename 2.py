for x in 0,1:
  for y in 0,1:
    for z in 0,1:
      for w in 0,1:
        F = (w == z) or (x and not y) or w
        if F == 0:
          print(z,y,x,w)
# X X 1 X
# X 0 X X
# X 1 0 0

### zyxw