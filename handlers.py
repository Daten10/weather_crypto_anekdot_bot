from aiogram import Router, types, F
from aiogram.filters import Command
from bot_tasks import get_weather, get_crypto_data
from parser import parse_anekdotov_net

handler_router = Router()


@handler_router.message(Command('start'))
async def btn(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Погода \U0001F327'),
                types.KeyboardButton(text='Крипта \U0001F4B3')
            ],
            [
                types.KeyboardButton(text='Анекдот \U0001F479'),
            ],
        ], resize_keyboard=True
    )
    await message.answer('Че надо?', reply_markup=kb)


@handler_router.message(F.text.lower() == 'погода \U0001F327')
async def answer(message: types.Message):
    weather = get_weather('bishkek')
    await message.answer(weather)


@handler_router.message(F.text.lower() == 'крипта \U0001F4B3')
async def answer(message: types.Message):
    crypto = get_crypto_data()
    await message.answer(crypto)


@handler_router.message(F.text.lower() == 'анекдот \U0001F479')
async def answer(message: types.Message):
    anekdot = parse_anekdotov_net('https://anekdotov.net/anekdot/today.html')
    await message.answer(anekdot)


# @handler_router.message(F.text.lower() == 'погода')
# async def answer(message: types.Message):
#     get_weather('bishkek')
