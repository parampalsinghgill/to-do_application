from tasks.task_list import TaskList
from common import print_options_in_dict, highlight_input_option
from colorama import Fore
from exceptions import TaskException
from exceptions import TaskException


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
            "6": "Log off"
        }

    def create_task(self):
        """Action on create task option"""
        highlight_input_option(self.show_task_menu_options["1"])

        task_name = input("Enter task: ")
        days_to_complete = input("Enter number of days to complete: ")

        self.tl.create_task(task_name, days_to_complete)
        print("A task '{}' has been created and added to To-Do list.\n".format(task_name))

    def modify_task(self):
        """Action to modify the task if task list is not empty"""
        if self.tl.tasks:
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
            self.tl.print_tasks()

            task_id = input("Enter the task id to modify: ")

            if TasksMenu.__is_valid_option(task_id, self.tl):
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
        try:
            self.tl.modify_task(task_id, task_status=task_status)
        except TaskException as e:
            print(e)

    def __update_task_completion_date(self, task_id, new_date):
        """Update the task completion date"""
        try:
            self.tl.modify_task(task_id, task_completion_date=new_date)
        except TaskException as e:
            print(e)

    def delete_task(self):
        """Action to delete the task if task list in not empty"""
        if self.tl.tasks:
            highlight_input_option(self.show_task_menu_options["3"])
            # display all tasks first to show which ones exist.
            self.tl.print_tasks()

            task_id = input("Enter the task id to delete a particular task: ")

            self.tl.delete_task(task_id)
            print("Task ID '{}' deleted successfully.\n".format(task_id))
        else:
            print(Fore.RED + "No tasks to delete. Task list is empty.\n")

    def search_task(self):
        """Action to search the tasks if task list in not empty"""
        if self.tl.tasks:
            highlight_input_option(self.show_task_menu_options["4"])
            search_string = input("Enter the string to search in tasks: ")

            searched_tasks = self.tl.search(search_string)
            self.tl.print_tasks(searched_tasks)
        else:
            print(Fore.RED + "No tasks to search. Task list is empty.\n")

    def print_tasks(self):
        """Prints all the tasks in the task list"""
        highlight_input_option(self.show_task_menu_options["5"])
        self.tl.print_tasks()

    @staticmethod
    def __is_valid_option(user_input, options):
        """
        Returns True or False,  if the user input option exists
        """
        if isinstance(options, dict):
            valid_options = options.keys()
        elif isinstance(options, TaskList):
            valid_options = [str(task.task_id) for task in options.tasks]
        else:
            valid_options = None

        if user_input in valid_options:
            return True
        else:
            return False

    def run(self):
        """Runs the app until user chooses to quit."""
        print("\nWelcome to To-Do List. Follow the menu options to navigate.\n")
        while True:
            print("********* Menu *********")
            print_options_in_dict(self.show_task_menu_options)
            choice = input("Choose your option: ")

            if choice == '6':
                print("Logging off... Bye.")
                break
            elif TasksMenu.__is_valid_option(choice, self.task_menu_options):
                self.task_menu_options[choice]()
            else:
                print(Fore.RED + "Invalid option\n")


if __name__ == "__main__":
    task_list = TaskList()
    menu = TasksMenu(task_list)
    menu.run()
