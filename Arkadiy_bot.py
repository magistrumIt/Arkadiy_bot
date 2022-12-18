#Ass We Can          # Талисман кода 




# Импорт библиотек
import webbrowser  # Библиотека для создания ссылок
from random import randint as r # Библиотека для генерации случайных чисел
from random import choice as c
import telebot # Библиотека для создания Telegram-бота
from telebot import types # Библиотека для создания inline кнопок



# Определение переменных и списков
answer = '' # Переменная для ответов 

gulugulu = 'www.google.ru/search?q=' # Переменные для обозначения поисковых систем 
yop_yan =  'yandex.ru/search/?text='
mail = 'go.mail.ru/search?q='
bing = 'www.bing.com/search?q='
ram = 'nova.rambler.ru/search?utm_source=head&utm_campaign=self_promo&utm_medium=form&utm_content=search&query='
yahoo = 'search.yahoo.com/search?p='

link_list = [gulugulu, yop_yan, mail, bing, ram, yahoo] # Список для перебора поисковых систем

inter = [] # Список интересов

ind_cats_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # Список для перебора фотографий котиков

poisk = 0 # Переменные для функции <<Поиск>> 
isk = ''
poisk_sis_list = ['/1 - Поиск в Google', '/2 - Поиск в Яндекс', '/3 - Поиск в Mail', '/4 - Поиск в Bing', '/5 - Поиск в Rambler', '/6 - Поиск в Yahoo']
poisk_sis_list_com = ['Google', 'Яндекс', 'Mail', 'Bing', 'Rambler', 'Yahoo']
ind_poisk_list = ['1', '2', '3', '4', '5', '6']

news =  'news.yandex.ru/news/' # Переменная для новостей 

region = '' # Переменная для региона погоды 

facts = ["Бот создавался на протяжении более чем 1-го месяца", "Бот имеет 480 строчек кода", "Бот написан на языке программирования Python", "В создании бота принимал участие сам Тима и Джоооооо Байден", "Вассал моего вассала - не мой вассал!", "На самом деле это Леша открыл Америку, подсказал Ньютону его 1-й закон и подсчитал сколько хромосом у Тимы (47)", "Никакие бренды, даже наш любимый Авиасейлс, с самыми дешевыми билетами, не платили нам за рекламу ):", "Бот создан в память о сбитом режиме сна Тимы (Спи спокойно. Аминь)", "Иван Михайлович не хочет отдавать нам наши паспорта", "Этот факт был придуман в подвале (помогите!!!)"]

reklama = ['www.aviasales.ru', 'tlauncher.org', '1xbet.onl', 'magistrumclub.ru'] # Список реклам


bot = telebot.TeleBot('5134589338:AAHU5juRtZ9pD2Jyesz8yILmOrp8YpTHKIQ') # API ключ бота 
keyboard = types.InlineKeyboardMarkup() # Переменная для inline кнопок



@bot.message_handler(commands=["start"]) # Команда для запуска бота 
def start(m, res=False): # Функция срабатывающая при старте 
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ваши интересы") # Определение кнопок
        item2=types.KeyboardButton("Авиасейлс")
        item3=types.KeyboardButton("Котики")
        item4=types.KeyboardButton("Поиск")
        item5=types.KeyboardButton("Новости")
        item6=types.KeyboardButton("Погода")
        item7=types.KeyboardButton("Информация о боте")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        key_izmen_inter = types.InlineKeyboardButton(text='Изменить список интересов', callback_data='izmen_inter')
        keyboard.add(key_izmen_inter)
        key_inter1 = types.InlineKeyboardButton(text= '1-й интерес', callback_data='inter1')
        keyboard.add(key_inter1)
        key_inter2 = types.InlineKeyboardButton(text= '2-й интерес', callback_data='inter2')
        keyboard.add(key_inter2)
        key_inter3 = types.InlineKeyboardButton(text= '3-й интерес', callback_data='inter3')
        keyboard.add(key_inter3)

        bot.send_message(m.chat.id, 'Бордюр, мадама. Щто привело тебя сюда, уважаемая?',  reply_markup=markup) # Фраза встречающая пользователя после комманды /start


