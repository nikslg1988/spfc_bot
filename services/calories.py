
activity_coefficient = {
    "very_low": 1.2,
    "low": 1.375,
    "medium": 1.55,
    "high": 1.725,
    "very_high": 1.9
}

goal_coefficient = {
    "lose": 0.85,
    "gain": 1.15,
    "maintain": 1
}

def calculate_calories(height, weight, age, gender, activity, goal):
    
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
    maintenance_calories = bmr * activity_coefficient[activity]
    result_calories = maintenance_calories * goal_coefficient[goal]
    return int(result_calories)