import random

# A static database of exercises
exercise_db = {
    'beginner': ['Jumping Jacks', 'Knee Push-ups', 'Squats'],
    'intermediate': ['Burpees', 'Pull-ups', 'Lunges'],
    'advanced': ['Weighted Push-ups', 'Muscle-ups', 'Pistol Squats']
}

def generate_workout_plan(user_profile):
    fitness_level = user_profile['fitness_level'] #takes the fitness level input
    days_per_week = user_profile['days_per_week'] #takes the days per week input
    time_commitment = user_profile['time_commitment'] #takes the time commitment input

    plan = []
    for _ in range(days_per_week):
        daily_workout = random.sample(exercise_db[fitness_level], 3)
        plan.append(daily_workout)
    
    return plan

workout_plan = generate_workout_plan('user_profile')
print(workout_plan)
