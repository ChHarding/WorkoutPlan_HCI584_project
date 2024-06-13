import matplotlib.pyplot as plt

def track_progress(workout_logs):
    days = [log['day'] for log in workout_logs]
    completed_exercises = [len(log['exercises']) for log in workout_logs]

    plt.plot(days, completed_exercises, marker='o')
    plt.xlabel('Day') #label
    plt.ylabel('Completed Exercises') #label
    plt.title('Workout Progress') #title of the table
    plt.show()

track_progress('workout_logs')