@bot.message_handler(commands=["1"]) # Команда для поиска в Google
def poisk1(m, res=False): # Функция для обработки команды по поику в Google
    global answer, poisk # Глобализация переменных(встречается в некоторых функциях)
    
    poisk = 1 # Запись номера поисковой системы в переменную
    answer = "Теперь напиши искомое и я найду его в " + poisk_sis_list_com[0] + " (если есть пробел, пожалуйста заменяйте на +)"

    bot.send_message(m.chat.id, answer)
    bot.register_next_step_handler(m, isk_fun)


@bot.message_handler(commands=["2"]) # Команда для поиска в Яндекс
def poisk2(m, res=False): # Функция для обработки команды по поику в Яндекс
    global answer, poisk 
    
    poisk = 2
    answer = "Теперь напиши искомое и я найду его в " + poisk_sis_list_com[1] + " (если есть пробел, пожалуйста заменяйте на +)"

    bot.send_message(m.chat.id, answer)
    bot.register_next_step_handler(m, isk_fun)


@bot.message_handler(commands=["3"]) # Команда для поиска в Mail
def poisk3(m, res=False): # Функция для обработки команды по поику в Mail
    global answer, poisk 
    
    poisk = 3
    answer = "Теперь напиши искомое и я найду его в " + poisk_sis_list_com[2] + " (если есть пробел, пожалуйста заменяйте на +)"

    bot.send_message(m.chat.id, answer)
    bot.register_next_step_handler(m, isk_fun)


@bot.message_handler(commands=["4"]) # Команда для поиска в Bing
def poisk4(m, res=False): # Функция для обработки команды по поику в Bing
    global answer, poisk 
    
    poisk = 4
    answer = "Теперь напиши искомое и я найду его в " + poisk_sis_list_com[3] + " (если есть пробел, пожалуйста заменяйте на +)"

    bot.send_message(m.chat.id, answer)
    bot.register_next_step_handler(m, isk_fun)


@bot.message_handler(commands=["5"]) # Команда для поиска в Rambler
def poisk5(m, res=False): # Функция для обработки команды по поику в Rambler
    global answer, poisk 
    
    poisk = 5
    answer = "Теперь напиши искомое и я найду его в " + poisk_sis_list_com[4] + " (если есть пробел, пожалуйста заменяйте на +)"

    bot.send_message(m.chat.id, answer)
    bot.register_next_step_handler(m, isk_fun)


@bot.message_handler(commands=["6"]) # Команда для поиска в Yahoo
def poisk6(m, res=False): # Функция для обработки команды по поику в Yahoo
    global answer, poisk 
    
    poisk = 6
    answer = "Теперь напиши искомое и я найду его в " + poisk_sis_list_com[5] + " (если есть пробел, пожалуйста заменяйте на +)"

    bot.send_message(m.chat.id, answer)
    bot.register_next_step_handler(m, isk_fun)


@bot.message_handler(commands=["joke"]) # Команда для повествования шутки
def joke(m, res=False): # Функция для обработки команды по повествованию шутки
    global answer
    
    answer = "Шутка - это ТЫ!"

    bot.send_message(m.chat.id, answer)



