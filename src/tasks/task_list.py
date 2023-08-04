from .to_do_task import ToDoTask
from exceptions import InvalidStatusError, InvalidDateError


class TaskList:
    """Creates, deletes, modifies and keeps track of  all tasks
    in a list."""
    def __init__(self):
        self.task_list = []

    def create_task(self, task_name, days_to_complete):
        """Create a new task with name and number of days to complete."""
        self.task_list.append(ToDoTask(task_name, days_to_complete))

    def modify_task(self, task_id, task_name=None, task_status=None, task_completion_date=None):
        """Modify and existing task."""
        if task_name is not None:
            self.__find_task(task_id).task_name = task_name

        # TODO: handle if __find_task return None
        try:
            if task_status is not None:
                self.__find_task(task_id).status = task_status
        except InvalidStatusError as e:
            print(e)

        try:
            if task_completion_date is not None:
                self.__find_task(task_id).completion_Date = task_completion_date
        except InvalidDateError as e:
            print(e)

    def delete_task(self, task_id):
        """Delete and existing task"""
        self.task_list.remove(self.__find_task(task_id))

    def __find_task(self, task_id):
        """Find a task based on id"""
        return_task = None

        for task in self.task_list:
            if str(task_id) == str(task.task_id):
                return_task = task
                break
            else:
                return_task = None

        return return_task

    def search(self, filter_str):
        """Search the task in task list using input filter"""
        tasks = [task for task in self.task_list if task.match(filter_str)]
        return tasks

    def print_tasks(self, tasks=None):
        """Prints all tasks on the screen."""
        if tasks is None:
            tasks_to_print = self.task_list
        else:
            tasks_to_print = tasks

        if not tasks_to_print or tasks_to_print is None:
            print("No current tasks.")
        else:
            for task in tasks_to_print:
                print("ID: {}, {}, \tCompleted by: {}, \tStatus: {}".format(task.task_id, task.task_name,
                                                                            task.completion_date, task.status.name))
        print()
