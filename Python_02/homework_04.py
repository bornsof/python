# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

words = []
while not words:
    string_word = input("Введите слова: ")
    if not string_word:
        print('Вы ничего не ввели. Повторите ввод')
    elif not string_word.replace(' ', '').isalpha():
        print('Введите только слова, никаких цифр и спецсимволов')
    else:
        words = string_word.split()
for word in words:
    print(word[:10])
