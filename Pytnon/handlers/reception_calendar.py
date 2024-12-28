from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import reception_calendar_keyboard, start_keyboard
from states import ReceptionCalendarStates, MenuStates
from db import EnterCalendar



async def reception_calendar_menu(message: types, state: FSMContext):
    await ReceptionCalendarStates.MENU.set()
    await message.answer("Выберете дейсвие:", reply_markup=reception_calendar_keyboard)


async def process_reception_calendar_menu(message: types, state: FSMContext):
    if message.text == "Дни открытых дверей":
        await bot.send_message(message.chat.id, "📅 14 марта\n"
                                                "в официальной группе VK (дистанционно)\n\n"
                                                "📅31 марта 12:00\n"
                                                "Ленсовета 14, актовый зал\n\n"
                                                "📅11 апреля\n"
                                                "в официальной группе VK (дистанционно)\n\n"
                                                "📅21 апреля 12:00\n"
                                                "Ленсовета 14, актовый зал\n\n"
                                                "📅19 мая 12:00\n"
                                                "Ленсовета 14, актовый зал)")


    if message.text == "Даты проведения олимпиад":
        await bot.send_message(message.chat.id, "🔹 Аэрокосмические олимпиады ГУАП\n"
                                                "🔹 43-я международная конференция «Школьная информатика и проблемы устойчивого развития»\n"
                                                "🔹 Объединённая межвузовская математическая олимпиада школьников — ОММО 2024\n"
                                                "🔹 Олимпиада школьников «Шаг в будущее»\n")

    if message.text == "Бюджет":
        enter_calendarDB = EnterCalendar()
        calendar = enter_calendarDB.get_budget()
        result = 'Календарь приема:\n\n'
        for entry in calendar:
            if entry[0] != None or entry[1] != None:
                result += f"📅 {entry[0]} 📅\n{entry[1]}\n\n"

        await bot.send_message(message.chat.id, result)

    if message.text == "Контракт":
        enter_calendarDB = EnterCalendar()
        calendar = enter_calendarDB.get_contract()
        result = 'Календарь приема:\n\n'
        for entry in calendar:
            if entry[0] != None or entry[1] != None:
                result += f"📅 {entry[0]} 📅\n{entry[1]}\n\n"

        await bot.send_message(message.chat.id, result)

    if message.text == "По квоте":
        enter_calendarDB = EnterCalendar()
        calendar = enter_calendarDB.get_kvot()
        result = 'Календарь приема:\n\n'
        for entry in calendar:
            if entry[0] != None or entry[1] != None:
                result += f"📅 {entry[0]} 📅\n{entry[1]}\n\n"

        await bot.send_message(message.chat.id, result)



    if message.text == "Назад":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:", reply_markup=start_keyboard)





