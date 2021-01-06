'''calories_count.py'''
# pylint: disable=C0103
# pylint: disable=W0612
def bmr_cal(weight, height, age, gender):

    weight_in_kgs = weight / 2.2
    height_in_centimeters = height * 2.54
    if gender.lower() == "man":
        bmr = int((10 * weight_in_kgs) + (6.25 * height_in_centimeters) - (5 * age) + 5)
    elif gender.lower() == "woman":
        bmr = int((10 * weight_in_kgs) + (6.25 * height_in_centimeters) - (5 * age) - 161)
    # protein and carbs should 40% of calories and fat should be 20%
    return bmr


def daily_caloric_need(bmr, activityLevel):

    if activityLevel == 1:
        activityLevelIndex = 1.2
    elif activityLevel == 2:
        print("")
        activityLevelIndex = 1.375
    elif activityLevel == 3:
        activityLevelIndex = 1.46
    elif activityLevel == 4:
        activityLevelIndex = 1.725
    elif activityLevel == 5:
        activityLevelIndex = 1.9

    print(bmr)
    dailyCaloriesNeeded = int(bmr * activityLevelIndex)

    return dailyCaloriesNeeded


def calculate_macro(calories):

    calories_from_protein = int(0.4 * calories)
    calories_in_protein = int(calories_from_protein / 4)
    calories_from_carbs = int(0.4 * calories)
    calories_in_carbs = int(calories_from_carbs / 4)
    calories_from_fat = int(0.2 * calories)
    calories_in_fat = int(calories_from_fat / 9)

    # calculate fat loss / gain
    # 1 lb pf fat has 3500 calories to lose .5 lbs a week, divide 3,500 in half and then divide by 7
    halfAPoundaWeek_calories = int(calories - int((3500 / 2) / 7))

    calories_from_protein_reduced = int(0.4 * halfAPoundaWeek_calories)
    calories_in_protein_reduced = int(calories_from_protein / 4)
    calories_from_carbs_reduced = int(0.4 * halfAPoundaWeek_calories)
    calories_in_carbs_reduced = int(calories_from_carbs / 4)
    calories_from_fat_reduced = int(0.2 * halfAPoundaWeek_calories)
    calories_in_fat_reduced = int(calories_from_fat / 9)

    macros = {
        "MaxCalories": calories,
        "MinCalories": halfAPoundaWeek_calories,
        "MaxProtein": calories_from_protein,
        "MinProtein": calories_from_protein_reduced,
        "MaxCarbs": calories_from_carbs,
        "MinCarbs": calories_from_carbs_reduced,
        "MaxFat": calories_from_fat,
        "MinFat": calories_from_fat_reduced,
    }
    return macros
