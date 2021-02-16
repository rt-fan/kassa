d = 1
m = 2
y = 2021
summa = 2000
tarif = 700
sd = 28

while True:
	if summa < tarif:
		#print("меньше")
		x = tarif / sd  # 25₽
		d = int(d + (summa / x))
		#print(int(d), m, y)
		break

	elif summa == tarif:
		#print("равно")
		m += 1
		if m > 12:
			y += 1
			m = 1
		#print(d, m, y)
		break

	else:
		#print("больше")
		summa -= tarif
		m += 1
		if m > 12:
			y += 1
			m = 1
		#print(d, m, y)
		
print(d, m, y)
