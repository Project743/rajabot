#!/usr/bin/python3
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
import config
import ivent
import uptime
from sqlighter import SQLighter
import keyboards as kb
from datetime import datetime
import question
# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(text="subscribe")
async def subscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его
		db.add_subscriber(message.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, True)
	
	await message.answer("Вы успешно подписались на рассылку!\n")
@dp.callback_query_handler(text="unsubscribe")
async def unsubscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
		db.add_subscriber(message.from_user.id, False)
		await message.answer("Вы итак не подписаны.")
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, False)
		await message.answer("Вы успешно отписаны от рассылки.")

# инициализируем соединение с БД
db = SQLighter('db.db')

# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его
		db.add_subscriber(message.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, True)
	
	await message.answer("Вы успешно подписались на рассылку!\n")

# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
		db.add_subscriber(message.from_user.id, False)
		await message.answer("Вы итак не подписаны.")
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, False)
		await message.answer("Вы успешно отписаны от рассылки.")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Добро пожаловать!\nЯ - Pirsia, бот созданный чтобы быть подопытным кроликом \nЯ раскажу о сегодняшних ивентах в Dragon raja\n bot-project.online", reply_markup=kb.inline_kb1)


@dp.message_handler(commands=['ivent'])
async def process_ivent_command(message: types.Message):
    await message.answer(ivent.iventmsg())

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Я могу ответить на следующие команды:/start, /ivent, /help, /subscribe, /unsubscribe")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, question.get_question(msg.text))

async def scheduled(wait_for):
	while True:
		await asyncio.sleep(wait_for)

		
		notification_msg = ivent.notification()

		if notification_msg != 0:
			# получаем список подписчиков бота
			subscriptions = db.get_subscriptions()

			# отправляем всем новость
			for s in subscriptions:
				await bot.send_message(
					s[1],
					notification_msg ,
					disable_notification = True
				)
		


# запускаем лонг поллинг
if __name__ == '__main__':
	loop = asyncio.get_event_loop()	
	loop.create_task(scheduled(60))
#	dp.loop.create_task(scheduled(10)) # пока что оставим 10 секунд (в качестве теста)
	executor.start_polling(dp, skip_updates=True)
