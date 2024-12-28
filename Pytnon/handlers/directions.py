from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import start_keyboard, institutes_keyboard, back_keyboard, back_inline_keyboard
from states import MenuStates, DirectonsStates
from db import Institutes, Directions, Focus


async def directions_menu(message: types, state: FSMContext):
    await DirectonsStates.MENU.set()
    await bot.send_message(message.chat.id, "Вы находитесь в меню обзора направлений!",
                           reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(message.chat.id, "🏢 Выберете институт(факультет):", reply_markup=institutes_keyboard)


async def process_directions_menu(callback_query: types.CallbackQuery, state: FSMContext):
    instituteDB = Institutes()
    institutes_ids = instituteDB.get_ids()
    if (int(callback_query.data),) in institutes_ids:
        await DirectonsStates.DIRECTIONS.set()
        directionDB = Directions()
        directions = directionDB.get_names_by_institute(callback_query.data)
        directions_keyboard = types.InlineKeyboardMarkup()
        for i in range(len(directions)):
            directions_keyboard.add(types.InlineKeyboardButton(directions[i][0], callback_data=f'{i + 1}'))
        directions_keyboard.add(types.InlineKeyboardButton("Назад", callback_data="404"))
        await bot.send_message(callback_query.from_user.id, "Выберете направление:", reply_markup=directions_keyboard)

    if callback_query.data == "404":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(callback_query.from_user.id, "Главное меню. Выберете действие:",
                               reply_markup=start_keyboard)


async def show_directions(callback_query: types.CallbackQuery, state: FSMContext):
    directionsDB = Directions()
    directions = directionsDB.get_ids()
    if (int(callback_query.data),) in directions:
        focusDB = Focus()
        focus = focusDB.get_names_by_direction(callback_query.data)
        focus_keyboard = types.InlineKeyboardMarkup()
        for i in range(len(focus)):
            focus_keyboard.add(types.InlineKeyboardButton(focus[i][0], callback_data=f'{focus[i][1]}'))
        focus_keyboard.add(types.InlineKeyboardButton("Назад", callback_data="404"))
        await DirectonsStates.FOCUS.set()
        await bot.send_message(callback_query.from_user.id, "Выберете направленность:", reply_markup=focus_keyboard)

    if callback_query.data == "404":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(callback_query.from_user.id, "Главное меню. Выберете действие:",
                               reply_markup=start_keyboard)


async def show_focus(callback_query: types.CallbackQuery, state: FSMContext):
    focusDB = Focus()
    focus = focusDB.get_all_ids()
    print(callback_query.data, focus)
    if (int(callback_query.data),) in focus:
        info_json = focusDB.get_info_by_id(callback_query.data)
        message = (f"<b>🔹 Направление:</b>\n{info_json['direction']}\n"
                   f"<b>🔹 Направленность:</b>\n{info_json['focus']}\n"
                   f"<b>🏢 Институт:</b>\n{info_json['institute']}\n\n"
                   f"📌 Проходной балл на бюджет прошлого года: <b>{info_json['passing_points']}</b>\n"
                   f"📌 Проходной балл на платное прошлого года: <b>{info_json['passing_points_contract']}</b>\n"
                   f"✏️ Необходимые предметы на ЕГЭ: {info_json['subjects']}\n"
                   f"💳 Цена платного за семестр: <b>{info_json['price']}</b>\n\n\n"
                   f"🧰 Общая характеристика: {info_json['specification']}\n"
                   f"📋 Учебный план: {info_json['learning_plan']}\n"
                   f"🗓 Календарный график: {info_json['calendar_chedule']}\n"
                   f"📄 Документы дисциплин: {info_json['documents']}\n"
                   )

        await bot.send_message(callback_query.from_user.id, message, parse_mode="HTML",
                               reply_markup=back_inline_keyboard)

    if callback_query.data == "404":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(callback_query.from_user.id, "Главное меню. Выберете действие:",
                               reply_markup=start_keyboard)