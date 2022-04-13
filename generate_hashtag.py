def generate_hashtag(s):
    """Функция для автоматического корректного написания хештегов из любой строки"""
    if ((len(list(s)) > 140) or (len(list(s)) == 0)):           #проверка содержания
        return False
    else:
        stroka_ = s.title()  # начала слов с большой буквы
        stroka_ = stroka_.split()           #формирование списка из слов,для удаления лишних пробелов
        hash_tag = '#'
        result = hash_tag + "".join(stroka_) #объединение символа и строки из списка
        return result

str_ = input('Введите строку,из которой необходимо сделать хештег:\n')
f = generate_hashtag(str_)
print(f)

