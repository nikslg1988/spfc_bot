from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def activity_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text="🧘 Минимальная активность",
                                 callback_data='activity_very_low'
                                 )],
            [InlineKeyboardButton(text="🚶 Низкая",
                                 callback_data='activity_low'
                                 )],
            [InlineKeyboardButton(text="🏃 Средняя",
                                 callback_data='activity_medium'
                                 )],
            [InlineKeyboardButton(text="💪 Высокая",
                                 callback_data='activity_high'
                                 )],
            [InlineKeyboardButton(text="🔥 Очень высокая",
                                 callback_data='activity_very_high'
                                 )]
        ]
    )