@bot.message_handler(content_types=["text"]) # Команда для получения текста   
def menu(message): # Функция для обработки основных кнопок 
    global answer 

    if message.text.strip() == 'Ваши интересы': # Если пользователь выбрал <<Ваши интересы>>
        if len(inter) == 0: # Если интересов нет, то переход в функцию по добавлению 1-го интереса 
            answer = "У вас пока нет интересов, напиши ниже и я его запомню) (если есть пробел, пожалуйста заменяйте на +)" # Определение переменной для ответа (встречается везде, где нужен ответ)
            bot.send_message(message.chat.id, answer) # Отправка переменной answer, в которой находиться ответ (встречается везде, где нужен ответ)
            bot.register_next_step_handler(message, dobav_inter) # Команда для переключения на следующую функцию (встречается везде, где нужен переход)
        
        else: # При оставшихся случаях 
            answer = "Выбери"
            bot.send_message(message.chat.id, answer)

            key_izmen_inter = types.InlineKeyboardButton(text='Изменить список интересов', callback_data='izmen_inter') #Показ инлайн кнопок 
            key_inter1 = types.InlineKeyboardButton(text= '1-й интерес', callback_data='inter1')
            key_inter2 = types.InlineKeyboardButton(text= '2-й интерес', callback_data='inter2')
            key_inter3 = types.InlineKeyboardButton(text= '3-й интерес', callback_data='inter3')

            answer = "1-й - " + inter[0] # Под каким номером, какой интерес 
            bot.send_message(message.chat.id, answer)

            if len(inter) >= 2: 
                answer = "2-й - " + inter[1]
                bot.send_message(message.chat.id, answer)

            if len(inter) >= 3:
                answer = "3-й - " + inter[2]
                bot.send_message(message.chat.id, answer)
 
            bot.send_message(message.from_user.id, answer, reply_markup=keyboard) # Обработка inline клавиатуры 


    elif message.text.strip() == 'Авиасейлс': # АВИАСЕЙЛС  
        answer = 'https://{}'.format(reklama[0]) + ' - поиск дешёвых авиабилетов'
        bot.send_message(message.chat.id, answer)
      
      
    elif message.text.strip() == 'Котики': # КОТИКИ 
        cats_r = 0 # Переменная для выбора случайной фотки котика
        run_cats = True #Определение переменной run_... для цикла с перебором (встречается везде, где нужен перебор)
        ind_cats_int = 0 #Определение переменной ind_... для цикла с перебором (встречается везде, где нужен перебор)
        
        cats_r = r(0, 9) # Выбор случайной фотки котика 
        
        while run_cats: # Цикл с перебором
            if cats_r == ind_cats_int:
                bot.send_photo(message.chat.id, open('cat' + ind_cats_list[ind_cats_int] + '.jpg', 'rb')) # Показ котика 
            
            if ind_cats_int == 9: # Выход из цикла, если перебор окончен (встречается везде, где нужен выход из перебора)
                run_cats = False
            
            ind_cats_int += 1 # Переход на следуюший пунк перебора (встречается везде, где нужен переход на следуюший пунк перебора)   
       
       
    elif message.text.strip() == 'Поиск': # Если пользователь выбрал <<Поиск>>
        run_poisk = True 
        ind_poisk = 0 
        
        answer = "Ты можешь командами вызывать поиск в той или иной поисковой системе в любой момент не нажимая <<Поиск>> (команды начинаются с /)"
        bot.send_message(message.chat.id, answer)

        while run_poisk: 
            answer = poisk_sis_list[ind_poisk] # Показ возможных поисковых систем 
            bot.send_message(message.chat.id, answer)
            
            if ind_poisk == 5:
                run_poisk = False
            
            ind_poisk += 1 


    elif message.text.strip() == 'Новости': # Если пользователь выбрал <<Новости>>   
        answer = "Самые свежие новости, честно: " + 'https://{}'.format(news) # Создание и отправка ссылки на новости
        bot.send_message(message.chat.id, answer)
        
        answer = "Выберите пункт снизу"
        bot.send_message(message.chat.id, answer)

        answer = "Рекламная пауза: " + c(reklama) # Случайная реклама (встречается в конце функций, которые выдают ссылки)
        bot.send_message(message.chat.id, answer)
    
    
    elif message.text.strip() == 'Погода':   # Если пользователь выбрал <<Погода>>
        if region == '': # Если регион не выбран 
            answer = 'Напишите регион, в котором хотите узнать погоду, и я запомню его ДО КОНЦА ТВОИХ ДНЕЙ (если есть пробел, пожалуйста заменяйте на +)'
            bot.send_message(message.chat.id, answer)
            
            bot.register_next_step_handler(message, region_fun) # Переход в функцию по добавлению региона 
            
        else: # Если регион уже выбран 
            answer = 'Нажмите <<Погода>> ещё раз, если хотиту узнать погоду в регионе ' + region + '. Иначе впишите новый регион'
            bot.send_message(message.chat.id, answer)
            
            bot.register_next_step_handler(message, pogoda) # Переход в функцию по подтверждению региона         
      
      
    elif message.text.strip() == 'Информация о боте': # Если пользователь выбрал <<Информация о боте>> 
        answer = c(facts) # Выбор и вывод случайного факта о боте 
        bot.send_message(message.chat.id, answer)
        
        answer = "Рекламная пауза: " + c(reklama)
        bot.send_message(message.chat.id, answer)


