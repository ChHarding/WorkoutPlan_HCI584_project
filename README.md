# WorkoutPlan_HCI584_project
Workout Plan Application

Introduction
Welcome to the WorkoutPlan Application! This application allows users to generate workout plans, log their workouts, and track their progress over time. Follow the steps below to get started.

Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.x
- Tkinter (usually comes with Python)
- Matplotlib
- CSV module (comes with Python)

Installation
1: Clone the Repository:
git clone https://github.com/abigailmill/WorkoutPlan_HCI584_project.git
cd workoutplan

2: Install Dependencies:
Ensure you have matplotlib installed:
pip install matplotlib

Setup
1: Download or Clone the Repository:
git clone https://github.com/abigailmill/WorkoutPlan_HCI584_project.git
cd workoutplan

2: Set Up the Project:
No additional setup is required beyond installing the dependencies.

Usage
Run the main application file:
python GUI.py
This will open the WorkoutPlan application window.

User Profile Tab
1: Goal: Select your fitness goal from the dropdown menu (e.g., lose weight, gain muscle, maintain fitness).
2: Fitness Level: Select your fitness level from the dropdown menu (e.g., beginner, intermediate, advanced).
3: Equipment: Select the equipment you have available. You can select multiple items by holding the Ctrl key (Cmd key on Mac).
4: Days per Week: Enter the number of days per week you plan to work out.
5: Time Commitment: Enter the amount of time (in minutes) you can commit to each workout session.
6: Update Profile: Click the "Update Profile" button to save your settings.

Generate Workout Plan Tab
1: Generate Workout Plan: Click the button to generate a workout plan based on your profile.
2: The generated workout plan will be displayed in a scrollable text box, organized by days (e.g., Day 1, Day 2).

Workout Logging Tab
1: Date: Enter the date of your workout in the format YYYY-MM-DD.
2: Exercises: Select the exercises you completed from the dropdown menu. The exercises are labeled (e.g., 1A: Jumping Jacks) for easy reference.
3: Log Workout: Click the "Log Workout" button to save your workout. A confirmation message will be displayed.

Progress Tracking Tab
1: Track Progress: Click the "Track Progress" button to view a graph of your workout progress over time.
2: The graph will display the number of completed exercises for each logged workout day.

Screenshots:
1: User Profile Tab
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.32.46%E2%80%AFAM.png?version%3D1721839037536)
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.33.18%E2%80%AFAM.png?version%3D1721839066219)
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.33.45%E2%80%AFAM.png?version%3D1721839077032)
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.34.11%E2%80%AFAM.png?version%3D1721839084454)
2: Generation Exercise Tab
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.34.35%E2%80%AFAM.png?version%3D1721839096489)
3: Workout Logging Tab
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.35.02%E2%80%AFAM.png?version%3D1721839107080)
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.35.24%E2%80%AFAM.png?version%3D1721839175580)
4: Progress Tracking Tab
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/abigailmiller/Documents/Screenshot%202024-07-24%20at%2011.35.48%E2%80%AFAM.png?version%3D1721839186542)

Troubleshooting
1: Logging Errors:
- Ensure you enter a date in the correct format (YYYY-MM-DD).
- If no exercises appear in the dropdown menu, generate a workout plan first.
2: Plot Display Issues:
- If the dates are cut off in the plot, ensure you have added the following line in the track_progress method:
 - fig.subplots_adjust(bottom=0.25)

Limitations
1: The application currently does not support custom exercises beyond the predefined list.
2: The workout plan generation does not consider the user's specific goals in depth.
3: Error handling is basic and could be improved for a better user experience.

Conclusion
Thank you for using the WorkoutPlan Application! We hope it helps you stay on track with your fitness goals. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.
