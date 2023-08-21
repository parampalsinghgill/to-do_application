from .to_do_task import ToDoTask
from exceptions import InvalidStatusError, InvalidDateError, InvalidTaskError


class TaskList:
    """Creates, deletes, modifies and keeps track of user tasks in a list."""
    def __init__(self):
        self.task_list = []

    def create_task(self, task_name, days_to_complete):
        """Create a new task with name and number of days to complete."""
        self.task_list.append(ToDoTask(task_name, days_to_complete))

    def modify_task(self, task_id, task_name=None, task_status=None, task_completion_date=None):
        """Modify and existing task."""
        task = self.__find_task(task_id)

        if task is None:
            raise InvalidTaskError("Task not found in the task list.")

        if task_name is not None:
            task.task_name = task_name

        if task_status is not None:
            try:
                task.status = task_status
            except InvalidStatusError as e:
                raise e

        if task_completion_date is not None:
            try:
                self.__find_task(task_id).completion_date = task_completion_date
            except InvalidDateError as e:
                raise e

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
                print("ID: {}, {}, \tComplete by: {}, \tStatus: {}".format(task.task_id, task.task_name,
                                                                    task.completion_date, task.status.name))
        print()


if __name__ == "__main__":
    tl = TaskList()

    # create task
    tl.create_task("work", 3)
    tl.create_task("play", 5)
    tl.create_task("plan", 10)
    tl.create_task("play with me", 5)

    # print
    print("Print tasks 1:")
    tl.print_tasks()

    # # search task
    # tks = tl.search("play")
    # for tk in tks:
    #     print(tk.task_name)
    #
    # # delete task
    # tl.delete_task(2)
    #
    # # print
    # print("Print tasks 2:")
    # tl.print_tasks()

    # modify tasks
    tl.modify_task(1, "work smart and hard")
    tl.print_tasks()

    tl.modify_task(1, task_status=1)
    tl.print_tasks()

    tl.modify_task(1, task_completion_date="")
    tl.print_tasks()

