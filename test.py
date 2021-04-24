import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import pymysql.cursors
import requests

def getConnection():
    connection = pymysql.connect(host = 'sql11.freemysqlhosting.net',
                                 user='sql11407890',
                                 password='41AjFqjtlW',
                                 db='sql11407890',
                                 charset='utf8mb4',
                                 cursorclass=mymysql.cursors.DictCursor)
    return connection

vk_session = vk_api.VkApi(token="1d1698a3e7f848ae7b8966dd63d07c1e2458ce99d9317f03747c2bb5f75086f7298dfbc42064948753e07")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "204161431")
#Проверка действий
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        #Проверяем не пустое ли сообщение нам пришло
        if event.obj.text != '':
            #Проверяем пришло сообщение от пользователя или нет
            if event.from_user:
                #Отправляем сообщение
                vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=event.obj.text)
