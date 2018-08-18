import requests

import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from random import sample
from random import randint
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pickle
import os
import time
def main():

    session = requests.Session()
    login, password = '+79684381928', '12345678901123321Qqwsx'
    vk_session = vk_api.VkApi(login, password,app_id=5836937)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:

        return
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)

    answers1 = '''КТО МЕНЯ ПРИЗВАЛ?
    Начинаю поиск...
    Хм...
    Посмотрим...
    Активирована команда пидордня! Все в укрытие!
    Pidor police viehala!
    Сейчас поколудю...
    Шаманим-шаманим...
    Инициирую поиск пидора дня...
    System (pidor.py) was occured...
    Итак... кто же сегодня пидор дня?'''.splitlines()

    answers2 = '''Идет поиск...
    Почти у цели...
    Боже, чем я занимаюсь...
    Рассматриваем подозреваемых...
    Системы повреждены!
    Ведется поиск в базе данных...
    Звоним президенту...
    Смотрим расположение звезд...
    Сканирую...'''.splitlines()

    answers3 = '''Так, что тут у нас?
    Проверяю данные...
    ОГО-ГО!'''.splitlines()
    answers4 = '''Пидор дня обыкновенный, 1шт — 
    Ага! Поздравляю! Сегодня ты пидор — 
    Ну ты и пидор, 
    Анализ завершен. Ты пидор, 
    Что? Где? Когда? А ты пидор дня — 
    Стоять! Не двигаться! Вы объявлены пидором дня, 
    Кто бы мог подумать, но пидор дня — 
    Вжух! Ты пидор, '''.splitlines()



    for event in longpoll.listen():
        try:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

                forward_messagess = ''
                if event.from_chat == True:
                    userlist=vk.messages.getConversationMembers(peer_id=event.raw[3])
                    #print(userlist['profiles'][randint(0,len(userlist['profiles'])-1)]['id'])
                    #print(userlist['profiles'][randint(0, len(userlist['profiles']) - 1)])

                txt=event.text.split()

                for i in range(0, len(txt)):
                    txt[i] = txt[i].lower()

                if event.text.lower()=='ауе':
                    text='АУЕ'

                if event.text.lower()=='ауе тупа':
                    text='ТУПА АУЕ'

                if event.text.lower()=='тупа ауе':
                    text='АУЕ ТУПА'

                if event.text.lower() == 'слава украине':
                    text = 'ГЕРОЯМ СЛАВА'

                if event.text.lower() == 'нужны ли тян':
                    text = 'НЕТ'

                if txt[0] == 'инфа':
                    vrtnst = randint(0, 100)
                    if vrtnst == 100:
                        vrtnst = '💯'
                    forward_messagess = (str(event.raw[1]))
                    text = ('Вероятность: ' + str(vrtnst) + '%')

                if txt[0] == 'давайте':
                    text = ('Инициатива ебет инициатора')

                if txt[0] == 'блять':
                    text = ('Тянешь нас на дно еблан блять')

                if (txt[0] == 'что')and (txt[1] == 'по') and (txt[2] =='физике'):
                    text = ('VI CHTO NE DOLBITES’ V ZHOPU UJASSSSSS WI PERVIY FIZMAT WHO NE DOLBITSA')

                if txt[0] == 'альбина':
                    text = ('B O L S H O Y M O L O D E C')

                if txt.count('рома') !=0:
                    text = ('Эй @romhl (пидор) ')
                if txt.count('роман') !=0:
                    text = ('Эй @romhl (пидор) ')

                if txt[0] == 'пидорпомощь':
                    text = ('1. Для начала зарегистрируйся по команде "пидорег".\n '
                            '2. Дождись пока большинство зарегистрируется. \n '
                            '3. Запусти розыгрыш по команде "пидордня".\n '
                            '4. Просмотр статистики чата доступен по команде "пидортоп"\n'
                            '5. Просмотр личной статистики доступен по команде "пидоря"\n'
                            'РОЗЫГРЫШ ПРОХОДИТ РАЗ В ДЕНЬ ')

                if txt.count('пидоря') !=0:
                    if event.from_chat == True:
                        chatname = str(format(event.raw[3])) + '.pkl'
                        try:
                            input = open(chatname, 'rb')
                            sss = True
                        except FileNotFoundError:
                            text = 'Сначала нужно зарегистрироваться и провести один розыгрыш! Для помощи напиши пидорпомощь.'
                            sss = False
                        if sss:
                            obj = pickle.load(input)
                            input.close()
                            text = obj[event.user_id][0]+', ты был(а) пидором дня — '+str(obj[event.user_id][1])+' раз!'
                    else:
                        text='Данная функция работает только в беседах'

                if txt[0] == 'пидортоп':
                    if event.from_chat == True:
                        chatname = str(format(event.raw[3])) + '.pkl'
                        try:
                            input = open(chatname, 'rb')
                            sss = True
                        except FileNotFoundError:
                            text = 'Сначала нужно зарегистрироваться и провести один розыгрыш! Для помощи напиши пидорпомощь.'
                            sss = False
                        if sss:
                            obj = pickle.load(input)
                            input.close()
                            ob = list(obj.values())
                            ob = ob[1:]
                            ob.sort(key=lambda s: s[1], reverse=True)
                            top = 'Топ-10 пидоров за все время:'
                            if len(ob) < 10:
                                f = len(ob)
                            else:
                                f = 10
                            for i in range(1, f + 1):
                                top += '\n' + str(i) + '. ' + ob[-1 + i][0] + ' — ' + str(ob[-1 + i][1]) + ' раз(а)'

                            text = (top)
                    else:
                        text='Данная функция работает только в беседах'

                if txt[0] == 'кто' or txt[0] == 'кого':
                    if event.from_chat == True:
                        fff=randint(0, len(userlist['profiles']) - 1)
                        userlist = vk.messages.getConversationMembers(peer_id=event.raw[3])
                        forward_messagess=(str(event.raw[1]))
                        text = 'Мне кажется это ' +(userlist['profiles'][fff]['first_name']) +' '+ (userlist['profiles'][fff]['last_name'] )
                    else:
                        text = 'Данная функция работает только в беседах'

                if event.text.lower() == 'погода':
                    html_doc = urlopen('https://yandex.ru/pogoda/surgut').read()
                    soup = BeautifulSoup(html_doc, "html.parser")
                    gra = str(soup.find('span', "temp__value"))
                    gra = gra[:-7]
                    gra = gra[26:]
                    veter = str(soup('span', "wind-speed")[0])
                    veter = veter[:-7]
                    veter = veter[25:]
                    davlenie = str(soup('dd', "term__value")[3])
                    davlenie = davlenie.replace('<span class="fact__unit">', '').replace('</span></dd>', '').replace('<dd class="term__value">', '')
                    vlaga = str(soup('dd', "term__value")[4])
                    vlaga = vlaga[:-5]
                    vlaga = vlaga[24:]
                    voshod = str(soup('dd', "sunrise-sunset__value")[0]).replace('<dd class="sunrise-sunset__value">','').replace('</dd>', '')
                    zakat = str(soup('dd', "sunrise-sunset__value")[1]).replace('<dd class="sunrise-sunset__value">','').replace('</dd>', '')
                    text = ('🇷🇺 Сейчас в Сургуте ' + gra + '°C' '\n' + '💨 Ветер ' + veter + ' м/с' '\n' + '🌞 ' + voshod + ' 🌚 ' + zakat + '\n' + '🏧 ' + davlenie + '\n' +'💧 Влажность '+ vlaga)

                if txt[0] == 'пидорег':
                    if event.from_chat == True:
                        chatname=str(format(event.raw[3]))+'.pkl'
                        if not os.path.isfile(chatname):
                            output = open(chatname, 'wb')
                        input = open(chatname, 'rb')
                        try:
                            obj = pickle.load(input)
                        except EOFError:
                            obj={'date':[32,'']}
                        input.close()
                        if event.user_id in obj:
                            text="Эй, ты уже в игре!"
                        else:
                            imya = vk.users.get(user_ids=event.user_id)[0]['first_name'] +' '+ vk.users.get(user_ids=event.user_id)[0]['last_name']

                            obj[event.user_id]=[imya, 0]
                            output = open(chatname, 'wb')
                            pickle.dump(obj, output, 2)
                            output.close()
                            text='Регистрация прошла успешно'
                            imya=''
                    else:
                        text='Данная функция работает только в беседах'

                if txt[0] == 'пидордня':
                    if event.from_chat == True:
                        chatname = str(format(event.raw[3])) + '.pkl'
                        try:
                            input = open(chatname, 'rb')
                            sss = True
                        except FileNotFoundError:
                            text = 'Сначала нужно зарегистрироваться и провести один розыгрыш! Для помощи напиши пидорпомощь.'
                            sss = False
                        if sss:
                            obj = pickle.load(input)
                            input.close()
                            if obj['date'][0] == int(time.strftime("%d", time.gmtime())):
                                text = 'Согласно моей информации, по результатам сегодняшнего розыгрыша пидор дня — ' + obj['date'][1]
                            else:
                                random_list=[['date']]
                                while random_list[0][0]=='date':
                                    random_list = sample(obj.items(), len(obj))
                                vk.messages.send(
                                    chat_id=event.chat_id,
                                    message=(random.choice(answers1)))
                                time.sleep(1)

                                pidor = random_list[0][1][0]
                                pidorid = random_list[0][0]
                                vk.messages.send(
                                    chat_id=event.chat_id,
                                    message=(random.choice(answers2)))
                                time.sleep(2)
                                output = open(chatname, 'wb')
                                obj[pidorid][1] += 1
                                vk.messages.send(
                                    chat_id=event.chat_id,
                                    message=(random.choice(answers3)))
                                time.sleep(2)
                                obj['date'][0] = int(time.strftime("%d", time.gmtime()))
                                obj['date'][1] = pidor
                                pickle.dump(obj, output, 2)
                                output.close()
                                text = random.choice(answers4)+ "@id"+str(pidorid)+" (" +(pidor+")")
                    else:
                        text='Данная функция работает только в беседах'

                if txt[0] == 'нролл':

                    chatname = str(format(event.raw[3])) + 'roll' +'.pkl'
                    imya2 = vk.users.get(user_ids=event.user_id)[0]['first_name'] + ' ' + \
                            vk.users.get(user_ids=event.user_id)[0]['last_name'] + ' '
                    roll = [imya2, randint(0, 100)]
                    output = open(chatname, 'wb')
                    obj = {event.user_id: [roll]}
                    obj[event.user_id]
                    pickle.dump(obj,output,2)
                    output.close()
                    print(roll)

                    res=vk.messages.send(chat_id=event.chat_id, message=(('Результаты розыгрыша!\n 1. '+roll[0]+str(roll[1])).replace('0','0⃣').replace('1','1⃣').replace('2','2⃣').replace('3','3⃣').replace('4','4⃣').replace('5','5⃣').replace('6','6⃣').replace('7','7⃣').replace('8','8⃣').replace('9','9⃣')))

                if txt[0] == 'ролл':
                    chatname = str(format(event.raw[3])) + 'roll' + '.pkl'
                    input=open(chatname, 'rb')
                    obj=pickle.load(input)
                    if not event.user_id in obj:
                        texte = 'Результаты розыгрыша! \n'
                        imya2 = vk.users.get(user_ids=event.user_id)[0]['first_name'] + ' ' + \
                                vk.users.get(user_ids=event.user_id)[0]['last_name']+' '
                        roll = [imya2, randint(0, 100)]
                        obj[event.user_id]=roll
                        obj.sort(key=lambda s: s[1], reverse=True)
                        print(obj)
                        ob = list(obj.values())
                        for i in range(0,len(roll)):
                            texte+=str(i+1)+'. '+ob[i][0] + ob[i][1]+'\n'
                        texte=texte.replace('0','0⃣').replace('1','1⃣').replace('2','2⃣').replace('3','3⃣').replace('4','4⃣').replace('5','5⃣').replace('6','6⃣').replace('7','7⃣').replace('8','8⃣').replace('9','9⃣')
                        vk.messages.delete(peer_id=event.raw[3],message_ids=res,delete_for_all=1)
                        res=vk.messages.send(chat_id=event.chat_id, message=texte)
                        print(roll)


                if not text:
                    continue

                attachments = []


                if event.from_chat==True:
                    vk.messages.send(
                        chat_id=event.chat_id,

                        attachment=','.join(attachments),
                        message=text,
                        forward_messages=forward_messagess
                    )
                else:
                    vk.messages.send(
                        user_id=event.user_id,

                        attachment=','.join(attachments),
                        forward_messages=forward_messagess,
                        message=text
                    )

                text=''
        except Exception as owibka:
            vk.messages.send(
                user_id=103004558,
                message=owibka,
                forward_messages =(str(event.raw[1]))
            )
            pass

if __name__ == '__main__':
    main()