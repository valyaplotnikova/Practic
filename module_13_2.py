from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

api = ''
bot = Bot(token=api)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def start(message: Message):
    print('Привет!\nЯ бот помогающий твоему здоровью.')


# Этот хэндлер будет срабатывать на любые текстовые сообщения,
# кроме команд "/start"
@dp.message()
async def all_massages(message: Message):
    print('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    dp.run_polling(bot)