def izmen_inter(message): # Функция по изменению списка интересов 
    global answer

    if message.text.strip() == '1': # Проверка номера выбранного пункта 
        answer = "Напиши интерес, который будет под 1-м номером (если есть пробел, пожалуйста заменяйте на +)"
        bot.send_message(message.chat.id, answer)
        bot.register_next_step_handler(message, izmen_inter1) # Переход в функцию по изменению этого интереса 
    
    elif message.text.strip() == '2':
        answer = "Напиши интерес, который будет под 2-м номером (если есть пробел, пожалуйста заменяйте на +)"
        bot.send_message(message.chat.id, answer)
        bot.register_next_step_handler(message, izmen_inter2)

    elif message.text.strip() == '3':
        if len(inter) <= 1: # Проверка длинны списка интересов 
            answer = "Ты не можешь добавлять 3-й интерес, пока нет 2-го. Я добавлю " + message.text.strip() + " на 2-е место" # Перестановка с 3-го на 2-е место 
            bot.send_message(message.chat.id, answer)
            
            answer = "Напиши интерес, который будет под 2-м номером (если есть пробел, пожалуйста заменяйте на +)"
            bot.send_message(message.chat.id, answer)
            bot.register_next_step_handler(message, izmen_inter2)

        else:
            answer = "Напиши интерес, который будет под 3-м номером (если есть пробел, пожалуйста заменяйте на +)"
            bot.send_message(message.chat.id, answer)
            bot.register_next_step_handler(message, izmen_inter3)


def izmen_inter1(message): # Функции по изменению интереса под определённым номером 
    inter[0] = message.text.strip() # Добавление интереса в список интересов под оределенный номер
    
    answer = inter[0] + ", я запомню :)" # Запоминание нового интереса
    bot.send_message(message.chat.id, answer)
    answer = "Выберите пункт снизу"
    bot.send_message(message.chat.id, answer)
    
    answer = "Рекламная пауза: " + c(reklama)
    bot.send_message(message.chat.id, answer)


def izmen_inter2(message):
    if len(inter) <= 1: # Проверка длинны списка интересов 
        inter.append(message.text.strip())
    
    else:
        inter[1] = message.text.strip()
    
    answer = inter[1] + ", я запомню :)"
    bot.send_message(message.chat.id, answer)
    answer = "Выберите пункт снизу"
    bot.send_message(message.chat.id, answer)
    
    answer = "Рекламная пауза: " + c(reklama)
    bot.send_message(message.chat.id, answer)


def izmen_inter3(message):
    if len(inter) <= 2:
        inter.append(message.text.strip())
    
    else:
        inter[2] = message.text.strip()
    
    answer = inter[2] + ", я запомню :)"
    bot.send_message(message.chat.id, answer)
    answer = "Выберите пункт снизу"
    bot.send_message(message.chat.id, answer)
    
    answer = "Рекламная пауза: " + c(reklama)
    bot.send_message(message.chat.id, answer)


def dobav_inter(message): # Функция по добавлению первого интереса 
    global answer
    
    inter.append(message.text.strip())
    answer = "Ваш интерес добавлен"
    bot.send_message(message.chat.id, answer)
    answer = "Выберите пункт снизу"
    bot.send_message(message.chat.id, answer)
    
    answer = "Рекламная пауза: " + c(reklama)
    bot.send_message(message.chat.id, answer)


def isk_fun(message): # Функция по запросу искомово 
    run_isk = True
    ind_isk = 0
    
    while run_isk:
        if poisk == int(ind_poisk_list[ind_isk]): # Проверка выбора поисковой системы 
            answer = 'https://{}'.format(link_list[ind_isk] + message.text.strip())
            bot.send_message(message.chat.id, answer)

        if ind_isk == 5:
            run_isk = False

        ind_isk += 1

    answer = "Выберите пункт снизу"
    bot.send_message(message.chat.id, answer)
    
    answer = "Рекламная пауза: " + c(reklama)
    bot.send_message(message.chat.id, answer)


