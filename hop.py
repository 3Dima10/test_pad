from bs4 import BeautifulSoup
from requests import get


while True :
    try:
        a = str(input("Веди URL чтобы узнать оцеку:"))
        b = get(a).text
        
        bs = BeautifulSoup(b, "lxml")
        bsd = bs.find(class_="val").text
        
        nfo = f'Оценка:{bsd}'
        print(nfo)
    except Exception:
        print("Веди URL тест пада")

