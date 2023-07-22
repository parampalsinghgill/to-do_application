from task_list import TaskList


class Menu:
    """Creates a command line interactive tool for users"""

    def __init__(self):
        self.tl = TaskList()
        self.menu = {
            "1": "create_task",
            "2": "modify_task",
            "3": "delete_task",
            "4": "search_task",
            "5": "quit"
        }

    def display_menu(self):
        """Display the menu options and ask user choice"""
        print(self.menu)

        choice = input("Choose your option: ")
        action = self.menu[choice]
        action()

    def create_task(self):
        """Action on create task option"""
        task_name = input("Enter task")
        days_to_complete = input("Enter number of days to complete")

        self.tl.create_task(task_name, days_to_complete)

    def modify_task(self):
        """Action to modify the task"""
        # display all tasks first to show which ones exist.
        self.tl.print_tasks()

        task_id = input("Enter the task id to modify")
        task_name = input("Enter updated task name")

        self.tl.modify_task(task_id, task_name)

    def delete_task(self):
        """Action to delete the task"""
        # display all tasks first to show which ones exist.
        self.tl.print_tasks()

        task_id = input("Enter the task id to delete a particular task")

        self.tl.delete_task(task_id)

    def search_tasks(self):
        """Action to search the tasks"""
        search_string = input("Enter the string to search in tasks")

        self.tl.search(search_string)


if __name__ == "__main__":
    my_menu = Menu()
    while True:
        my_menu.display_menu()
