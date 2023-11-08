# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define v = Character('Валентин', color="#ffffff")
define r = Character('Родя', color="610000")
define rs = Character('Родион Сергеевич', color="57b0ff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    e "Вы создали новую игру Ren'Py."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
