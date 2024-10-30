from aiogram.fsm.state import StatesGroup, State

class UserState(StatesGroup):
    subscription = State()
    payment = State()
    gift = State()
    check = State()