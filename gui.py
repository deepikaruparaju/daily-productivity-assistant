import tkinter as tk
from tkinter import messagebox, ttk
from local_tasks import add_task, get_all_tasks, delete_task_by_index, update_task_done_status
from notify import notify_user
from quote import get_quote
import datetime
import threading

class ProductivityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌞 Daily Productivity Assistant")
        self.root.geometry("700x600")
        self.root.configure(bg="#1c1c1c")

        self.task_entry = tk.Entry(root, font=("Segoe UI", 13, "bold"), width=30)
        self.task_entry.pack(pady=10)

        time_frame = tk.Frame(root, bg="#2E2E2E")
        time_frame.pack()

        self.hour_var = tk.StringVar(value="HH")
        self.minute_var = tk.StringVar(value="MM")

        hour_dropdown = ttk.Combobox(time_frame, textvariable=self.hour_var, values=[f"{i:02d}" for i in range(24)], width=5)
        hour_dropdown.pack(side=tk.LEFT, padx=5)

        minute_dropdown = ttk.Combobox(time_frame, textvariable=self.minute_var, values=[f"{i:02d}" for i in range(0, 60)], width=5)
        minute_dropdown.pack(side=tk.LEFT, padx=5)

        add_button = tk.Button(root, text="➕ Add Task", command=self.add_task_gui, bg="#5cb85c", fg="white", font=("Segoe UI", 11))
        add_button.pack()

        self.task_frame = tk.Frame(root, bg="#2E2E2E")
        self.task_frame.pack(pady=10)

        self.quote_label = tk.Label(root, text=get_quote(), bg="#2E2E2E", fg="white", wraplength=600, font=("Arial", 10))
        self.quote_label.pack(pady=10)

        self.refresh_tasks()
        self.start_notification_thread()

    def add_task_gui(self):
        task = self.task_entry.get()
        hour = self.hour_var.get()
        minute = self.minute_var.get()

        if not task:
            messagebox.showwarning("⚠️ Empty Task", "Task cannot be empty!")
            return

        if hour == "HH" or minute == "MM":
            messagebox.showwarning("⚠️ Invalid Time", "Please select a valid time.")
            return

        due_time = f"{hour}:{minute}"
        current_time = datetime.datetime.now().strftime("%H:%M")
        if due_time <= current_time:
            messagebox.showwarning("⚠️ Invalid Time", "Time must be in the future!")
            return

        add_task(task, due_time)
        self.task_entry.delete(0, tk.END)
        self.hour_var.set("HH")
        self.minute_var.set("MM")
        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        tasks = get_all_tasks()
        self.task_widgets = []

        for idx, task in enumerate(tasks):
            text = task['task']
            due_time = task['due_time']
            done = task.get('done', False)

            current_time = datetime.datetime.now().strftime("%H:%M")
            overdue = not done and current_time > due_time

            task_var = tk.BooleanVar(value=done)
            cb = tk.Checkbutton(self.task_frame, text=f"{text} - {due_time}", variable=task_var, command=lambda i=idx, var=task_var: self.toggle_task(i, var),
                                font=("Segoe UI", 11), anchor='w', bg="#2E2E2E", fg="red" if overdue else "white", selectcolor="green")
            cb.pack(fill="x", pady=2)
            self.task_widgets.append((cb, task_var))

    def toggle_task(self, index, var):
        update_task_done_status(index, var.get())
        self.refresh_tasks()

    def start_notification_thread(self):
        def check_notifications():
            while True:
                now = datetime.datetime.now()
                now_str = now.strftime("%H:%M")
                tasks = get_all_tasks()
                for task in tasks:
                    due = datetime.datetime.strptime(task['due_time'], "%H:%M")
                    delta = (due - now).total_seconds()

                    if 295 <= delta <= 305:
                        notify_user("⏰ Reminder", f"5 minutes left: {task['task']}")
                    elif -5 <= delta <= 5:
                        notify_user("❗ Task Due", f"Time completed: {task['task']}")
                threading.Event().wait(60)

        threading.Thread(target=check_notifications, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductivityApp(root)
    root.mainloop()