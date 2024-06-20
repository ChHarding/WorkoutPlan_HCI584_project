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