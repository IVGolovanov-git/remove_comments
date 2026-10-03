# Удаление комментариев после знака '#'

Программа открывает файл - источник. Находит строки, содержащие знак '#', и удаляет всю информацию после этого знака.
Результат работы сохраняется в новом файле

Используются методы:

1) split() - преобразует строку в список строк по символу в скобках. Например,'#'
2) strip() - удаление лишних пробелов в начале и конце строки
3) ('/n).join() - формирует единую строку из списка по символу '\n'


# Removing comments after the '#' sign

The program opens the source file. It finds lines, containing the '#' sign, and removes all information after this sign.
The result is saved in a new file.

The following methods are used:

1) split() — converts a string into a list of strings based on the character in the brackets. For example, '#'
2) strip() — removes extra spaces at the beginning and end of a string
3) ('/n).join() — forms a single string from the list based on the '\n' character
