# У исполнителя Калькулятор две команды, которым 

# Содержит
def make(x, y):
	if x == y:
		return 1
	elif x > y:
		return 0
	elif x < y:
		return make(x + 1, y) + make(x + 2, y)
n = make(5, 10) * make(10, 15)
print(n)

# Содержит 16 | Не содержит 56
def make(x, y):
	if x == y:
		return 1
	elif x > y or x == 45:
		return 0
	elif x < y:
		return make(x + 1, y) + make(x * 3, y)

n = make(3, 16) * make(16, 52)
print(n)
