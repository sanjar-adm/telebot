import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from telebotRicandMorty import get_character_data_by_name

API_TOKEN = '5264879427:AAH5sE8DY3vroO5bWvNry9pEb89VkZhFzUc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    characters = ['Rick Sanchez', 'Morty Smith',
                  'Summer Smith', 'Jerry Smith',
                  'Squanchy', 'Beth Smith',
                  'Krombopulos Michael', 'Reverse Giraffe', 'Birdperson']
    characters_buttons = [KeyboardButton(name) for name in characters]
    keyboard = ReplyKeyboardMarkup().add(*characters_buttons)

    await message.reply("Привет! Друг 👋 Смотрели Рик и Морти?,Выбери персонаж и Узнай о них! ", reply_markup=keyboard)


@dp.message_handler()
async def send_info_about_character(message: types.Message):

    character = get_character_data_by_name(message.text)

    if character is None:
        await message.reply("not found please try entering the name again")
    else:
        await message.reply(
            f"name: {character['name']}\n\
            status: {character['status']}\n\
            species: {character['species']}\n\
            type: {character['type']}\n\
            gender: {character['gender']}\n\
            img: {character['image']}\n\
            location: {character['location']['name']}\
            ")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)