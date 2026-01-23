GENDER_MAP = {
    "male": "мужской",
    "female": "женский"
}

def gender_mapper(gender_data: dict) -> dict | None:
    
    result = {
        "gender": GENDER_MAP.get(gender_data.get("gender"), None) # type: ignore
    }
    return result