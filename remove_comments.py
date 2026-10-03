# Программа открывает файл источник. Извлекает из него комментарии
# и удаляет их. Очищенный код добавляется в новый файл

def remove_com(f_name_sourse, f_name_new):
    # Проверяем возможность открытия файла
    try:
        with open(f_name_sourse, 'r', encoding='utf-8') as f:
            file_text = f.readlines()
            new_text = []
            for line in file_text:
                # Разбиваем строку на список по знаку "#"
                # Берем элемент [0], т.е. первый до "#"
                # Удаляем в нем лишние пробелы методом strip()
                new_line = line.split("#")[0].strip()
                new_text.append(new_line)
        with open(f_name_new,'a', encoding='utf-8') as new_f:
            new_f.write('\n'.join(new_text))
    except FileNotFoundError: # Если ошибка открытия файла
        print(f'Отсутствует файл с именем: {f_name_sourse}')
        return 0

file_sourse= input('Введите имя файла - источника: ')
file_new = input('Введите имя нового файла: ')
remove_com(file_sourse, file_new)
