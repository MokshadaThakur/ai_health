import math

def calculate_bmi(weight, height):
    # BMI = weight (kg) / (height (m))^2
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmr(weight, height, age, gender):
    # Mifflin-St Jeor Formula
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def daily_calories(bmr, activity_level):
    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    return round(bmr * activity_factors.get(activity_level.lower(), 1.2), 2)

def health_advice(bmi, activity):
    advice = []
    if bmi < 18.5:
        advice.append("Increase calorie intake with balanced diet.")
    elif bmi > 24.9:
        advice.append("Incorporate more physical activity and monitor calorie intake.")
    else:
        advice.append("Maintain your healthy lifestyle!")
    
    if activity in ["sedentary", "light"]:
        advice.append("Try at least 30 minutes of exercise daily.")
    else:
        advice.append("Great job staying active!")
    
    return advice

def health_report():
    print("\n--- AI Health Report Bot ---\n")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (Male/Female): ")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    activity = input("Activity level (sedentary, light, moderate, active, very active): ")

    # Calculate metrics
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    bmr = calculate_bmr(weight, height, age, gender)
    calories = daily_calories(bmr, activity)
    advice = health_advice(bmi, activity)

    # Display report
    print("\n--- Health Report for", name, "---")
    print(f"Age: {age} | Gender: {gender}")
    print(f"Weight: {weight} kg | Height: {height} cm")
    print(f"BMI: {bmi} ({category})")
    print(f"Daily Calorie Requirement: {calories} kcal/day")
    print("Advice:")
    for i, tip in enumerate(advice, 1):
        print(f"{i}. {tip}")

if __name__ == "__main__":
    health_report()
