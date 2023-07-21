from to_do_task import ToDoTask
from to_do_task import Status


class TaskList:
    """Creates, deletes, modifies and keeps track of  all tasks
    in a list."""
    def __init__(self):
        self.task_list = []

    def create_task(self, task_name, days_to_complete):
        """Create a new task with name and number of days to complete."""
        self.task_list.append(ToDoTask(task_name, days_to_complete))

    def modify_task(self, task_id, task_name):
        """Modify and existing task."""
        self.__find_task(task_id).task_name = task_name
        print("\nModified task with id: {}".format(task_id))
        print("Updated tasks list as follows:")
        self.print_tasks()

    def update_task_status(self, task_id, status):
        """Update the status of the task"""
        if "in_progress" in status:
            status = Status.IN_PROGRESS
        elif "done" in status:
            status = Status.DONE
        else:
            status = status.NEW

        for task in self.task_list:
            if task_id == task.id:
                task.status = status

    def delete_task(self, task_id):
        """Delete and existing task"""
        self.task_list.remove(self.__find_task(task_id))
        print("\nDeleted task with id: {}".format(task_id))
        print("Updated tasks list as follows:")
        self.print_tasks()

    def __find_task(self, task_id):
        """Find a task based on id"""
        return_task = None

        for task in self.task_list:
            if task_id == task.id:
                return_task = task
                break
            else:
                return_task = None

        return return_task

    def search(self, filter_str):
        """Search the task in task list using input filter"""
        tasks = [task for task in self.task_list if task.match(filter_str)]
        print("\nPrinting searched tasks:")
        self.print_tasks(tasks)

    def print_tasks(self, tasks=None):
        """Prints all tasks on the screen."""
        if tasks is None:
            tasks_to_print = self.task_list
        else:
            tasks_to_print = tasks

        for task in tasks_to_print:
            print("ID: {}, {}, Completion Date: {}".format(task.id, task.task_name, task.completion_date))
