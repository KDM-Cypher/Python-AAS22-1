import Levenshtein

class LevenshteinWordComparison:

    def word_comparison(word1, word2):
            print(word1, word2, Levenshtein.distance(word1, word2), )

if __name__ == "__main__":

    words = [
        'Уазик', 'Убавить', 'Убавиться', 'Убаюкать', 'Убаюкивать', 'Убедительный', 'Убедить', 'Убедиться', 'Убежать',
        'Убеждение', 'Убежденный', 'Убежище', 'Убелить', 'Уберечь', 'Убивать', 'Убиваться', 'Убийственный', 'Убийство',
        'Убийца', 'Убирать', 'Убираться', 'Убитый', 'Убить', 'Убиться', 'Ублаготворить']
    word_comparison = 'Убаюкать'

    print('Проверяемое слово ' + str(word_comparison))
    for i in words:
        if LevenshteinWordComparison.word_comparison(i, word_comparison) == 0:
            print('"' + str(i) + '"' + ' совподает с проверяемым словом')
        else:
            print('"' + str(i) + '"' + ' не совподает с проверяемым словом')

