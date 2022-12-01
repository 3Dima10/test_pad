from bs4 import BeautifulSoup

import pyperclip

while True:
    try:
        a = str(pyperclip.paste())  # html из буфера обмена

        # создания файла с текстом
        with open(f"rr.txt", 'w') as file:
            file.write(a)  # вписываем текст
            file.close()  # закрываем

        # открываем и читаем файл
        with open(f"rr.txt") as file:
            gen = file.read()  # читаем файл

        # парсим
        bs = BeautifulSoup(gen, 'lxml')  # парсим текст
        bd = bs.find(class_="qtext")  # ищим нужною нас строчку
        print("Вопрос : \n" + bd.text)  # выводим на екран
        paste = pyperclip.copy(bd.text)
    except Exception:
        print("скопируй HTML")
