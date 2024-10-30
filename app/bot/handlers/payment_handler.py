from datetime import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from app.bot.keyboards.inline_keyboard import (
    subscription_duration_keyboard,
    payment_method_keyboard,
    network_selection_keyboard,
    check_payment_keyboard
)
from app.bot.state_manager import UserState

payment_router = Router()


@payment_router.callback_query(F.data == "pay_access")
async def pay_access(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = callback.from_user.id
    await callback.message.edit_text(
        "Выберите срок подписки:",
        reply_markup=subscription_duration_keyboard()
    )

    await state.set_state(UserState.subscription)


@payment_router.callback_query(F.data.startswith("subscribe_"))
async def subscribe(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    duration = int(callback.data.split("_")[1])
    await state.update_data(duration=duration)

    user_id = callback.from_user.id
    await callback.message.edit_text(
        f"Выбрана подписка на {duration} месяц(ев). Выберите способ оплаты:",
        reply_markup=payment_method_keyboard()
    )

    await state.set_state(UserState.payment)


@payment_router.callback_query(F.data.startswith("pay_stars"))
async def pay_stars(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    duration = data.get("duration")
    amount_required = {
        1: 1500,
        6: 8000,
        12: 15000}.get(duration)
    duration = data.get("duration")
    await callback.message.answer_invoice(title="Покупка ключей",
                                          description=f"срок: {duration} месяц(ев)",
                                          provider_token="",
                                          currency="XTR",
                                          prices=[types.LabeledPrice(label="XTR", amount=int(amount_required/2.04))],
                                          payload="demo",
                                          start_parameter="demo")

@payment_router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await pre_checkout_q.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@payment_router.message()
async def successful_payment(message: types.Message, state: FSMContext):
    await message.answer("Платеж прошел успешно! Вы получили доступ к каналу", reply_markup=check_payment_keyboard(), message_effect_id="5104841245755180586")
