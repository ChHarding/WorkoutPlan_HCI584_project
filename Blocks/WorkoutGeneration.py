import random
# A static database of exercises
# CH this could later be read from a pickeled dict file
exercise_db = {
    'beginner': ['Jumping Jacks', 'Knee Push-ups', 'Squats'],
    'intermediate': ['Burpees', 'Pull-ups', 'Lunges'],
    'advanced': ['Weighted Push-ups', 'Muscle-ups', 'Pistol Squats']
}
# would it not also be desireable to put the number or reps in your db?
# e.g. 'beginner': [{'Jumping Jacks': 5}, {'Knee Push-ups':10}, {'Squats': 5}]


def generate_workout_plan(user_profile):
    ''' docstring '''
    fitness_level = user_profile['fitness_level'] #takes the fitness level input
    days_per_week = user_profile['days_per_week'] #takes the days per week input
    time_commitment = user_profile['time_commitment'] #takes the time commitment input

    plan = []
    for _ in range(days_per_week):
        daily_workout = random.sample(exercise_db[fitness_level], 3)
        plan.append(daily_workout)
    
    return plan

# Use this for testing but also protect it against running this code being run when imported
if __name__ == '__main__':
    user_profile = {
        'goal': 'lose weight',
        'fitness_level': 'beginner',
        'equipment': ['dumbbells'],
        'days_per_week': 3,
        'time_commitment': 30
    }
    workout_plan = generate_workout_plan(user_profile) # CH this was a string!
    print(workout_plan)