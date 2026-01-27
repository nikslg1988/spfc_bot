import logging

def day_calories(calories: int,
                 goal: str ,
                 gender: str = None,
                 age: int = None,
                 activity: str = None) -> str:
        """
    Генерирует текстовое объяснение суточной нормы калорий.
    Гарантии:
    - всегда возвращает str
    - не выбрасывает исключения наружу
    - при ошибке LLM возвращает fallback-текст
    """
    
    fallback_text = (
        f"Ваша суточная норма калорий составляет {calories} ккал и соответствует выбранной цели — {goal}. Это количество энергии рассчитано для поддержания сбалансированного питания и помогает двигаться к цели постепенно, без резких ограничений и перегрузок. Соблюдение этой нормы упрощает контроль рациона и делает питание более осознанным в повседневной жизни"
                     )
    
    try:
        #формирование промт
         prompt_parts = [
            "Ты помощник по питанию, который объясняет уже рассчитанную суточную норму калорий.",
            f"Пользователю передано готовое значение нормы калорий: {calories} ккал.",
            f"Цель пользователя — {goal}."
        ]
        
        if gender is not None:
            prompt_parts.append(f"Пол пользователя: {gender}.")
            
        if age is not None:
            prompt_parts.append(f"Возраст пользователя: {age}")
        
        if activity is not None:
            prompt_parts.append(f"Активность пользователя: {activity}")
        
        prompt_parts.extend(
            [
            "Объясни, что означает это число в контексте его цели.",
            "Дай 1–2 практических совета, связанных с этой целью.",
            "Не рассчитывай калории, не объясняй формулы и не давай  медицинских рекомендаций.",
            "Ответ должен быть нейтральным по тону и состоять из 4–5 предложений."
            ]
        )
        prompt = "\n".join(prompt_parts)
        
        # вызов LLM
        # Здесь предполагается, что функция call_llm(prompt: str) -> str
        # реализована в этом же модуле или импортируется.
        
        response = call_llm(prompt)
        
        # валидация ответа
        if not isinstance(response, str):
            raise TypeError("LLM response is not a string")

        response = response.strip()
        if not response:
            raise ValueError("LLM response is empty")

        return response

    except Exception as exc:
        # ---------- логирование для разработчика ----------
        logging.exception("LLM error in day_calories(): %s", exc)

        # ---------- безопасный возврат ----------
        return fallback_text