# WorkoutPlan_HCI584_project
__Workout Plan Application__



__Introduction:__

Welcome to the WorkoutPlan Application! This application allows users to generate workout plans, log their workouts, and track their progress over time. Follow the steps below to get started.



__Prerequisites:__

Before you begin, ensure you have the following installed on your system:
- Python 3.x
- Tkinter (usually comes with Python)
- Matplotlib
- CSV module (comes with Python)



__Installation:__

1: Clone the Repository:
git clone https://github.com/abigailmill/WorkoutPlan_HCI584_project.git
cd workoutplan

2: Install Dependencies:
Ensure you have matplotlib installed:
pip install matplotlib



__Setup:__

1: Download or Clone the Repository:
git clone https://github.com/abigailmill/WorkoutPlan_HCI584_project.git
cd workoutplan

2: Set Up the Project:
No additional setup is required beyond installing the dependencies.



__Usage:__

Run the main application file:
python GUI.py
This will open the WorkoutPlan application window.



__User Profile Tab:__

1: Goal: Select your fitness goal from the dropdown menu (e.g., lose weight, gain muscle, maintain fitness).

2: Fitness Level: Select your fitness level from the dropdown menu (e.g., beginner, intermediate, advanced).

3: Equipment: Select the equipment you have available. You can select multiple items by holding the Ctrl key (Cmd key on Mac).

4: Days per Week: Enter the number of days per week you plan to work out.

5: Time Commitment: Enter the amount of time (in minutes) you can commit to each workout session.

6: Update Profile: Click the "Update Profile" button to save your settings.



__Generate Workout Plan Tab:__

1: Generate Workout Plan: Click the button to generate a workout plan based on your profile.

2: The generated workout plan will be displayed in a scrollable text box, organized by days (e.g., Day 1, Day 2).



__Workout Logging Tab:__

1: Date: Enter the date of your workout in the format YYYY-MM-DD.

2: Exercises: Select the exercises you completed from the dropdown menu. The exercises are labeled (e.g., 1A: Jumping Jacks) for easy reference.

3: Log Workout: Click the "Log Workout" button to save your workout. A confirmation message will be displayed.



__Progress Tracking Tab:__

1: Track Progress: Click the "Track Progress" button to view a graph of your workout progress over time.

2: The graph will display the number of completed exercises for each logged workout day.



__Screenshots:__

1: User Profile Tab:
![alt text](<Screenshot 2024-07-24 at 11.32.46 AM.png>)
![alt text](<Screenshot 2024-07-24 at 11.33.18 AM.png>)
![alt text](<Screenshot 2024-07-24 at 11.33.45 AM.png>)
![alt text](<Screenshot 2024-07-24 at 11.34.11 AM.png>)

2: Generation Exercise Tab:
![alt text](<Screenshot 2024-07-24 at 11.34.35 AM.png>)

3: Workout Logging Tab:
![alt text](<Screenshot 2024-07-24 at 11.35.02 AM.png>)
![alt text](<Screenshot 2024-07-24 at 11.35.24 AM.png>)

4: Progress Tracking Tab:
![alt text](<Screenshot 2024-07-24 at 11.35.48 AM.png>)



__Troubleshooting:__

1: Logging Errors:
- Ensure you enter a date in the correct format (YYYY-MM-DD).
- If no exercises appear in the dropdown menu, generate a workout plan first.

2: Plot Display Issues:
- If the dates are cut off in the plot, ensure you have added the following line in the track_progress method:
- fig.subplots_adjust(bottom=0.25)



__Limitations:__

1: The application currently does not support custom exercises beyond the predefined list.

2: The workout plan generation does not consider the user's specific goals in depth.

3: Error handling is basic and could be improved for a better user experience.



__Conclusion:__

Thank you for using the WorkoutPlan Application! We hope it helps you stay on track with your fitness goals. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.
