from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_instance import bot
from keyboards import start_keyboard, ege_keyboard, subject_keyboard, back_keyboard
from states import MenuStates, EGEStates
from EGE_calc import ChoiseDirections



async def ask_points_rus(message: types.Message, state: FSMContext):
    await EGEStates.ASK_POINTS_RUS.set()
    await bot.send_message(message.chat.id, "📱 Вы находитесь в калькуляторе ЕГЭ.\n\n✅ Введите ваши баллы по всем предметам и я вышлю вам направления, на которые вы проходите!", reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(message.chat.id, "👉 Введите ваши баллы по русскому языку:", reply_markup=back_keyboard)




async def process_ask_points_rus(message: types.Message, state: FSMContext):
    if message.text == 'Назад':
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:",
                               reply_markup=start_keyboard)

    else:
        try:
            points_rus = int(message.text)
            if points_rus < 0 or points_rus > 100:
                await bot.send_message(message.chat.id, "⛔️ Не корректно введены баллы, попробуйте еще раз!")
                await ask_points_rus(message, state)
            else:
                await state.update_data(points_rus=points_rus)
                await bot.send_message(message.chat.id, "❔ Какой экзамен по математике вы сдавали?", reply_markup=ege_keyboard)
                await EGEStates.ASK_POINTS_MATH.set()
        except:
            await bot.send_message(message.chat.id, "⛔️ Не корректно введены баллы, попробуйте еще раз!")
            await ask_points_rus(message, state)



async def ask_points_math(callback_data: types.CallbackQuery, state: FSMContext):
    if callback_data.data == "answer_2":
        data = await state.get_data()
        points_rus = data.get('points_rus')
        await EGEStates.ASK_POINTS.set()
        await bot.send_message(callback_data.from_user.id, "👉 Введите ваши баллы по математике:")
    if callback_data.data == "answer_1":
        await state.update_data(points_math=0)
        await EGEStates.ASK_DOP_SUBJ_POINTS.set()
        await bot.send_message(callback_data.from_user.id, "❔ Выберете предмет который вы еще сдавали:",
                               reply_markup=subject_keyboard)


async def process_ask_points_math(message: types.Message, state: FSMContext):
    if message.text == 'Назад':
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:",
                               reply_markup=start_keyboard)

    else:
        try:
            points_math = int(message.text)
            if points_math < 0 or points_math > 100:
                await bot.send_message(message.chat.id, "⛔️ Не корректно введены баллы, попробуйте еще раз!")
                await bot.send_message(message.from_user.id, "👉 Введите ваши баллы по математике:")
            else:
                await state.update_data(points_math=points_math)
                await EGEStates.ASK_DOP_SUBJ_POINTS.set()
                await bot.send_message(message.chat.id, "❔ Выберете предмет который вы еще сдавали:", reply_markup=subject_keyboard)
        except:
            await bot.send_message(message.chat.id, "⛔️ Не корректно введены баллы, попробуйте еще раз!")
            await bot.send_message(message.from_user.id, "👉 Введите ваши баллы по математике:")

async def ask_points(callback_data: types.CallbackQuery, state: FSMContext):
    await state.update_data(subj = callback_data.data)
    await EGEStates.GET_DOP_SUBJ_POINTS.set()
    await bot.send_message(callback_data.from_user.id, f"👉 Введите ваши баллы по {callback_data.data}:")


async def get_points(message: types.Message, state: FSMContext):
    if message.text == 'Назад':
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:",
                               reply_markup=start_keyboard)

    else:
        try:
            await state.update_data(subj_points=message.text)
            data = await state.get_data()
            subjects = ["Математика", "Русский язык", data.get('subj')]
            points = int(message.text)
            if points < 0 or points > 100:
                await bot.send_message(message.chat.id, "⛔️ Не корректно введены баллы, попробуйте еще раз!")
                await bot.send_message(message.from_user.id, "👉 Введите ваши баллы по выбранному предмету:")
            else:
                CD = ChoiseDirections(subjects, int(data.get('points_rus')) + int(data.get('points_math')) + points)
                info = CD.get_directions()
                mes = "Вы можете поступить на направления:\n\n"
                for dir in info:
                    mes += (f"🔹 <b>Направление:</b>\n {dir['description']}\n  {dir['name']}\n"
                                f"✏️ <b>Направленность:</b>\n  {dir['focus']}\n"
                                f"👉 <b>Проходные баллы прошлого года:</b>\n  {dir['passing_points']}\n\n\n"
                                )

                if mes == "Вы можете поступить на направления:\n\n":
                    mes += '-'


                await bot.send_message(message.chat.id, mes, parse_mode="HTML")

        except:
            await bot.send_message(message.chat.id, "⛔️ Не корректно введены баллы, попробуйте еще раз!")
            await bot.send_message(message.from_user.id, "👉 Введите ваши баллы по выбранному предмету:")









