from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import submittting_aplication_keyboard, document_examples_keyboard, back_keyboard, start_keyboard
from states import SubmitttingAplicationStates, MenuStates, DocumentExamplesStates


async def submiting_aplication_menu(message: types.Message, state: FSMContext):
    await SubmitttingAplicationStates.MENU.set()
    await message.answer("Выберите действие:", reply_markup=submittting_aplication_keyboard)

async def process_submitting_aplication_menu(message: types.Message, state: FSMContext):
    if message.text == "✏️Образцы документов для заполнения✏️":
        await SubmitttingAplicationStates.DOCUMENT_EXAMPLES.set()
        await process_document_examples(message, state)


    if message.text == "📍Как пройти к комиссии?📍":
        await bot.send_location(message.chat.id, longitude=30.29448647542808, latitude=59.9311571749424)
        await bot.send_message(message.chat.id, "📍 Санкт-Петербург, ул. Якубовича, д. 26\n\n"
                                                "🚇 Ближайшие станции метро:\n"
                                                "🔹 «Садовая»\n"
                                                "🔹 «Сенная»\n"
                                                "🔹 «Спасская»\n"
                                                "🔹 «Адмиралтейская»\n\n"
                                                "📌 До остановки «Площадь Труда»:\n"
                                                "🚎 троллейбусы: 5 или 22 (конечная остановка)\n"
                                                "🚌 автобусы: 6, 22 или 27\n"
                               )


    if message.text == "Дополнительные баллы при зачислении":
        with open('handlers/documents/dopUnits.pdf', 'rb') as document:
            await bot.send_document(message.chat.id, document, caption="Информация о перечне индивидуальных достижений поступающих, учитываемых при приеме на обучение и порядок учета указанных достижений")


    if message.text == "📞Контакты комиссии?📞":
        await bot.send_message(message.chat.id, "▶️ Бакалавриат, Специалитет, Магистратура, Аспирантура:\n\n"
                                                "📍 Санкт-Петербург, ул. Якубовича, д. 26\n"
                                                "📞 Телефон: +7 (812) 312-21-07\n"
                                                "📩 E-mail: priem@guap.ru\n")


    if message.text == "Какие документы нужны для поступления?":
        await bot.send_message(message.chat.id, "✏️ Документы, необходимые для поступления:\n\n"
                                                "🔹 Паспорт и его ксерокопия.\n"
                                                "🔹 Аттестат о полном среднем образовании или диплом о среднем профессиональном образовании.\n"
                                                "🔹 ИНН и СНИЛС.\n"
                                                "🔹 6  фотографий размером 3х4.\n"
                                                "🔹 Медицинская справка 086У.\n"
                                                "🔹 Документ об отношении к воинской обязанности (для мужчин).\n"
                                        )

    if message.text == "Назад":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:", reply_markup=start_keyboard)




# document examples
async def process_document_examples(message: types.Message, state: FSMContext):
    await DocumentExamplesStates.MENU.set()
    await message.reply("Выберете форму обучения:", reply_markup=document_examples_keyboard)


async def document_examples(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "och":
        await bot.send_message(callback_query.from_user.id, "Документы об очном", reply_markup=back_keyboard)
    elif callback_query.data == "zaoch":
        await bot.send_message(callback_query.from_user.id, "Документы об очно-заочном", reply_markup=back_keyboard)
    elif callback_query.data == "ev":
        await bot.send_message(callback_query.from_user.id, "Документы об вечернем", reply_markup=back_keyboard)

async def document_examples_back(message: types, state: FSMContext):
    if message.text == "Назад":
        await MenuStates.SUBMITTING_APLICATION.set()
        await submiting_aplication_menu(message, state)

# -------------------------------------------------------------------



# commition way
