import json
import matplotlib.pyplot as plt

TASK_FILE = "tasks.json"

def show_productivity_stats():
    with open(TASK_FILE, "r") as file:
        tasks = json.load(file)

    completed = sum(1 for t in tasks if t["done"])
    pending = sum(1 for t in tasks if not t["done"])

    labels = ['Completed', 'Pending']
    counts = [completed, pending]
    colors = ['#81c784', '#e57373']

    plt.bar(labels, counts, color=colors)
    plt.title("Your Productivity Stats")
    plt.ylabel("Number of Tasks")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_productivity_stats()
