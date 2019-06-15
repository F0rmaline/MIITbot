from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Показать студак охраннику.')
source_markup_btn2 = types.KeyboardButton('Достать социальную карту и пройти через турникеты.')
source_markup.add(source_markup_btn1, source_markup_btn2)

responce_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
responce_markup_btn1 = types.KeyboardButton('Пойти медленно.')
responce_markup_btn2 = types.KeyboardButton('Пойти быстро.')
responce_markup.add(responce_markup_btn1, responce_markup_btn2)

responce2_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
responce2_markup_btn1 = types.KeyboardButton('Дойти до столовой в соседнем корпусе.')
responce2_markup_btn2 = types.KeyboardButton('Поискать еду в 8 корпусе.')
#responce2_markup_btn3 = types.KeyboardButton('Тортик...')
responce2_markup.add(responce2_markup_btn1, responce2_markup_btn2)

responce22_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
responce22_markup_btn1 = types.KeyboardButton('Яблоко.')
responce22_markup_btn3 = types.KeyboardButton('Тортик...')
responce22_markup.add(responce22_markup_btn1, responce22_markup_btn3)

responce3_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
responce3_markup_btn1 = types.KeyboardButton('Есть.')
responce3_markup_btn2 = types.KeyboardButton('Не есть.')
responce3_markup_btn3 = types.KeyboardButton('Отойти в сторону.')
responce3_markup.add(responce3_markup_btn1, responce3_markup_btn2, responce3_markup_btn3)

responce4_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
responce4_markup_btn1 = types.KeyboardButton('Съесть.')
responce4_markup_btn2 = types.KeyboardButton('Не надо.')
responce4_markup.add(responce4_markup_btn1, responce4_markup_btn2)

responce5_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
responce5_markup_btn1 = types.KeyboardButton('Finita la comedia!')
responce5_markup.add(responce5_markup_btn1)

responce6_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
responce6_markup_btn1 = types.KeyboardButton('Да!')
responce6_markup_btn2 = types.KeyboardButton('Хочу!')
responce6_markup.add(responce6_markup_btn1, responce6_markup_btn2)