def pogoda(message): # Функция по выбору региона где пользоваетель ищет погоду 
    global region
    
    if message.text.strip() == "Погода":  # Подтверждение старого региона 
        answer = "Самая свежая погода в населённом пункте " + region + ", честно: " + 'https://{}'.format(yop_yan + "погода+" + region)
        bot.send_message(message.chat.id, answer)
       
    else: # Запись нового региона 
        region = message.text.strip()
        answer = "Самая свежая погода в населённом пункте " + region + ", честно: " + 'https://{}'.format(yop_yan + "погода+" + region)
        bot.send_message(message.chat.id, answer)
    
    answer = "Выберите пункт снизу"
    bot.send_message(message.chat.id, answer)
            
    answer = "Рекламная пауза: " + c(reklama)
    bot.send_message(message.chat.id, answer)


def region_fun(message): # Функция по добавления самого первого региона где пользователь ищет погоду 
    global region 
    
    region = message.text.strip()
    
    answer = region + ' , я запомню ;)'
    bot.send_message(message.chat.id, answer)
    
    answer = "Выберите пункт снизу"
    bot.send_message(message.chat.id, answer)
            
    answer = "Рекламная пауза: " + c(reklama)
    bot.send_message(message.chat.id, answer)



@bot.callback_query_handler(func=lambda call: True) # Команда обработки инлайн кнопок 
def callback_worker(call): # Функция по обработки инлайн кнопок 
    global answer

    if call.data == "inter1": # Проверка выбора номера интереса 
        answer = inter[0] # Показ пользователю какой интерес был выбран
        bot.send_message(call.message.chat.id, answer)
        
        run_inter = True
        ind_inter = 0

        while run_inter:
            answer = 'https://{}'.format(link_list[ind_inter] + inter[0]) # Открытие интереса в 6-ти разных поисковых системах 
            bot.send_message(call.message.chat.id, answer)

            if ind_inter == 5:
                run_inter = False
        
            ind_inter += 1

        answer = "Рекламная пауза: " + c(reklama)
        bot.send_message(call.message.chat.id, answer)

    elif call.data == "inter2": 
        if len(inter) >= 2: # Проверка длинны списка интересов
            answer = inter[1]
            bot.send_message(call.message.chat.id, answer)
        
            run_inter = True
            ind_inter = 0

            while run_inter:
                answer = 'https://{}'.format(link_list[ind_inter] + inter[1])
                bot.send_message(call.message.chat.id, answer)

                if ind_inter == 5:
                    run_inter = False
        
                ind_inter += 1
        
            answer = "Рекламная пауза: " + c(reklama)
            bot.send_message(call.message.chat.id, answer)

        else: # Обработка ошибки по недостатку интересов 
            answer = "У вас пока что нет 2-го интереса. Нажмини кнопку <<Изменить список интересов>>, чтобы добавить 2-й интерес"
            bot.send_message(call.message.chat.id, answer)

    elif call.data == "inter3":
        if len(inter) >= 3:
            answer = inter[2]
            bot.send_message(call.message.chat.id, answer)
        
            run_inter = True
            ind_inter = 0

            while run_inter:
                answer = 'https://{}'.format(link_list[ind_inter] + inter[2])
                bot.send_message(call.message.chat.id, answer)

                if ind_inter == 5:
                    run_inter = False
        
                ind_inter += 1
        
            answer = "Рекламная пауза: " + c(reklama)
            bot.send_message(call.message.chat.id, answer)

        else: 
            answer = "У вас пока что нет 3-го интереса. Нажмини кнопку <<Изменить список интересов>>, чтобы добавить 3-й интерес"
            bot.send_message(call.message.chat.id, answer)


    elif call.data == "izmen_inter": # Проверка нажатия кнопки <<Изменить список интересов>>
        answer = "Напиши номер какого интереса ты хочешь поменять(добавить) (1 - 3)"
        bot.send_message(call.message.chat.id, answer)
        bot.register_next_step_handler(call.message, izmen_inter) # Переход в функцию по изменению списка интересов



bot.polling(none_stop=True, interval=0) # Запуск бота 