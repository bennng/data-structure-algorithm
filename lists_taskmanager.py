class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def complete_last_task(self):
        if self.tasks:
            completed_task = self.tasks.pop()
            print(f"Task '{completed_task}' completed and removed from the list.")
        else:
            print("No tasks to complete.")

task_manager = TaskManager()

task_manager.add_task("Task 1")
task_manager.add_task("Task 2")
task_manager.add_task("Task 3")

task_manager.complete_last_task()
task_manager.complete_last_task()
task_manager.complete_last_task()
