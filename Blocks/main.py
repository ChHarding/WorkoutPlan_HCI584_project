# to be able to import these they cannot have spaces!
from Blocks.ProfileUpdate import update_user_profile
from Blocks.WorkoutLogging import log_workout
from Blocks.ProgressTracking import track_progress
from Blocks.WorkoutGeneration import generate_workout_plan
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
# we don't need to check that the list of workouts is valid as per the workout plan
# b/c one we have a GUI, the choice of available workouts to choose to log will be restricted
# to those listed in the plan for a given day. You could do this now by implementing a
# get_workouts_for_day() function in the WorkoutLogging module
# workouts = get_workouts_for_day(1)
# log_workout(workout_logs, date(2024, 6, 3), workouts)

log_workout(workout_logs, date(2024, 6, 3), ['Jumping Jacks', 'Knee Push-ups']) #user input
log_workout(workout_logs, date(2024, 6, 5), ['Squats', 'Knee Push-ups']) #user input
print("logs:", workout_logs)

# simulate user tracking progress
track_progress(workout_logs)
