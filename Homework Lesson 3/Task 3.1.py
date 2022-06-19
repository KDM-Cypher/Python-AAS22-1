# 1 Устанавливаем модуль Levenshtein через PIP
# 2 Проверка модуля
# 3 Импортируем модуль Levenshtein

if __name__ == "__main__":
    import Levenshtein

    pairs = [
        ('год', 'человек'),
        ('время', 'дело'),
        ('жизнь', 'день'),
        ('рука', 'работа'),
        ('слово', 'место'),
        ('вопрос', 'лицо'),
    ]
    print('Количество преобразований:')
    i = 0
    for s, t in pairs:
        print('Из "' + str(pairs[i][0]) + '"' + ' в "' + str(pairs[i][1]) + '"' + ' ' + str(Levenshtein.distance(s, t)))
        i += 1
