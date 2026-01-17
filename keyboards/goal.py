from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def goal_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard = [
                [InlineKeyboardButton(text="Похудеть", 
                                     callback_data="goal_lose")],
                [InlineKeyboardButton(text="Набрать вес",
                                     callback_data="goal_gain")],
                [InlineKeyboardButton(text="Сохранить вес",
                                     callback_data="goal_maintain")]
        ]
    )