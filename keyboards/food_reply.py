from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def food_analysis_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🍽 Анализ еды")]
        ],
        resize_keyboard=True
    )
