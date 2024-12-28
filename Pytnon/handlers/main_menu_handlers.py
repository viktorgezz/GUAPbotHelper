# main_menu_handlers.py

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_instance import bot
from keyboards import start_keyboard, submittting_aplication_keyboard, document_examples_keyboard, back_keyboard
from states import MenuStates, SubmitttingAplicationStates, ReceptionCalendarStates, OtherStates, FAQStates, DirectonsStates, ElasticSearchStates, EGEStates
from .submtion_aplication import submiting_aplication_menu
from .reception_calendar import reception_calendar_menu
from .other import other_menu
from .faq import faq_menu
from .directions import directions_menu
from .elastic_handlers import elastic_handler
from .EGE import ask_points_rus


async def send_welcome(message: types.Message, state: FSMContext):
    await MenuStates.MAIN_MENU.set()
    await message.answer("🤚 Привет!\n"
                         "🤖 Я бот-помощник. Я могу тебе помочь с поступлением в ГУАП\n\nВыбери действие:", reply_markup=start_keyboard)

async def process_menu(message: types.Message, state: FSMContext):
    if message.text == "Подача заявления":
        await SubmitttingAplicationStates.MENU.set()
        await submiting_aplication_menu(message, state)

    if message.text == "Календарь приема":
        await ReceptionCalendarStates.MENU.set()
        await reception_calendar_menu(message, state)


    if message.text == "Другое":
        await OtherStates.MENU.set()
        await other_menu(message, state)


    if message.text == "FAQ":
        await FAQStates.MENU.set()
        await faq_menu(message, state)

    if message.text == "Направления подготовки":
        await DirectonsStates.MENU.set()
        await directions_menu(message, state)


    if message.text == "Задать вопрос виртуальному ассистенту":
        await ElasticSearchStates.ASK_QUESTION.set()
        await elastic_handler(message, state)

    if message.text == "ЕГЭ":
        await EGEStates.ASK_POINTS_RUS.set()
        await ask_points_rus(message, state)







