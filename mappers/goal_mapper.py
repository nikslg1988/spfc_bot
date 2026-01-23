    
GOAL_MAP = {
    "lose": "сбросить вес",
    "gain": "набрать вес",
    "maintain": "удержать вес",
    }
    

def goal_mapper(goal_data: dict) -> dict|None:

    result = {
    "goal": GOAL_MAP.get(goal_data.get("goal"), None) # type: ignore
    }
    return result
