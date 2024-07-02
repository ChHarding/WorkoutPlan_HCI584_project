# Major parts:
# 1) user profile: Load user profile from a csv file, update it, save it
# 2) Exercise generation: load exercises from a csv file, generate a workout plan based on user profile
# 3) Workout logging: log workouts to a csv file
# 4) Progress tracking: track/plot progress over time

import tkinter as tk
from tkinter import messagebox, ttk # for notebook tabs and messagebox

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
            'equipment': ['dumbbells', "barbell"], # must be from equipment_values
            'days_per_week': 3,
            'time_commitment':30  }

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

        # Add label to a tab (just for testing, replace these with the equivalent of create_user_profile_tab
        tk.Label(exercise_generation_tab, text="Exercise Generation Content Goes Here").pack()
        tk.Label(workout_logging_tab, text="Workout Logging Content Goes Here").pack()
        tk.Label(progress_tracking_tab, text="Progress Tracking Content Goes Here").pack()

        # Create user profile tab
        self.create_user_profile_tab(user_profile_tab)

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
        self.equipment_listbox.insert(tk.END, *self.equipment_values) # * means that it will unpack the list
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
        # Update user profile from the values of user_profile_tab widgets
        self.user_profile['goal'] = self.goal_combobox.get()
        self.user_profile['fitness_level'] = self.fitness_level_combobox.get()
        selected_indices = self.equipment_listbox.curselection()
        self.user_profile['equipment'] = [self.equipment_listbox.get(i) for i in selected_indices] # Use the indices to get the actual items

        # Set the selected equipment values as selected in the listbox
        self.equipment_listbox.selection_clear(0, tk.END)  # Clear all previous selections
        for value in self.user_profile['equipment']:
            index = self.equipment_values.index(value)
            self.equipment_listbox.selection_set(index)


        # Check if days per week are within the range of 1 to 7
        days_per_week = int(self.entry_days_per_week.get())  # might still bomb if int() fails!
        if days_per_week < 1 or days_per_week > 7:
            tk.messagebox.showerror("Error", "Days per week must be between 1 and 7")
        else:
            self.user_profile['days_per_week'] = days_per_week
        self.user_profile['days_per_week'] = int(self.entry_days_per_week.get())


        # Check if time commitment is within the range of 10 to 120
        time_commitment = int(self.entry_time_commitment.get())
        if time_commitment < 10 or time_commitment > 120:
            tk.messagebox.showerror("Error", "Time commitment must be between 10 and 120 minutes")
        else:
            self.user_profile['time_commitment'] = int(self.entry_time_commitment.get())
        print("Updated profile:", self.user_profile)

# Create and run the application
if __name__ == "__main__":
    app = WorkoutTrackerApp()
    app.mainloop()