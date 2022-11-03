import functools


# создает поле для игры в крестики нолики
def create_grid():
    weight, height = 3, 3
    grid = [[1 for x in range(weight)] for y in range(height)]
    k = 1
    for j in range(len(grid)):
        for i in range(len(grid)):
            grid[j][i] = i + k
        k += 3
    return grid


print(create_grid())


# удаляет слова с заданной буквой
def delete_words(letters, text):
    list_text = text.split()
    index_with_letters = []
    for i in range(len(list_text)):
        if letters in list_text[i]:
            index_with_letters.append(i)
    new_text_list = []
    for i in range(len(list_text)):
        if i not in index_with_letters:
            new_text_list.append(list_text[i])
    new_text = ' '.join(str(x) for x in new_text_list)
    return new_text


letters = 'р'
text = 'над пропастью во ржи'
print(delete_words(letters, text))


# находит сумму цифр вещественного числа
def sum_digit(num):
    def check(n):
        if n not in (',', '.'):
            return n

    count = functools.reduce(lambda x, y: x + y, map(int, (filter(check, num))))
    return count


print(sum_digit('0,56'))


# перемешивает список
def mix_list(sequence):
    new_seq = [sequence[-i - 1] for i in range(0, len(sequence))]
    return new_seq


seq = ['f', 'r', 4]
print(mix_list(seq))
