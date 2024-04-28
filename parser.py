import requests
from bs4 import BeautifulSoup
from random import randint


def parse_anekdotov_net(url):

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        anekdot_elements = soup.find_all(class_='anekdot')

        anekdoty = []

        for anekdot_element in anekdot_elements:
            anekdot_text = anekdot_element.text.strip()
            anekdoty.append(anekdot_text)

        i = randint(1, len(anekdoty))
        rand_joke = anekdoty[i]
        i = 0
        return rand_joke
    else:
        print("Ошибка при загрузке страницы")

#
# # URL страницы с анекдотами
# url = "https://anekdotov.net/anekdot/today.html"
#
# # Вызываем функцию для парсинга анекдотов с указанного URL
# parse_anekdotov_net(url)
