#TODO Reply клавиатура для анализа еды

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

analyze_button = KeyboardButton(text="🍽 Анализ еды")
#cancel_button = KeyboardButton(text="Отмена")

food_analysis_keyboard = ReplyKeyboardMarkup(
    keyboard=[[analyze_button]],
    resize_keyboard=True,
)
