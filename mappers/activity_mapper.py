ACTIVITY_MAP = {
    "very_low": "очень низкая",
    "low": "низкая",
    "medium": "средняя",
    "high": "высокая",
    "very_high": "очень высокая",
}

def activity_mapper(activity_data: dict) -> dict| None:
    
    result = {
        "activity": ACTIVITY_MAP.get(activity_data.get("activity"), None) # type: ignore
    }
    
    return result
