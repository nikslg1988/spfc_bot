from aiogram.fsm.state import State, StatesGroup

class FoodAnalysis(StatesGroup):
    waiting_text = State()
    preview = State()
    
