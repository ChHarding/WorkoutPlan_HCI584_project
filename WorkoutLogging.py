# This and returning a updated list makes this into a worker that can be called
# from any file.
def log_workout(workout_logs, day, exercises_completed):
    workout_logs.append({'day': day, 'exercises': exercises_completed})
    return workout_logs


# Use this for testing but also protect it against running this code being run when imported
if __name__ == '__main__':
    from datetime import date 
    workout_logs = []
    # using an actual date object instead of just an int
    log_workout(workout_logs, date(2024, 6, 3), ['Jumping Jacks', 'Knee Push-ups']) #user input
    log_workout(workout_logs, date(2024, 6, 5), ['Squats', 'Knee Push-ups']) #user input
    print(workout_logs)

# Simulate user logging workouts
def get_workouts_for_day(workout_plan, day):
    '''Return the workout for the specific day from the workout plan.'''
    if day < 1 or day > len(workout_plan):
        return "Invalid day, please provide a day within the workout plan duration."
    return workout_plan[day - 1]