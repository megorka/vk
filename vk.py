# Импортируем библиотеку vk_api
import vk_api
# Импортируем библиотеку random
import random
# Импортируем библиотеку datetime
import datetime
# Импортируем библиотеку json
import json
# Импортируем клавиатуру
from vk_api.keyboard import VkKeyboard
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType

# Создаём переменную для  токена от группы

token="1d1698a3e7f848ae7b8966dd63d07c1e2458ce99d9317f03747c2bb5f75086f7298dfbc42064948753e07" # В ковычки вставляем аккуратно наш ранее взятый из группы токен.


# Подключаем токен и longpoll
bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)



# Создадим функцию для ответа на сообщения в лс группы
def blasthack(id, text, keyboard=None):
    post = {
    {'user_id' : id, 'message' : text, 'random_id': 0}
    }

    if keyboard != None:
        post['keyboard'] = keyboard.get_keyboard()
    else:
        post = post

    bh.method('messages.send', post)

# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      # Чтобы наш бот не слышал и не отвечал на самого себя
       if event.to_me:

        # Для того чтобы бот читал все с маленьких букв
          message = event.text.lower()
          # Получаем id пользователя
          id = event.user_id

    # Доисторическая логика общения на ифах
    # Перед вами структура сообщений на которые бот сможет ответить, elif можно создавать сколько угодно, if и else же могут быть только 1 в данной ситуации.
    # if - если, else - иначе(значит бот получил сообщение на которое не вызвана наша функция для ответа)

          if message == 'начать':
           blasthack(id, 'Привет,что хотели?!')

          elif message == 'питон':
             keyboard = VkKeyboard(one_time=False)
             keyboard.add_button('Питон')
             blasthack(id, 'https://www.youtube.com/watch?v=fp5-XQFr_nk')

          else:
               blasthack(id, 'Можете более понятнее выразиться')
