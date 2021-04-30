# Импортируем библиотеку vk_api
import vk_api
# Импортируем библиотеку random
import random
# Импортируем библиотеку datetime
import datetime
# Импортируем библиотеку requests
import requests
# Импортируем библиотеку json
import json
# Импортируем bs4
from bs4 import BeautifulSoup
# Импортируем клавиатуру
from vk_api.keyboard import VkKeyboard
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType

# Создаём переменную для  токена от группы

token="1d1698a3e7f848ae7b8966dd63d07c1e2458ce99d9317f03747c2bb5f75086f7298dfbc42064948753e07" # В ковычки вставляем токен.

comps = []



# Подключаем токен и longpoll
bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but('Питон', 'positive'), get_but('Группа Кванториума', 'positive')],
        [get_but('Наш дискорд', 'positive')], [get_but('Научные гифки', 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


# Создадим функцию для ответа на сообщения в лс группы
def vk(id, text):

    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0, 'keyboard' : keyboard})

def parse():
    url = 'https://vk.com/kvantorium62'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='wall_text')

    for item in items:

        comps.append([item.find('div', class_='wall_post_text')])

parse()

# Слушаем (Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      # Чтобы наш бот не слышал и не отвечал на самого себя
       if event.to_me:

        # Для того чтобы бот читал все с маленьких букв
          message = event.text.lower()
          # Получаем id пользователя
          id = event.user_id

          if message == 'начать':
           vk(id, 'Привет,что хотели?!')

          elif message == 'питон':
             vk(id, 'https://www.youtube.com/watch?v=fp5-XQFr_nk')

          elif message == 'группа кванториума':
             vk(id, 'https://vk.com/kvantorium62')

          elif message == 'наш дискорд':
             vk(id, 'https://discord.gg/NuMjvGAPPH')


          elif message == 'научные гифки':
                    for i in comps:
                      if '/emoji/e/f09f8eaf.png' in str(i[0]):
                          i[0] = str(i[0]).replace("<br/>", "\n")
                          i[0] = BeautifulSoup(i[0], 'html.parser')
                          vk(id,(i[0].get_text(strip=False))) 

          else:
                    vk(id, 'Можете более понятнее выразиться')
