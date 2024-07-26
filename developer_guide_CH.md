# Developer's Guide

## Overview

This project is a WorkoutPlan application built with Python using the `tkinter` library for the GUI, and `matplotlib` for plotting progress. The application allows users to manage their workout routines, log their exercises, and track their progress over time. The project is divided into several key modules: `WorkoutLogging.py`, `ProgressTracking.py`, and `GUI.py`.

## Project Structure
```
WorkoutPlan/
│
├── GUI.py
├── WorkoutLogging.py
├── ProgressTracking.py
├── workout_log.csv
├── README.md
│   └── user_guide.md
├── doc/
│   ├── developer_guide.md
```


## Modules Overview

### `GUI.py`

Handles the graphical user interface of the application. Contains the main `WorkoutApp` class.

### `WorkoutLogging.py`

Handles the logging of workout data. Contains the `WorkoutLog` class.

### `ProgressTracking.py`

Handles the tracking and plotting of workout progress. Contains the `ProgressTracker` class.

## User Interaction and Flow

0. **User Profile Tab**
   - Allows users to input their personal goal, fitness level, available equipment, days they can/want to workout per week, and the time commitment they have for each workout. It can be changed by the users at any point.
     
   ![image](https://github.com/user-attachments/assets/1697213c-324d-4477-9aab-cb11d5d10a53)


2. **Generate Workout Tab**
   - Allows users to generate workout routines.
     
    ![image](https://github.com/user-attachments/assets/d7e02e27-7c2e-49f0-a7bf-1cf814657ac0)


3. **Workout Logging Tab**
   - Allows users to log their workouts.
     
    ![image](https://github.com/user-attachments/assets/309b38d6-9042-4a4f-8723-4277b598585b)

    - talk about the format of the `workout_log.csv` log file!
   ```
    2024-07-18,Jumping Jacks,Squats,Knee Push-ups
    2024/07/19,Jumping Jacks,Knee Push-ups,Squats
    2024-07-22,Jumping Jacks,Squats,Jumping Jacks
    2024-07-23,Lunges,Pull-ups,Burpees
   ```

4. **Progress Tracking Tab**
   - Allows users to track their progress over time. Progress is defined by looking at your prior logged workouts on the chart.
     
   ![image](https://github.com/user-attachments/assets/a4c87b9d-bb59-46ef-bac9-71ec311808de)



### Code Walkthrough

- GUI.py: The WorkoutApp class in GUI.py handles the main application window and contains methods to create the different tabs.

- WorkoutLogging.py The WorkoutLog class in WorkoutLogging.py handles the logging of workout data to a CSV file.

- ProgressTracking.py: The ProgressTracker class in ProgressTracking.py handles the plotting of workout progress using matplotlib.

### Known Issues
- Minor: Ensure the date format is consistent (YYYY-MM-DD).
- Major: None identified.

### Future Work
- Add more detailed workout analytics.
- Implement additional features such as workout suggestions based on past performance.

### Ongoing Development
- Maintain and update the workout_log.csv structure as needed.
- Ensure compatibility with newer versions of Python and libraries.
