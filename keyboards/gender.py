from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def gender_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👨 Мужчина",
                                     callback_data="gender_male"
                                     ),
                InlineKeyboardButton(text="👩 Женщина",
                                     callback_data="gender_female"
                                     )                
            ]
        ]
    )
    