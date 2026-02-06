from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext

from states.food import FoodAnalysis
from keyboards.analyze_food import analyze_food_keyboard
from services.llm.food_analysis import analyze_food

router = Router()

@router.message(F.text == "🍽 Анализ еды")
async def entry_text_handler(message: types.Message, state: FSMContext):
    
    #await state.clear() # Не работает пока нет БД TODO
    await state.set_state(FoodAnalysis.waiting_text)
    await message.answer("Опиши, что ты съел(а), одной строкой")
    
@router.message(FoodAnalysis.waiting_text, F.text)
async def waiting_text_handler(message: types.Message, state: FSMContext):
    
    food_text = message.text
    data = await state.get_data()
    daily_calories = data["daily_calories"]
    result_text = await analyze_food(food_text, daily_calories) # type: ignore
    
    await message.answer(
        result_text,
        reply_markup=analyze_food_keyboard()
    )
    
    await state.set_state(FoodAnalysis.preview)
    
@router.callback_query(F.data == "food_add_more", FoodAnalysis.preview)
async def add_more_food(callback: types.CallbackQuery,
                        state: FSMContext):
    
    if callback.message is None:
        await callback.answer("Ошибка", show_alert=True)
        return
    
    await state.set_state(FoodAnalysis.waiting_text)
    
    await callback.message.answer(
        "Опиши, что ты съел(а), одной строкой"
    )
    
    await callback.answer()
    
@router.callback_query(F.data == "food_fix", FoodAnalysis.preview)
async def food_fix_handler(callback: types.CallbackQuery, state: FSMContext):
    
    if callback.message is None:
        await callback.answer("Ошибка", show_alert=True)
        return
    
    await state.clear()
    
    await callback.message.answer(
        "Приём пищи зафиксирован"
    )
    
    await callback.answer()
    
    
