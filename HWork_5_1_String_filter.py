# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


string_input = input("введите строку: ")
if string_input == '':
    string_input = "привет абв мир улеабвтел"

# ------ filter()
string_result = string_input.split(' ')
string_result = filter(lambda s: not 'абв' in s , string_result)
print (' '.join(list(string_result)), ' <-- filter()')

# ------ python comrehension
string_result = string_input.split(' ')
string_result = [s for s in string_result if s.find('абв') == -1] # not 'абв' in s | s.find('абв') == -1 (Аналоги)
print (' '.join(list(string_result)), ' <-- python comrehension')