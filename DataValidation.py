def validate_user_input(user_profile):
    '''validating each field in the user_profile dictionary
       return True if valid, else False'''
    
    valid_goals = ['lose weight', 'gain muscle', 'maintain fitness']
    valid_levels = ['beginner', 'intermediate', 'advanced']

    if user_profile['goal'] not in valid_goals:
        return "Invalid goal, must be one of: " + ', '.join(valid_goals)
    if user_profile['fitness_level'] not in valid_levels:
        return "Invalid fitness level, must be one of: " + ', '.join(valid_levels) 
    if not isinstance(user_profile['equipment'], list):
        return "Invalid equipment, must be a list of strings"
    if not (1 <= user_profile['days_per_week'] <= 7):
        return "Invalid days per week, must be between 1 and 7" #there's 7 days in a week so the days per week must fall in that range
    if not (10 <= user_profile['time_commitment'] <= 120):
        return "Invalid time commitment, must be between 10 and 120 minutes" #must have 10 minutes at a minimum and there's a cap of 120 minutes

    return True

# Use this for testing but also to protect it against running this code being run when imported
if __name__ == '__main__': 

    # this test each possible error message
    user_profile = {
        'goal': 'lost weight',
        'fitness_level': 'beginner',
        'equipment': ['dumbbells'],
        'days_per_week': 3,
        'time_commitment': 30
    }
    print(validate_user_input(user_profile))

    user_profile = {
        'goal': 'lose weight',
        'fitness_level': 'master of the universe!',
        'equipment': ['dumbbells'],
        'days_per_week': 3,
        'time_commitment': 30
    }
    print(validate_user_input(user_profile))

    user_profile = {
        'goal': 'lose weight',
        'fitness_level': 'beginner',
        'equipment': 'dumbbells',
        'days_per_week': 3,
        'time_commitment': 30
    }
    print(validate_user_input(user_profile))

    user_profile = {
        'goal': 'lose weight',
        'fitness_level': 'beginner',
        'equipment': ['dumbbells'],
        'days_per_week': 8,
        'time_commitment': 30
    }
    print(validate_user_input(user_profile))

    user_profile = {
        'goal': 'lose weight',
        'fitness_level': 'beginner',
        'equipment': ['dumbbells'],
        'days_per_week': 3,
        'time_commitment': 5
    }
    print(validate_user_input(user_profile))

    user_profile = {
        'goal': 'lose weight',
        'fitness_level': 'beginner',
        'equipment': ['dumbbells'],
        'days_per_week': 3,
        'time_commitment': 130
    }
    print(validate_user_input(user_profile)) 
