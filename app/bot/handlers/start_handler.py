from aiogram import Router, types, F
from aiogram.filters import CommandStart
from app.bot.keyboards.inline_keyboard import main_menu_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать! Этот бот позволяет получить доступ к эксклюзивному каналу", reply_markup=main_menu_keyboard())


@start_router.callback_query(F.data == "back_to_main_menu")
async def start_command(callback: types.CallbackQuery):
    await callback.message.edit_text("Добро пожаловать! Этот бот позволяет получить доступ к эксклюзивному каналу", reply_markup=main_menu_keyboard())