import requests


def fetch_high_priority_tasks():
    # Replace 'your_access_token' with your actual Todoist API token
    headers = {"Authorization": "Bearer your_access_token"}

    response = requests.get("https://api.todoist.com/rest/v1/tasks", headers=headers)
    tasks = response.json()

    # Filter tasks with priority 2 and higher
    high_priority_tasks = [
        {
            "content": task["content"],
            "due": task.get("due", {}).get("date", "No due date"),
        }
        for task in tasks
        if task["priority"] >= 2
    ]

    return high_priority_tasks


# Example usage
high_priority_task_list = fetch_high_priority_tasks()
for task in high_priority_task_list:
    print(f"{task['content']} - {task['due']}")
