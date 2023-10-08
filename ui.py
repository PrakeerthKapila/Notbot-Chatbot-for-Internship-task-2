import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
#setting remainder function
def set_reminder():
    #Text for taking remainder input
    reminder_text = reminder_entry.get()
    #Converting minutes as integer input
    minutes = int(minutes_entry.get())
    if not reminder_text:
        #Error Message if no remainder and immediately return function
        messagebox.showerror("Error", "Reminder text cannot be empty")
        return
    #calculate remainder
    reminder_time = datetime.now() + timedelta(minutes=minutes)
    reminders.append((reminder_time, reminder_text))
    reminder_entry.delete(0, tk.END)
    minutes_entry.delete(0, tk.END)
def check_reminders():
    #calculating CurrentTime
    current_time = datetime.now()
    #Looping on Reaminder list
    for reminder_time, reminder_text in reminders[:]:
        if current_time >= reminder_time:
            messagebox.showinfo("Reminder", reminder_text)
            reminders.remove((reminder_time, reminder_text))
#Creating Remainder empty list and appending the parameters
reminders = []
root = tk.Tk()
root.title("Reminder Bot")
reminder_label = tk.Label(root, text="Enter Reminder:")
reminder_label.pack()
reminder_entry = tk.Entry(root)
reminder_entry.pack()
minutes_label = tk.Label(root, text="Set Reminder (Minutes from now):")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()
set_button = tk.Button(root, text="Set Reminder", command=set_reminder)
set_button.pack()
check_button = tk.Button(root, text="Check Reminders", command=check_reminders)
check_button.pack()
root.mainloop()
