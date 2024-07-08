import matplotlib.pyplot as plt
def track_progress(workout_logs):
    days = [log['day'] for log in workout_logs]
    completed_exercises = [len(log['exercises']) for log in workout_logs]

    plt.plot(days, completed_exercises, marker='o')
    plt.xlabel('Day') #label
    plt.ylabel('Completed Exercises') #label
    plt.title('Workout Progress') #title of the table
    plt.xticks(rotation=-90) #rotates the x-axis labels
    plt.show()

# Use this for testing but also to protect it against running this code being run when imported
if __name__ == '__main__':
    from datetime import date 
    from Blocks.WorkoutLogging import log_workout
    workout_logs = []
    # using an actual date object instead of just an int
    log_workout(workout_logs, date(2024, 6, 3), ['Jumping Jacks', 'Knee Push-ups']) #user input
    log_workout(workout_logs, date(2024, 6, 5), ['Squats', 'Knee Push-ups']) #user input
    print(workout_logs)
    track_progress(workout_logs)