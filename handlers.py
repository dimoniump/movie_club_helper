from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.methods.send_message import SendMessage
from aiogram.utils.chat_action import ChatActionSender

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from misc import send_message


day = 'fri'  # mon, tue, wed, thu, fri, sat, sun
hour = '08'
minute = '00'

user_router = Router()
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')


@user_router.message(CommandStart())
async def start_handler(msg: Message):
    chat_id = msg.chat.id
    user_id = msg.from_user.id
    user_names = msg.from_user.first_name

    await msg.answer(f'Hi, <b>{msg.from_user.first_name}</b>. '
                     f'I`m  <b>Ryan Gosling</b>! I will help you, my boy ❤️!',
                     parse_mode='HTML')
    scheduler.add_job(
        send_message,
        'cron',
        day_of_week=day, hour=hour, minute=minute,
        args=[msg],
    )
    scheduler.start()
    await msg.answer(f'Every second week on Monday at <b>{hour}:{minute}</b>, '
                     f'I`ll chose one from us who`ll create an activity in a <i>random way</i>')


@user_router.message(Command('next_activity'))
async def chose_activity_maker(msg: Message):
    await msg.answer(f'Test! Alex')


@user_router.message(Command('Ryan'))
async def message_handler(msg: Message):
    await msg.answer(f'I`m Ryan Gosling! I will help you')
