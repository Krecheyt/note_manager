username = input('Введите имя пользователя: ')
title = input('Заголовок заметки: ')
new_title = title.upper()
content = input('Опишите содержание заметки: ')
start_date = input('Введите дату (дд.мм.гг.) начала действия заметки: ',)
start_time = input('Введите время (чч-мм) начала действия заметки: ')
end_date = input('Введите дату (дд.мм.гг.) окончания действия заметки: ')
end_time = input('Введите время (чч-мм) окончания действия заметки: ')
print('Пользователь:        ', username)
print('Заметка:             ', new_title)
print('Содержание заметки:  ', content)
print('Начало действия:     ', start_date + '  ' + start_time)
print('Окончание действия:  ', end_date + '  ' + end_time)

