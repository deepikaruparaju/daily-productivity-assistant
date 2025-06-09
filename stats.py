from local_tasks import get_all_tasks

def calculate_productivity():
    tasks = get_all_tasks()
    if not tasks:
        return 0
    done_tasks = sum(1 for t in tasks if t.get("done", False))
    return (done_tasks / len(tasks)) * 100