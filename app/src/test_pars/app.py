"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from bs4 import BeautifulSoup
from requests import get
import pyperclip
import asyncio
# import aiofiles
# import aiohttp


class test_pars(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        button1 = toga.Button("ПАРСЕР", on_press=self.test, style=Pack(flex=1))

        # name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        # name_box.add(button1)
        button2 = toga.Button(
            "ОСТАНОВИТЬ ПАРСЕР", on_press=self.stop, style=Pack(flex=1)
        )

        button3 = toga.Button(
            "УЗНАТЬ ОЦЕНКУ", on_press=self.solo, style=Pack(padding=10)
        )

        name_box2 = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box2.add(button1)
        name_box2.add(button2)

        main_box.add(name_box2)
        main_box.add(button3)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # def test(self, widget):
    #     self.is_running = True
    #     self.loop.run_in_executor(self.executor, self._test_async)

    async def test(self, widget):
        self.is_running = True
        while self.is_running:
            try:
                # html из буфера обмена
                a = await self.loop.run_in_executor(None, pyperclip.paste)

                # # создание файла с текстом
                # async with open("rr.txt", "w") as file:
                #     await file.write(a)

                # # открываем и читаем файл
                # async with open("rr.txt") as file:
                #     gen = await file.read()

                # парсим
                bs = BeautifulSoup(str(a), "lxml")  # парсим текст
                bd = bs.find(class_="qtext")  # ищем нужную строку
                print("Вопрос : \n" + bd.text)  # выводим на экран
                paste = await self.loop.run_in_executor(None, pyperclip.copy, bd.text)

                await asyncio.sleep(0)  # Пауза в секунду перед новой итерацией

            except Exception :
                print(a)

    async def stop(self, widget):
        self.is_running = False
        await self.main_window.info_dialog(f"Остановка", "Парсер остановлен")

    async def solo(self, widget):
        try:
            a = str(pyperclip.paste())
            b = get(a).text
            bs = BeautifulSoup(b, "lxml")
            bsd = bs.find(class_="val").text
            # nfo = f"Оценка:{bsd}"

            self.main_window.info_dialog(f"Оценка", rf"{bsd}")
        except Exception:
            self.main_window.info_dialog(f"Ошыбка", "Скопируй сылку тест пада")


def main():
    return test_pars()
