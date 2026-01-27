from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def analyze_food_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Добавить ещё",
                                  callback_data="food_add_more")],
            [InlineKeyboardButton(text="✅ Зафиксировать",
                                  callback_data="food_fix")]
        ]
    )