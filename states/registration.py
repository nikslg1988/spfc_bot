from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    height = State()
    weight = State()
    age = State()
    gender = State()
    activity = State()