text = 'asdxfghyxyx'
modified_text = ''
changeable_character = 'x'
for string in text:
    if string != changeable_character:
        modified_text += string
    elif string == changeable_character:
        modified_text += 'y'
print(f'Изменённый текст: {modified_text}')
input('Для выхода нажмите Enter')
