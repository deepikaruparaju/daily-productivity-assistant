from quote import get_quote
from weather import get_weather
from tasks import init_task_file, add_task, view_tasks, delete_task, toggle_task_status

def print_header():
    print("=" * 50)
    print("🌞 DAILY PRODUCTIVITY ASSISTANT".center(50))
    print("=" * 50)

def main():
    init_task_file()
    print_header()

    # Quote Section
    print("\n📝 Quote of the Day:\n")
    print(get_quote())
    print("\n" + "-" * 50)

    # Weather Section
    city = input("\n🏙️  Enter your city for weather info: ")
    print("\n" + get_weather(city))
    print("\n" + "-" * 50)

    # Task Section
    while True:
        print("\n✅ TASK MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Toggle Task Status")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            print("\n📋 Your Tasks:\n")
            print(view_tasks())
        elif choice == "2":
            task = input("Enter new task: ")
            print(add_task(task))
        elif choice == "3":
            print(view_tasks())
            try:
                num = int(input("Enter task number to delete: "))
                print(delete_task(num - 1))
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print(view_tasks())
            try:
                num = int(input("Enter task number to toggle status: "))
                print(toggle_task_status(num - 1))
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "5":
            print("👋 Exiting task menu.")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
