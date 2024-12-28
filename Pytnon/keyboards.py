from aiogram import types

from db import Institutes

back_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton("Назад")
back_keyboard.add(back_button)

back_inline_keyboard = types.InlineKeyboardMarkup()
back_inline_keyboard.add(types.InlineKeyboardButton("Back", callback_data="404"))

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Задать вопрос виртуальному ассистенту")
button2 = types.KeyboardButton("Подача заявления")
button3 = types.KeyboardButton("Календарь приема")
button4 = types.KeyboardButton("ЕГЭ")
button5 = types.KeyboardButton("Другое")
button6 = types.KeyboardButton("FAQ")
button7 = types.KeyboardButton("Направления подготовки")
start_keyboard.add(button1)
start_keyboard.add("Направления подготовки")
start_keyboard.row( button4, button5, button6)
start_keyboard.add(button2, button3)

submittting_aplication_keyboard = types.ReplyKeyboardMarkup()
submittting_aplication_buttons = [
    types.KeyboardButton("✏️Образцы документов для заполнения✏️"),
    types.KeyboardButton("📍Как пройти к комиссии?📍"),
    types.KeyboardButton("Дополнительные баллы при зачислении"),
    types.KeyboardButton("📞Контакты комиссии?📞"),
    types.KeyboardButton("Какие документы нужны для поступления?")
]
for button in submittting_aplication_buttons:
    submittting_aplication_keyboard.add(button)
submittting_aplication_keyboard.add(back_button)

document_examples_keyboard = types.InlineKeyboardMarkup()
document_examples_buttons = [
    types.InlineKeyboardButton("Очное", callback_data="och"),
    types.InlineKeyboardButton("Очно-заочное", callback_data="zaoch"),
    types.InlineKeyboardButton("Вечернее", callback_data="ev")
]
for button in document_examples_buttons:
    document_examples_keyboard.add(button)

reception_calendar_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
reception_calendar_buttons = [
    types.KeyboardButton("Бюджет"),
    types.KeyboardButton("Контракт"),
    types.KeyboardButton("По квоте"),
]
reception_calendar_keyboard.row(*reception_calendar_buttons)
reception_calendar_keyboard.row(types.KeyboardButton("Даты проведения олимпиад"))
reception_calendar_keyboard.row(types.KeyboardButton("Дни открытых дверей"))
reception_calendar_keyboard.add(back_button)



other_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
other_keyboard.row(types.KeyboardButton("Общежития"), types.KeyboardButton("Льготное"))
other_keyboard.row(types.KeyboardButton("Военная кафедра"), types.KeyboardButton("Воинский учет"))
other_keyboard.row(back_button)


dormitories_keyboard = types.ReplyKeyboardMarkup()
dormitories_buttons = [
    types.KeyboardButton("Какие общежития есть?"),
    types.KeyboardButton("Документы для общежития"),
    types.KeyboardButton("По какому принципу дают общежитие"),
    types.KeyboardButton("Условия предоставления общежития"),
    back_button
]
for button in dormitories_buttons:
    dormitories_keyboard.add(button)


dormitories_geo_keyboard = types.InlineKeyboardMarkup()
dormitories_geo_buttons = [
    types.InlineKeyboardButton("пр. Маршала Жукова, д. 24", callback_data="1"),
    types.InlineKeyboardButton("ул. Передовиков, д. 13", callback_data="2"),
    types.InlineKeyboardButton("ул. Варшавская, д. 8", callback_data="3"),
    types.InlineKeyboardButton("MCГ", callback_data="4"),
    types.InlineKeyboardButton("на ул. Кузнецовской", callback_data="5")
]
for button in dormitories_geo_buttons:
    dormitories_geo_keyboard.add(button)


lgotnoe_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
lgotnoe_keyboard.add(types.KeyboardButton("Кто может претендовать?"), types.KeyboardButton("Какие документы нужно предоставить?"))
lgotnoe_keyboard.add(back_button)


military_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
military_buttons = [
    types.KeyboardButton("Как поступить на военную кафедру?"),
    types.KeyboardButton("Когда заканчивается срок приёма документов?"),
    types.KeyboardButton("Какие нормативы нужно пройти для поступления?"),
    types.KeyboardButton("Какие документы нужны для поступления на военную кафедру?"),
    types.KeyboardButton("Какие документы нужно предоставить военкомату?"),
    back_button
]
for button in military_buttons:
    military_keyboard.add(button)


military_state_keyboard = types.ReplyKeyboardMarkup()
military_state_buttons = [
    types.KeyboardButton("Нужно ли предоставлять приписное удостоверение или военный билет при подаче документов и для зачисления на 1 курс?"),
    types.KeyboardButton("Как найти второй отдел?"),
    types.KeyboardButton("В процессе зачисления или сразу после него нужно ли сниматься с учета в военкомате по месту регистрации?"),
    types.KeyboardButton("Какие документы нужно предоставить военкомату/ второму отделу?"),
    types.KeyboardButton("Как встать на воинский учёт?"),
    back_button
]
for button in military_state_buttons:
    military_state_keyboard.add(button)



faq_keyboard = types.ReplyKeyboardMarkup()
faq_buttons = [
    types.KeyboardButton("Нужен ли мед осмотр?"),
    types.KeyboardButton("Нужна ли справка 086-У?"),
    types.KeyboardButton("Сколько баллов ЕГЭ по предмету необходимо набрать, чтобы воспользоваться правом поступления «без вступительных испытаний»?"),
    types.KeyboardButton("Если одинаковое количество баллов?"),
    types.KeyboardButton("Можно ли перевестись на бюджет с платного?"),
    types.KeyboardButton("Что делать если нет отчества?"),
    types.KeyboardButton("Имеет ли значение дата подачи заявления при одинаковых баллах?"),
    types.KeyboardButton("Как проходит конкурс?"),
    types.KeyboardButton("Какие есть формы обучения?"),
    back_button
]
for button in faq_buttons:
    faq_keyboard.add(button)



institutes_keyboard = types.InlineKeyboardMarkup()
instittuteDB = Institutes()
names = instittuteDB.get_names()
for i in range(len(names)):
    institutes_keyboard.add(types.InlineKeyboardButton(f"{names[i][0]}", callback_data=f'{i+1}'))
institutes_keyboard.add(types.InlineKeyboardButton("Назад", callback_data="404"))


ege_keyboard = types.InlineKeyboardMarkup()

ege_keyboard.add(types.InlineKeyboardButton(f"Базовый", callback_data=f"answer_1"))
ege_keyboard.add(types.InlineKeyboardButton(f"Профильный", callback_data=f"answer_2"))



subject_keyboard = types.InlineKeyboardMarkup()
subjects = [
    "Иностранный язык",
    "Литература",
    "Обществознание",
    "История",
    "География",
    "Биология",
    "Химия",
    "Физика",
    "Информатика"
]
for sub in subjects:
    subject_keyboard.add(types.InlineKeyboardButton(sub, callback_data=sub))