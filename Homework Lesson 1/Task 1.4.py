row = [3, 4, 56, 100, 15, 2, 20, 30]
composition = 1
index = 0
for i in row:
    if row[index] % 3 == 0 and row[index] % 5 == 0:
        composition *= row[index]
    index += 1
print(composition)
input('Для выхода нажмите Enter')
