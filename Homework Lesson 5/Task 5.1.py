import Levenshtein


class LevenshteinWordComparison:

    def word_comparison(word1, word2):
        print(word1, word2, Levenshtein.distance(word1, word2), )


if __name__ == "__main__":

    words = [
        'Уазик', 'Убавить', 'Убавиться', 'Убаюкать', 'Убаюкивать', 'Убедительный', 'Убедить', 'Убедиться', 'Убежать',
        'Убеждение', 'Убежденный', 'Убежище', 'Убелить', 'Уберечь', 'Убивать', 'Убиваться', 'Убийственный', 'Убийство',
        'Убийца', 'Убирать', 'Убираться', 'Убитый', 'Убить', 'Убиться', 'Ублаготворить'
    ]
    word_comparison = 'Убаюкать'

    print('Проверяемое слово ' + str(word_comparison))
    for i in words:
        if LevenshteinWordComparison.word_comparison(i, word_comparison) == 0:
            print('"' + str(i) + '"' + ' совпадает с проверяемым словом')
        else:
            print('"' + str(i) + '"' + ' не совпадает с проверяемым словом')

# Определение класса отделено двумя пустыми строками вместо одной
# Значения в списке расположены на нескольких строках, а не в одну строку
# Закрывающая скобка в списке расположена под первым символом строки, начинающей многострочную конструкцию
# Указанные выше меры улучшают читаемость кода для человека
