from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import start_keyboard, other_keyboard, dormitories_keyboard, lgotnoe_keyboard, military_keyboard, military_state_keyboard
from states import MenuStates, OtherStates


async def other_menu(message: types, state: FSMContext):
    await OtherStates.MENU.set()
    await message.answer("Выберете дейсвие:", reply_markup=other_keyboard)


async def process_other_menu(message: types, state: FSMContext):
    if message.text == "Общежития":
        await OtherStates.DORMITORIES.set()
        await message.answer("Выберите действие:", reply_markup=dormitories_keyboard)

    if message.text == "Льготное":
        await OtherStates.LGOTNOE.set()
        await message.answer("Выберите действие:", reply_markup=lgotnoe_keyboard)

    if message.text == "Военная кафедра":
        await OtherStates.MILITARY.set()
        await message.answer('Выберите действие', reply_markup=military_keyboard)

    if message.text == "Воинский учет":
        await OtherStates.MILITARY_STATE.set()
        await message.answer('Выберите действие', reply_markup=military_state_keyboard)

    if message.text == "Назад":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:", reply_markup=start_keyboard)



async def process_dormitories(message: types, state: FSMContext):
    if message.text == "Какие общежития есть?":
        await bot.send_message(message.chat.id, "🏢 Студенты гуапа расселяются по 5 общежитиям:\n\n"
                                                "🔹 Общежитие №1, пр. Маршала Жукова, д. 24\n\n"
                                                "🔹 Общежитие №2, ул. Передовиков, д. 13\n\n"
                                                "🔹 Общежитие №3, ул. Варшавская, д. 8\n\n"
                                                "🔹 Межвузовский студенческий городок «УМСГ»\n\n"
                                                "🔹 Общежитие на ул. Кузнецовской"
                                                )

    if message.text == "Документы для общежития":
        await bot.send_message(message.chat.id, "📍 <a href = 'https://docs.yandex.ru/docs/view?url=ya-browser%3A%2F%2F4DT1uXEPRrJRXlUFoewruBCeq2QPbUAeNMCA4A_3KmCnixruqX56b5E4OdvCH2oaSaheYzsXXlqaFXTwq3t4DlqbsxficJgrJhaaOw_cNWp1DHNW6Dpdh714mDu7saEDK-GU8c-9Q8rpwc931QsrwA%3D%3D%3Fsign%3DSj4w_F_EUp-iXzkHPpfqbReL-dK_Z9ePj3FoOkDE5K0%3D&name=zayavlenie_1.docx&nosw=1'>Заявление</a>\n"
                                                "подавать в формате word, без личной подписи на эл. адрес 4947095@guap.ru\n\n"
                                                "📍 <a href = 'https://docs.yandex.ru/docs/view?url=ya-browser%3A%2F%2F4DT1uXEPRrJRXlUFoewruCyQZ9Lg0M729LWUV0p4SmybRFH6T4u1SM_H_T3Sh9shHePiEguQza8irGB9QA1gI1G4WBzwugyIcYB4FjD6NGfah3732vyRMI8JzluD7qlcdnTTLcF-_OVTw_QPGlNoTw%3D%3D%3Fsign%3DZ-biPbOdt-D-qJX75oReaYVmfkt9OutITOqHst4lnaY%3D&name=zayavlenie_1.docx&nosw=1'>Заявление согласие на заключение договора найма</a>\n"
                                                "(если студенту нет 18 лет)\n\n"
                                                "📍 ксерокопия паспорта РФ с пропиской (2-5 страницы);\n\n"
                                                "📍 ксерокопия ФЛГ (флюорографии);\n\n"
                                                "📍 ксерокопия формы 086у (для 1 курса);\n\n"
                                                "📍 ксерокопия прививочного сертификата;\n\n"
                                                "📍 2 фото 3*4;\n\n"
                                                "📍 документы, подтверждающие льготу (при наличии)\n\n",
                               parse_mode="HTML")

    if message.text == "По какому принципу дают общежитие":
        await bot.send_message(message.chat.id, "📍 Лица, указанные в части 5 статьи Федерального закона от 29 декабря 2012 г. № 273-ФЗ «Об образовании в Российской Федерации (http://www.consultant/ru/document/cons_doc_LAW_140174, см. раздел «Информация об основных правах и преимуществах» https://www.spbstu.ru/abit/bachelor/oznakomitsya-with-the-regulations/beneficiaries);\n\n"
                                                "📍 Лица, претендующие на получение места в общежитиях университета и представляемых ГУАП в общежитиях МСГ и АТТ, ранжируются по убыванию баллов ЕГЭ или вступительных испытаний ГУАП (Внимание! Ранжирование осуществляется в рамках каждой очереди).")

    if message.text == "Условия предоставления общежития":
        await bot.send_message(message.chat.id, "📌 Места в общежитиях университета и представляемых ГУАП общежитиях МСГ и АТТ предоставляются иногородним студентам бакалавриата, специалитета, магистратуры, программ СПО очной формы обучения.")


    if message.text == "Назад":
        await OtherStates.MENU.set()
        await other_menu(message, state)


