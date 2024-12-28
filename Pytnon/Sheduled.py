
import asyncio
import datetime
from bot_instance import bot
from db import EnterCalendar

def create_scheduled_tasks():
    sheduled_tasks = []
    db = EnterCalendar()
    for date_desc in db.get_budget():
        task = send_message(f"Привет!\n Напоминаю, что завтра {date_desc[0]} - {date_desc[1]}")
        sheduled_tasks.append(task)
    return sheduled_tasks




async def send_message(message):
    chat_id = 123456789
    await bot.send_message(chat_id, message)


# Функция для запуска отправки сообщения в определенные дни
async def schedule_messages():
    dates_to_send = [
        datetime.datetime(2024, 6, 20, 12, 0, 0),
        datetime.datetime(2024, 6, 26, 12, 0, 0),
        datetime.datetime(2024, 7, 10, 12, 0, 0),
        datetime.datetime(2024, 7, 25, 12, 0, 0),
        datetime.datetime(2024, 7, 27, 12, 0, 0),
        datetime.datetime(2024, 7, 31, 12, 0, 0),
        datetime.datetime(2024, 8, 3, 12, 0, 0),
        datetime.datetime(2024, 8, 9, 12, 0, 0)
        # Добавьте сюда другие даты, если нужно
    ]


    tasks = create_scheduled_tasks()

    for i in range(8):
        current_time = datetime.datetime.now()
        time_to_wait = (dates_to_send[i] - current_time).total_seconds()
        if time_to_wait > 0:
            await asyncio.sleep(time_to_wait)
            await tasks[i]


async def main():
    await schedule_messages()

