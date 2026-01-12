def validate_int(text: str | None, min_value: int, max_value: int) -> int | None:
    if text is None or not text.isdigit():
        return None

    value = int(text)
    if not min_value <= value <= max_value:
        return None

    return value
