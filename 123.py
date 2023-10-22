import vk_api
from random import choice, randrange, random
from vk_api.longpoll import VkLongPoll, VkEventType
TOKEN = 'vk1.a.InXZp6twCvl951gAcCDIf1tGD4RWSiqSGjpF1ErdqeXjF2OE5KGK12mHUAq-1iD9iKgGI461EtxWkOvFVZ_WhEuwqb8zHsCabDvxwahMcaJHZME_X3eXf62Di-EzRNme5LrX-OPRm-t7grt_xO3aVXXDLRrHrGlsiBcL4CHWEO_QZcBhKtBVTQodZCwYNA63I4zzeD0yk1n7ju-DeBnxhw'
vk_sesion = vk_api. VkApi(token = TOKEN)

longpoll = VkLongPoll(vk_sesion)
vk = vk_sesion.get_api()

Vars = ['камень', 'ножницы', 'бумага']
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and str(event.text).lower() in Vars:
        if event.from_user:
            user = str(event.text).lower()
            bot = choice(Vars)
            vk.messages.send(user_id=event.user_id, message=choice(Vars), random_id = randrange(1, 100000))
            answer = event.text
            cut = None
            if bot == 'ножницы':
                if user == 'ножницы':
                    cut = 'Ничья'
                elif user == 'бумага':
                    cut = 'Ты проиграл лошара'
                elif user == 'камень':
                    cut = 'Лээээ! У тебя нет права выигрывать'
            elif bot == 'бумага':
                if user == 'бумага':
                    cut = 'Ничья'
                elif user == 'камень':
                    cut = 'Ты проиграл лошара'
                elif user == 'ножницы':
                    cut = 'Лээээ! У тебя нет права выигрывать'
            elif bot == 'камень':
                if user == 'камень':
                    cut = 'Ничья'
                elif user == 'ножницы':
                    cut = 'Ты проиграл лошара'
                elif user == 'бумага':
                    cut = 'Лээээ! У тебя нет права выигрывать'
            vk.messages.send(user_id=event.user_id, message=cut, random_id=randrange(1, 100000))