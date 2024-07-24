# Developer's Guide

## Overview

This project is a WorkoutPlan application built with Python using the `tkinter` library for the GUI, and `matplotlib` for plotting progress. The application allows users to manage their workout routines, log their exercises, and track their progress over time. The project is divided into several key modules: `WorkoutLogging.py`, `ProgressTracking.py`, and `GUI.py`.

## Project Structure

WorkoutPlan/
│
├── C_run_app.py
├── GUI.py
├── WorkoutLogging.py
├── ProgressTracking.py
├── workout_log.csv
├── README.md
│ └── user_guide.md
├── doc/
│ ├── developer_guide.md

## Setup and Installation

1. Ensure you have Python 3.6+ installed.
2. Install required dependencies:
    ```
    pip install pandas matplotlib
    ```
3. Run the application:
    ```
    python C_run_app.py
    ```

## Modules Overview

### `GUI.py`

Handles the graphical user interface of the application. Contains the main `WorkoutApp` class.

### `WorkoutLogging.py`

Handles the logging of workout data. Contains the `WorkoutLog` class.

### `ProgressTracking.py`

Handles the tracking and plotting of workout progress. Contains the `ProgressTracker` class.

## User Interaction and Flow

1. **Generate Workout Tab**
   - Allows users to generate workout routines.

2. **Workout Logging Tab**
   - Allows users to log their workouts.

3. **Progress Tracking Tab**
   - Allows users to track their progress over time.

## Code Walkthrough

### `C_run_app.py`

```python
from GUI import WorkoutApp

if __name__ == "__main__":
    app = WorkoutApp()
    app.mainloop()

GUI.py
The WorkoutApp class in GUI.py handles the main application window and contains methods to create the different tabs.

WorkoutLogging.py
The WorkoutLog class in WorkoutLogging.py handles the logging of workout data to a CSV file.

ProgressTracking.py
The ProgressTracker class in ProgressTracking.py handles the plotting of workout progress using matplotlib.

Known Issues
- Minor: Ensure the date format is consistent (YYYY-MM-DD).
- Major: None identified.

Future Work
- Add more detailed workout analytics.
- Implement additional features such as workout suggestions based on past performance.

Ongoing Development
- Maintain and update the workout_log.csv structure as needed.
- Ensure compatibility with newer versions of Python and libraries.