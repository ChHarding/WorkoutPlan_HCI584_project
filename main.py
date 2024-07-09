# to be able to import these they cannot have spaces!
from ProfileUpdate import update_user_profile
from WorkoutLogging import log_workout, get_workouts_for_day
from ProgressTracking import track_progress
from WorkoutGeneration import generate_workout_plan
from datetime import date
from sys import exit 

# simulates user profile being created via GUI or loaded from a csv file
user_profile = {
    'goal': 'lose weight',  # Ch was lost weight
    'fitness_level': 'beginner',
    'equipment': ['dumbbells'],
    'days_per_week': 3,
    'time_commitment':30 #in minutes
}

# list of workouts performed
workout_logs = []

print("Initial profile:", user_profile)
result = update_user_profile(user_profile, 
                             {'fitness_level': 'intermediate', 'equipment': ['dumbbells', 'resistance bands']})
if isinstance(result, dict):
    user_profile = result
    print("Updated profile:", user_profile)
    workout_plan = generate_workout_plan(user_profile)
    print("Generated Plan for new profile:", workout_plan)
else:
    print(result) # error string
    exit()

# simulate user logging workouts
# getting workouts for the day using get_workouts_for_day
for i in range(1, user_profile['days_per_week'] + 1):
    workouts = get_workouts_for_day(workout_plan, i)
    if isinstance(workouts, str):
        print(workouts)
        exit()
    log_workout(workout_logs, date(2024, 6, 3 + i), workouts)

print("logs:", workout_logs)

# simulate user tracking progress
track_progress(workout_logs)
