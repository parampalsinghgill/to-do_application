from tasks.task_list import TaskList
from common import print_options_in_dict, highlight_input_option


class TasksMenu:
    """Creates a command line interactive tool for user to manage tasks"""

    def __init__(self, tl):
        self.tl = tl
        self.task_menu_options = {
            "1": self.create_task,
            "2": self.modify_task,
            "3": self.delete_task,
            "4": self.search_task,
            "5": self.print_tasks,
            "6": quit
        }
        self.show_task_menu_options = {
            "1": "Create a new task",
            "2": "Modify an existing task",
            "3": "Delete an existing task",
            "4": "Search existing tasks",
            "5": "Show all existing tasks",
            "6": "Exit"
        }

    def get_input_from_user(self):
        """Show options and ask user for the input. Call the appropriate method accordingly."""
        print("********* Menu *********")
        print_options_in_dict(self.show_task_menu_options)
        choice = input("Choose your option: ")
        if choice in self.task_menu_options.keys():
            self.task_menu_options[choice]()
        else:
            print("Invalid option\n")

    def create_task(self):
        """Action on create task option"""
        highlight_input_option(self.show_task_menu_options["1"])

        task_name = input("Enter task: ")
        days_to_complete = input("Enter number of days to complete: ")

        self.tl.create_task(task_name, days_to_complete)
        print("A task '{}' has been created and added to TO-Do list.\n".format(task_name))

    def modify_task(self):
        """Action to modify the task"""
        modify_options = {
            "a": "Update task name",
            "b": "Update task Status",
            "c": "Update completion date"
        }
        modify_actions = {
            "a": self.__update_task_name,
            "b": self.__update_task_status,
            "c": self.__update_task_completion_date
        }
        highlight_input_option(self.show_task_menu_options["2"])

        # display all tasks first to show which ones exist.
        print("The following is the list of all existing tasks:")
        self.tl.print_tasks()

        task_id = input("Enter the task id to modify: ")

        print_options_in_dict(modify_options)

        update_choice = input("Choose the task value to update: ")

        if update_choice in modify_actions.keys():
            new_value = input("Enter the new value: ")
            modify_actions[update_choice](task_id, new_value)

        print("Task ID '{}' modified successfully.\n".format(task_id))

    def __update_task_name(self, task_id, task_name):
        """Update the name of the task"""
        self.tl.modify_task(task_id, task_name=task_name)

    def __update_task_status(self, task_id, task_status):
        """Update the status of the task"""
        self.tl.modify_task(task_id, task_status=task_status)

    def __update_task_completion_date(self, task_id, new_date):
        """
        Update the task completion date
        @param task_id: the unique id of the task
        @param new_date: the new date of the task
        """
        self.tl.modify_task(task_id, task_completion_date=new_date)

    def delete_task(self):
        """Action to delete the task"""
        highlight_input_option(self.show_task_menu_options["3"])
        # display all tasks first to show which ones exist.
        self.tl.print_tasks()

        task_id = input("Enter the task id to delete a particular task: ")

        self.tl.delete_task(task_id)
        print("Task ID '{}' deleted successfully.\n".format(task_id))

    def search_task(self):
        """Action to search the tasks"""
        highlight_input_option(self.show_task_menu_options["4"])
        search_string = input("Enter the string to search in tasks: ")

        searched_tasks = self.tl.search(search_string)
        self.tl.print_tasks(searched_tasks)

    def print_tasks(self):
        """Prints all the tasks in the task list"""
        highlight_input_option(self.show_task_menu_options["5"])
        self.tl.print_tasks()

    def run(self):
        """RUns the app until user chooses to quit."""
        print("\nWelcome to To-Do List. Follow the menu options to navigate.\n")
        while True:
            self.get_input_from_user()


if __name__ == "__main__":
    task_list = TaskList()
    menu = TasksMenu(task_list)
    menu.run()