async def process_lgotnoe(message: types, state: FSMContext):
    if message.text == "Кто может претендовать?":
        await bot.send_message(message.chat.id, "🔹 сироты или дети, которые оказались без родительского попечения;\n\n"
                                                "🔹 инвалиды первой или второй группы;\n\n"
                                                "🔹 абитуриенты в возрасте до 20 лет, у которых только один родитель — инвалид первой группы (при доходе ниже прожиточного минимума на одного человека в семье);\n\n"
                                                "🔹 дети военнослужащих, Героев России, работников прокуратуры, сотрудников противопожарной службы и т. д.\n\n"
                                                "👉 Полный перечень льгот для абитуриентов указан в статье 71 закона «Об образовании».\n\n\n")


    if message.text == "Какие документы нужно предоставить?":
        await bot.send_message(message.chat.id, "🛠 Данный раздел пока находится в разработке 🛠")
        # дописать

    if message.text == "Назад":
        await OtherStates.MENU.set()
        await other_menu(message, state)


async def process_military(message: types, state: FSMContext):
    if message.text == "Как поступить на военную кафедру?":
        await bot.send_message(message.chat.id, "https://new.guap.ru/vuc/abits")
    if message.text == "Когда заканчивается срок приёма документов?":
        await bot.send_message(message.chat.id, "1 мая года поступления в университет.")
    if message.text == """Какие нормативы нужно пройти для поступления?""":
        await bot.send_message(message.chat.id, "https://media.guap.ru/2882/tabl_fiz_p.docx")
    if message.text == "Какие документы нужны для поступления на военную кафедру?":
        await bot.send_message(message.chat.id, "🔹 копия свидетельства о рождении\n"
                                                "🔹 копия документа, удостоверяющего личность и гражданство\n"
                                                "🔹 автобиография, характеристика с места учёбы или работы (приложение № 3)\n"
                                                "🔹 копия документа о среднем образовании (учащиеся представляют справку о текущей успеваемости)\n"
                                                "🔹 три фотографии без головного убора размером 4,5x6 см")
    if message.text == "Какие документы нужно предоставить военкомату?":
        await bot.send_message(message.chat.id, "🔹 Копия приписного")

    if message.text == "Назад":
        await OtherStates.MENU.set()
        await other_menu(message, state)


async def process_military_state(message: types, state: FSMContext):
    if message.text == "Нужно ли предоставлять приписное удостоверение или военный билет при подаче документов и для зачисления на 1 курс?":
        await bot.send_message(message.chat.id, "нет")
    if message.text == "Как найти второй отдел?":
        await bot.send_message(message.chat.id, "Второй отдел находится в корпусе на Большой морской ауд. 5210")
    if message.text == "В процессе зачисления или сразу после него нужно ли сниматься с учета в военкомате по месту регистрации?":
        await bot.send_message(message.chat.id, "Нет.\nПосле зачисления в сентябре, каждому студенту мужского пола необходимо обратиться в военно-учетный отдел ГУАП, который поставит студента на учет и выдаст (или направит) необходимые документы в военный комиссариат по месту регистрации")
    if message.text == "Какие документы нужно предоставить военкомату/ второму отделу?":
        await bot.send_message(message.chat.id, "🔹 Копия приписного")
    if message.text == "Как встать на воинский учёт?":
        await bot.send_message(message.chat.id, "https://guap.ru/omp/vuch")

    if message.text == "Назад":
        await OtherStates.MENU.set()
        await other_menu(message, state)

