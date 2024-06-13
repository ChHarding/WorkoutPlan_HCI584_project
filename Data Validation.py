def validate_user_input(user_profile):
    # validating each field in the user_profile dictionary
    # return True if valid, else False
    valid_goals = ['lose weight', 'gain muscle', 'maintain fitness']
    valid_levels = ['beginner', 'intermediate', 'advanced']

    if user_profile['goal'] not in valid_goals:
        return False
    if user_profile['fitness_level'] not in valid_levels:
        return False 
    if not isinstance(user_profile['equipment'], list):
        return False
    if not (1 <= user_profile['days_per_week'] <= 7):
        return False #there's 7 days in a week so the days per week must fall in that range
    if not (10 <= user_profile['time_commitment'] <= 120):
        return False #must have 10 minutes at a minimum and there's a cap of 120 minutes
    
    return True
