beginning_of_the_row = 0
end_of_row = 88888888
result = 0
print('Терпение, расчёты займут некоторое время')
for i in range(beginning_of_the_row, end_of_row + 1):
    result += i
print(f'Сумма ряда от {beginning_of_the_row} до {end_of_row} равняется: {result}')
input('Для выхода нажмите Enter')
