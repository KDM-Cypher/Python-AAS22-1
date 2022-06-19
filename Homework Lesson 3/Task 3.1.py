# 1 Устанавливаем модуль Levenshtein через PIP
# 2 Импортируем модуль Levenshtein


import Levenshtein

pairs = [
    ('год', 'человек'),
    ('время', 'дело'),
    ('жизнь', 'жизни'),
    ('рука', 'работа'),
    ('слово', 'место'),
    ('вопрос', 'лицо'),
    ]
if __name__ == "__main__":
    print('Количество преобразований:')
    i = 0
    for s, t in pairs:
        print('Из "' + str(pairs[i][0]) + '"' + ' в "' + str(pairs[i][1]) + '"' + ' ' + str(Levenshtein.distance(s, t)))
        i += 1
