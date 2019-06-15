import telebot

import markups as m



bot = telebot.TeleBot('')


#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Здравствуй, дорогой друг! Ты попал в симулятор выживания студента. Твой герой плохо знает физику, поэтому он поступил в Гуманитарный институт МИИТ. Исход игры зависит только от тебя…Начнем!')
    bot.send_message(message.chat.id,'Студент подходит к КПП. Как пройти дальше?', reply_markup=m.source_markup)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text
    chat_id = message.chat.id
    if text == "Показать студак охраннику.":
        bot.send_message(chat_id, 'Ура! Ты преодолел первое испытание и попал на территорию университета. Взгляни на часы, ты опаздываешь! Тебе стоит поторопиться… (Warning! На улице зима)', reply_markup=m.responce_markup)
    if text == "Достать социальную карту и пройти через турникеты.":
        bot.send_message(chat_id, 'Ура! Ты преодолел первое испытание и попал на территорию университета. Взгляни на часы, ты опаздываешь! Тебе стоит поторопиться… (Warning! На улице зима)', reply_markup=m.responce_markup)

    if text == "Пойти медленно.":
            bot.send_message(chat_id, 'Разумное решение *звуки хлопков*')
            bot.send_message(chat_id, 'Вау! Мы внутри. Наконец-то можно пойти на увлекательные пары.')
            bot.send_message(chat_id, '*Прошло три пары*')
            bot.send_message(chat_id, 'Настало время обеда. Но что делать бедному студенту, который учится в 8 корпусе, где нет пункта питания?', reply_markup=m.responce2_markup)
    if text == "Пойти быстро.":
            bot.send_message(chat_id, 'О, нет! Ты упал, какааая жалость! Ох, было больно:(')
            bot.send_message(chat_id, 'Вау! Мы внутри. Наконец-то можно пойти на увлекательные пары.')
            bot.send_message(chat_id, '*Прошло три пары*')
            bot.send_message(chat_id, 'Настало время обеда. Но что делать бедному студенту, который учится в 8 корпусе, где нет пункта питания?', reply_markup=m.responce2_markup)
    if text == "Дойти до столовой в соседнем корпусе.":
        bot.send_message(chat_id, 'В столовой огромная очередь, ты опаздываешь на важную пару:(')
        bot.send_message(chat_id, 'Поздравляю, препод ненавидит тебя.')
        bot.send_message(chat_id, 'О, нет! Преподаватель сильно разозлился.Тебя отчисляют. So sad :(', reply_markup=m.responce5_markup)
        #bot.send_message(chat_id, 'Блаблабла2', reply_markup=m.responce3_markup)
    if text == "Поискать еду в 8 корпусе.":
        bot.send_message(chat_id, 'ЕДА!', reply_markup=m.responce22_markup)
    if text == "Яблоко.":
        bot.send_message(chat_id, 'ТЕБЕ ПОВЕЗЛО, ТЫ НАШЕЛ В МУСОРКЕ ЯБЛОКО!!!', reply_markup=m.responce3_markup)


    if text == "Есть.":
            bot.send_message(chat_id, 'Хехе, оно отравлено. Ты мертв:(', reply_markup=m.responce5_markup)
    if text == "Отойти в сторону.":
            bot.send_message(chat_id, 'Твой герой видит цветок. Можно ведь и его съесть…', reply_markup=m.responce4_markup)
    if text == "Не есть.":
            bot.send_message(chat_id, 'Ты голоден, но не пропускаешь важную пару. Это хорошая концовка. В качестве подарка можешь забрать кактус с подоконника домой!', reply_markup=m.responce5_markup)
    if text == "Съесть.":
            bot.send_message(chat_id,'Цветок был очень вкусным, но к сожалению ты умер от наслаждения :( (Мне не жаль)')
            bot.send_message(chat_id, 'ХА-ХА', reply_markup=m.responce5_markup)
    if text == "Не надо.":
            bot.send_message(chat_id, 'Ты остался голодным, но попал на важную пару. Препод любит тебя <3', reply_markup=m.responce5_markup)
    if text == "Тортик...":
            bot.send_message(chat_id, 'Находишь странную дверь с надписью « Вечеринка с тортом». ( Мне кажется, что стоит зайти, хочешь тортик?)')
            bot.send_message(chat_id, 'Открываешь дверь...')
            bot.send_message(chat_id, 'Прости, это была ловушка. Какая жалость. Ты мертв.', reply_markup=m.responce5_markup)

    if text == "Finita la comedia!":
            bot.send_message(chat_id, 'Можно перемотать жизнь и переиграть заново. Хочешь?', reply_markup=m.responce6_markup)

    if text == "Да!":
        bot.send_message(message.chat.id,
                         'Здравствуй, дорогой друг! Ты попал в симулятор выживания студента. Твой герой плохо знает физику, поэтому он поступил в Гуманитарный институт МИИТ. Исход игры зависит только от тебя…Начнем!')
        bot.send_message(message.chat.id, 'Студент подходит к КПП. Как пройти дальше?', reply_markup=m.source_markup)

    if text == "Хочу!":
        bot.send_message(message.chat.id,
                         'Здравствуй, дорогой друг! Ты попал в симулятор выживания студента. Твой герой плохо знает физику, поэтому он поступил в Гуманитарный институт МИИТ. Исход игры зависит только от тебя…Начнем!')
        bot.send_message(message.chat.id, 'Студент подходит к КПП. Как пройти дальше?', reply_markup=m.source_markup)

    if text == "Иди нахуй":
            bot.send_message(chat_id, 'Го ты сам нахуй')

    if text == "Хочу зачет автоматом":
            bot.send_message(chat_id, 'Александр Владимирович, ну поставьте, пожалуйста')






@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво!')


bot.polling(none_stop=True)
