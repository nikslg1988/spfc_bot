from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from states.registration import Registration
from keyboards.gender import gender_keyboard
from keyboards.activity import activity_keyboard

from keyboards.goal import goal_keyboard
from services.validators import validate_int
from services.calories import calculate_calories



def register_registration_handlers(dp):

    @dp.message(Command("start"))
    async def start_handler(message: types.Message, state: FSMContext):
        await state.clear()
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
        age = validate_int(message.text, 10, 120)
        if age is None:
            await message.answer("Возраст от 10 до 120")
            return

        await state.update_data(age=age)
        await message.answer(
            "Выбери пол:",
            reply_markup=gender_keyboard()
        )
        await state.set_state(Registration.gender)


    @dp.callback_query(Registration.gender, F.data.startswith("gender_"))
    async def gender_handler(callback: types.CallbackQuery, state: FSMContext):
        if callback.message is None:
            await callback.answer("Ошибка", show_alert=True)
            return

        if callback.data == "gender_male":
            gender = "male"
        elif callback.data == "gender_female":
            gender = "female"
        else:
            await callback.answer("Некорректный выбор", show_alert=True)
            return

        await state.update_data(gender=gender)
        await callback.message.answer(
            "Выберите уровень активности:",
            reply_markup=activity_keyboard()
        )
        await state.set_state(Registration.activity)
        await callback.answer()



    @dp.callback_query(Registration.activity, F.data.startswith("activity_"))
    async def activity_handler(callback: types.CallbackQuery, state: FSMContext):
        if callback.message is None:
            await callback.answer("Ошибка", show_alert=True)
            return

        await state.update_data(activity=callback.data.replace("activity_", "")) # type: ignore
        await callback.message.answer(
            "Выберите цель:",
            reply_markup=goal_keyboard()
        )
        await state.set_state(Registration.goal)
        await callback.answer()

    @dp.callback_query(Registration.goal,
                       F.data.startswith("goal_"))
    
    async def goal_handler(callback: types.CallbackQuery,
                           state: FSMContext):
        
        if callback.message is None:
            await callback.answer("Ошибка", show_alert=True)
            return

        goal = callback.data.replace("goal_", "") # type: ignore
        await state.update_data(goal=goal)
        
        data = await state.get_data()
        calories = calculate_calories(data["height"], data["weight"], 
                                      data["age"], data["gender"], 
                                      data["activity"], data["goal"])

        await callback.message.edit_text( # type: ignore
            "Регистрация завершена ✅\n"
            f"Рост: {data['height']} см\n"
            f"Вес: {data['weight']} кг\n"
            f"Возраст: {data['age']}\n"
            f"Пол: {data['gender']}\n"
            f"Активность: {data['activity']}\n"
            f"Цель: {data['goal']}\n"
            f"Норма калорий на день: {calories}"
        )

        await callback.answer()
        await state.clear()

   
