number = input("Ingrese el número: ")
total_d = 0

if int(number) < 10:
    total_d = number
elif int(number) >= 10:
    total_d = 9
    for i in range(10, int(number) + 1):
        total_d += len(str(i))

print(total_d)
