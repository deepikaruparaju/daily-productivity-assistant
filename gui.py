import tkinter as tk
from tkinter import messagebox
import requests
import random
import threading
import time
from datetime import datetime

# --- Global Task List ---
tasks = []

# --- Quote Bank ---
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Stay focused and never give up.",
    "Success doesn't just find you. You have to go out and get it."
]

# --- Weather Fetch Function ---
def get_weather(city):
    API_KEY = "2909fb0e6e7e830543aa4ac998edd7d5"  # <-- Replace with real key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url).json()
        if res.get("main"):
            return f"{res['main']['temp']}°C, {res['weather'][0]['description'].title()}"
        else:
            return "City not found!"
    except:
        return "⚠️ Network Error"

# --- Notify Function ---
def notify_pending_tasks():
    while True:
        time.sleep(120)  # Every 2 mins
        if tasks:
            messagebox.showinfo("⏰ Reminder", f"You have pending tasks:\n• " + "\n• ".join(tasks))

# --- GUI Class ---
class ProductivityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Productivity Dashboard")
        self.root.geometry("700x650")
        self.root.configure(bg="#1e1e1e")

        # --- Quote Section ---
        tk.Label(root, text="💬 Quote of the Day", fg="#ffcc00", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=5)
        quote = random.choice(quotes)
        self.quote_label = tk.Label(root, text=quote, wraplength=600, fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.quote_label.pack(pady=5)

        # --- Weather Section ---
        tk.Label(root, text="🌦️ Weather", fg="#00d0ff", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=5)
        self.city_entry = tk.Entry(root, font=("Arial", 12))
        self.city_entry.pack()
        tk.Button(root, text="Get Weather", command=self.show_weather, bg="#00aaff", fg="white", font=("Arial", 12)).pack(pady=5)
        self.weather_result = tk.Label(root, text="", fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.weather_result.pack()

        # --- Task Entry ---
        tk.Label(root, text="📝 Tasks", fg="#7CFC00", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=10)
        self.task_entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.task_entry.pack()
        tk.Button(root, text="Add Task", command=self.add_task, bg="#28a745", fg="white", font=("Arial", 12)).pack(pady=5)

        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=60, height=8)
        self.task_listbox.pack(pady=5)

        # --- Stats Section ---
        tk.Label(root, text="📊 Stats", fg="#ff66cc", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=10)
        self.stats_label = tk.Label(root, text="Total Tasks: 0", fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.stats_label.pack()

        # --- Requirements / To-Do ---
        tk.Label(root, text="📌 Requirements", fg="#ffa500", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=10)
        requirements = [
            "✅ Check today's weather",
            "✅ Add at least one task",
            "✅ Complete one pending task",
            "✅ Stay consistent"
        ]
        self.req_label = tk.Label(root, text="\n".join(requirements), fg="white", bg="#1e1e1e", font=("Arial", 11), justify=tk.LEFT)
        self.req_label.pack(pady=5)

        # Start Notification Thread
        threading.Thread(target=notify_pending_tasks, daemon=True).start()

    def show_weather(self):
        city = self.city_entry.get()
        weather = get_weather(city)
        self.weather_result.config(text=weather)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.update_stats()
        else:
            messagebox.showwarning("⚠️", "Task cannot be empty!")

    def update_stats(self):
        self.stats_label.config(text=f"Total Tasks: {len(tasks)}")

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ProductivityApp(root)
    root.mainloop()
