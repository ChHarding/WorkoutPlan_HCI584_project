# Major parts:
# 1) user profile: Load user profile from a csv file, update it, save it
# 2) Exercise generation: load exercises from a csv file, generate a workout plan based on user profile
# 3) Workout logging: log workouts to a csv file
# 4) Progress tracking: track/plot progress over time

import tkinter as tk
from tkinter import messagebox, ttk
import random
import csv
from datetime import date
import matplotlib.pyplot as plt

class WorkoutTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Workout Tracker")

        # Create the Notebook widget
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        # These should be loaded from a csv file or a pickle file!
        self.equipment_values = ['dumbbells', 'barbell', 'resistance bands', 'kettlebell']
        self.valid_goals = ['lose weight', 'gain muscle', 'maintain fitness']
        self.valid_levels = ['beginner', 'intermediate', 'advanced']

        self.user_profile = {
            'goal': 'lose weight',
            'fitness_level': 'beginner',
            'equipment': ['dumbbells', "barbell"], #must be from equipment_values
            'days_per_week': 3,
            'time_commitment': 30
        }

        self.exercise_db = {
            'beginner': ['Jumping Jacks', 'Knee Push-ups', 'Squats'],
            'intermediate': ['Burpees', 'Pull-ups', 'Lunges'],
            'advanced': ['Weighted Push-ups', 'Muscle-ups', 'Pistol Squats']
        }

        self.workout_log_file = 'workout_log.csv'
        self.workout_logs = self.load_workout_logs()

        # Initialize tabs
        self.init_tabs()

    def init_tabs(self):
        # Create frames for each tab
        user_profile_tab = ttk.Frame(self.notebook)
        exercise_generation_tab = ttk.Frame(self.notebook)
        workout_logging_tab = ttk.Frame(self.notebook)
        progress_tracking_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(user_profile_tab, text='User Profile')
        self.notebook.add(exercise_generation_tab, text='Exercise Generation')
        self.notebook.add(workout_logging_tab, text='Workout Logging')
        self.notebook.add(progress_tracking_tab, text='Progress Tracking')

        # Create tabs
        self.create_user_profile_tab(user_profile_tab)
        self.create_exercise_generation_tab(exercise_generation_tab)
        self.create_workout_logging_tab(workout_logging_tab)
        self.create_progress_tracking_tab(progress_tracking_tab)

    def create_user_profile_tab(self, user_profile_tab):
        label = tk.Label(user_profile_tab, text="Goal:")
        label.grid(row=0, column=0, sticky="w")
        self.goal_combobox = ttk.Combobox(user_profile_tab, values=self.valid_goals)
        self.goal_combobox.set(self.user_profile['goal'])
        self.goal_combobox.grid(row=0, column=1)

        label = tk.Label(user_profile_tab, text="Fitness Level:")
        label.grid(row=1, column=0, sticky="w")
        self.fitness_level_combobox = ttk.Combobox(user_profile_tab, values=self.valid_levels)
        self.fitness_level_combobox.set(self.user_profile['fitness_level'])
        self.fitness_level_combobox.grid(row=1, column=1)

        label = tk.Label(user_profile_tab, text="Equipment:")
        label.grid(row=2, column=0, sticky="w")
        self.equipment_listbox = tk.Listbox(user_profile_tab, selectmode="multiple")
        self.equipment_listbox.insert(tk.END, *self.equipment_values)
        self.equipment_listbox.grid(row=2, column=1)

        # Set the selected equipment values as selected in the listbox
        for value in self.user_profile['equipment']:
            index = self.equipment_values.index(value)
            self.equipment_listbox.selection_set(index)

        label = tk.Label(user_profile_tab, text="Days per Week:")
        label.grid(row=3, column=0, sticky="w")
        self.entry_days_per_week = tk.Entry(user_profile_tab)
        self.entry_days_per_week.insert(0, str(self.user_profile['days_per_week']))
        self.entry_days_per_week.grid(row=3, column=1)

        label = tk.Label(user_profile_tab, text="Time Commitment:")
        label.grid(row=4, column=0, sticky="w")
        self.entry_time_commitment = tk.Entry(user_profile_tab)
        self.entry_time_commitment.insert(0, str(self.user_profile['time_commitment']))
        self.entry_time_commitment.grid(row=4, column=1)

        self.update_profile_button = tk.Button(user_profile_tab, text="Update Profile", command=self.update_profile)
        self.update_profile_button.grid(row=5, column=0, columnspan=2)

    def update_profile(self):
        # Update user profile from the values of user-profile_tab widgets
        self.user_profile['goal'] = self.goal_combobox.get()
        self.user_profile['fitness_level'] = self.fitness_level_combobox.get()
        selected_indices = self.equipment_listbox.curselection()
        self.user_profile['equipment'] = [self.equipment_listbox.get(i) for i in selected_indices]

        # Set the selected equipment values as selected in the listbox
        self.equipment_listbox.selection_clear(0, tk.END) #Clear all previous selections
        for value in self.user_profile['equipment']:
            index = self.equipment_values.index(value)
            self.equipment_listbox.selection_set(index)

        # Check if days per week are within the range of 1 to 7
        days_per_week = int(self.entry_days_per_week.get()) # Might still bomb if int() fails!
        if days_per_week < 1 or days_per_week > 7:
            tk.messagebox.showerror("Error", "Days per week must be between 1 and 7")
        else:
            self.user_profile['days_per_week'] = days_per_week

        # Check if time commitment is within the range of 10 to 120
        time_commitment = int(self.entry_time_commitment.get())
        if time_commitment < 10 or time_commitment > 120:
            tk.messagebox.showerror("Error", "Time commitment must be between 10 and 120 minutes")
        else:
            self.user_profile['time_commitment'] = int(self.entry_time_commitment.get())
        print("Updated profile:", self.user_profile)

    # for this tab we basically just fire a button to create a workout plan based on the user profile
    # and display it in a Scrollable text box
    def create_exercise_generation_tab(self, exercise_generation_tab):
        # Create a button to generate a workout plan
        self.generate_workout_button = tk.Button(exercise_generation_tab, text="Generate Workout Plan", command=self.generate_workout_plan)
        self.generate_workout_button.pack(padx=10)

        # create scrollable text box to display the workout plan
        self.workout_plan_text = tk.Text(exercise_generation_tab, height=15, width=50)
        self.workout_plan_text.pack(padx=10, pady=10, fill='both', expand=True)

        #creat vertical scrollbar for the text box
        scrollbar = tk.Scrollbar(self.workout_plan_text, orient="vertical", command=self.workout_plan_text.yview)
        scrollbar.pack(side="right", fill="y")
        #configure the text bos to use the scrollbar
        self.workout_plan_text.configure(yscrollcommand=scrollbar.set)

    # called when generate_workout_button is clicked
    # will store generated plan in self.plan and show it in the text box
    def generate_workout_plan(self):
        fitness_level = self.user_profile['fitness_level']
        self.plan = []
        for _ in range(self.user_profile['days_per_week']):
            daily_workout = random.sample(self.exercise_db[self.user_profile['fitness_level']], 3)
            self.plan.append(daily_workout)
            # print(plan)

        #Display the workout plan in the text box
        for i, daily_workout in enumerate(self.plan, 1):
            self.workout_plan_text.insert(tk.END, f"Day {i}:\n")
            for exercise in daily_workout:
                self.workout_plan_text.insert(tk.END, f"  - {exercise}\n")
            self.workout_plan_text.insert(tk.END, "\n")
        # scroll down to the end of the text
        self.workout_plan_text.see(tk.END)

    def create_workout_logging_tab(self, workout_logging_tab):
        tk.Label(workout_logging_tab, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="w")
        self.entry_date = tk.Entry(workout_logging_tab)
        self.entry_date.grid(row=0, column=1)

        tk.Label(workout_logging_tab, text="Exercises (comma-separated):").grid(row=1, column=0, sticky="w")
        self.entry_exercises = tk.Entry(workout_logging_tab)
        self.entry_exercises.grid(row=1, column=1)

        self.log_workout_button = tk.Button(workout_logging_tab, text="Log Workout", command=self.log_workout)
        self.log_workout_button.grid(row=2, column=0, columnspan=2)

    def log_workout(self):
        workout_date = self.entry_date.get()
        exercises = self.entry_exercises.get().split(',')

        workout_entry = {'day': workout_date, 'exercises': exercises}
        self.workout_logs.append(workout_entry)

        with open(self.workout_log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([workout_date] + exercises)

        tk.messagebox.showinfo("Success", "Workout logged successfully!")
        self.entry_date.delete(0, tk.END)
        self.entry_exercises.delete(0, tk.END)
    
    def load_workout_logs(self):
        workout_logs = []
        try:
            with open(self.workout_log_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    workout_date = row[0]
                    exercises = row[1:]
                    workout_logs.append({'day': workout_date, 'exercises': exercises})
        except FileNotFoundError:
            pass
        return workout_logs

    def create_progress_tracking_tab(self, progress_tracking_tab):
        self.track_progress_button = tk.Button(progress_tracking_tab, text="Track Progress", command=self.track_progress)
        self.track_progress_button.pack(pady=10)

    def track_progress(self):
        if not self.workout_logs:
            tk.messagebox.showerror("Error", "No workout logs found to track progress.")
            return
        
        days = [log['day'] for log in self.workout_logs]
        completed_exercises = [len(log['exercises']) for log in self.workout_logs]

        plt.plot(days, completed_exercises, marker='o')
        plt.xlabel('Day') #label
        plt.ylabel('Completed Exercises') #label
        plt.title('Workout Progress') #title of the table
        plt.xticks(rotation=-90) #rotates the x-axis labels
        plt.show()


if __name__ == "__main__":
    app = WorkoutTrackerApp()
    app.mainloop()

