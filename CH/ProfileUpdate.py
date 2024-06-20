from DataValidation import validate_user_input
from WorkoutGeneration import generate_workout_plan

# CH: I find it weird that updating the profile also generates a new plan 
# so I'm now calling generate_workout_plan separately after the profile is updated/validated
def update_user_profile(user_profile, updates):
    user_profile.update(updates)
    result = validate_user_input(user_profile) # validate could alternatively return error strings
    if result == True:  
        return user_profile
    else:
        return result # You would need to test in the caller if the result is a dict or a string

'''
def update_user_profile(user_profile, updates):
    user_profile.update(updates)
    if validate_user_input(user_profile):  
        new_plan = generate_workout_plan(user_profile)  
        return new_plan, user_profile
    else:
        return None, "Invalid profile update"

'''

# Use this for testing but also protect it against running this code being run when imported
if __name__ == '__main__':
    user_profile = {
        'goal': 'lose weight',
        'fitness_level': 'beginner',
        'equipment': ['dumbbells'],
        'days_per_week': 3,
        'time_commitment': 30
    }
    print("Initial profile:", user_profile)
    result = update_user_profile(user_profile, 
                             {'fitness_level': 'intermediate', 'equipment': ['dumbbells', 'resistance bands']})
    if isinstance(result, dict):
        user_profile = result
        print("Updated profile:", user_profile)
        workout_plan = generate_workout_plan(user_profile)
        print("Generated Plan for new profile:", workout_plan)