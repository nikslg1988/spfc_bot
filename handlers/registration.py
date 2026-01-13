from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from states.registration import Registration
from keyboards.gender import gender_keyboard
from keyboards.activity import activity_keyboard

from services.validators import validate_int


def register_registration_handlers(dp):

    @dp.message(Command("start"))
    async def start_handler(message: types.Message, state: FSMContext):
        await message.answer("Привет! Введи рост в см:")
        await state.set_state(Registration.height)

    @dp.message(Registration.height, F.text)
    async def height_handler(message: types.Message, state: FSMContext):
        height = validate_int(message.text, 100, 250)
        if height is None:
            await message.answer("Рост от 100 до 250 см")
            return

        await state.update_data(height=height)
        await message.answer("Теперь введи вес в кг:")
        await state.set_state(Registration.weight)

    @dp.message(Registration.weight, F.text)
    async def weight_handler(message: types.Message, state: FSMContext):
        weight = validate_int(message.text, 30, 300)
        if weight is None:
            await message.answer("Вес от 30 до 300 кг")
            return

        await state.update_data(weight=weight)
        await message.answer("Введите возраст:")
        await state.set_state(Registration.age)

    @dp.message(Registration.age, F.text)
    async def age_handler(message: types.Message, state: FSMContext):
        age = validate_int(message.text, 1, 150)
        if age is None:
            await message.answer("Возраст от 1 до 150")
            return

        await state.update_data(age=age)
        await message.answer(
            "Выбери пол:",
            reply_markup=gender_keyboard()
        )
        await state.set_state(Registration.gender)

    @dp.callback_query(Registration.gender, F.data.startswith("gender_"))
    async def gender_handler(callback: types.CallbackQuery, state: FSMContext):
        gender = "male" if callback.data == "gender_male" else "female"
        
        if callback.message is None:
            await callback.answer("Ошибка", show_alert=True)
            return
        
        await state.update_data(gender=gender)
        await callback.message.answer("Выберите уровень активности: ",
                                      reply_markup=activity_keyboard())
        await state.set_state(Registration.activity)
        await callback.answer()


    
    @dp.callback_query(Registration.activity)
    async def activity_handler(callback: types.CallbackQuery, state: FSMContext):
        await callback.answer()
        await state.update_data(activity=callback.data)
        
        data = await state.get_data()
        if callback.message is None:
            await callback.answer("Ошибка", show_alert=True)
            return
        
        await callback.message.edit_text( # type: ignore
            f"Регистрация завершена ✅\n"
            f"Рост: {data['height']} см\n"
            f"Вес: {data['weight']} кг\n"
            f"Возраст: {data['age']}\n"
            f"Пол: {data['gender']}\n"
            f"Активность: {data['activity']}"
        )
        await state.clear()

   
