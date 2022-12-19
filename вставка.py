import pyperclip


while True:
    try:
        a = pyperclip.paste()

        with open(f"rr.txt", 'w') as file:
            file.write(a)  # вписываем текст
            file.close()  # закрываем

        with open(f"rr.txt") as file:
            gen = file.read()  # читаем файл

        l = pyperclip.copy(gen)

    except Exception:
        print("Програма работает жди если нет перезапусти")
