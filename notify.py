from plyer import notification
from quote import get_quote
from tasks import load_tasks

def send_daily_notification():
    tasks = load_tasks()
    completed = sum(1 for task in tasks if task["done"])
    total = len(tasks)
    quote = get_quote()

    message = f"✅ Tasks Done: {completed}/{total}\n💬 Quote: {quote}"
    
    notification.notify(
        title="🌞 Good Morning, Nani!",
        message=message,
        timeout=10,
        app_name="Productivity Assistant"
    )

if __name__ == "__main__":
    send_daily_notification()
