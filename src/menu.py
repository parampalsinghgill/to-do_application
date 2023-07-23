from task_list import TaskList


class Menu:
    """Creates a command line interactive tool for users"""

    def __init__(self):
        self.tl = TaskList()
        self.menu = {
            "1": self.create_task,
            "2": self.modify_task,
            "3": self.delete_task,
            "4": self.search_task,
            "5": self.print_tasks,
            "6": quit
        }
        self.print_menu = {
            "1": "Create a new task",
            "2": "Modify an existing task",
            "3": "Delete an existing task",
            "4": "Search existing tasks",
            "5": "Show all existing tasks",
            "6": "Exit"
        }

    def display_menu(self):
        """Display the menu options and ask user choice"""
        print("********* Menu *********")
        for item in self.print_menu.items():
            print("{} : {}".format(item[0], item[1]))
        print()

    def get_input_from_user(self):
        """Show options and ask user for the input. Call the appropriate method accordingly."""
        self.display_menu()
        choice = input("Choose your option: ")
        if choice in self.menu.keys():
            self.menu[choice]()
        else:
            print("Invalid option\n")

    def create_task(self):
        """Action on create task option"""
        self.__highlight_input_option(self.print_menu["1"])

        task_name = input("Enter task: ")
        days_to_complete = input("Enter number of days to complete: ")

        self.tl.create_task(task_name, days_to_complete)
        print("A task '{}' has been created and added to TO-Do list.\n".format(task_name))

    def modify_task(self):
        """Action to modify the task"""
        self.__highlight_input_option(self.print_menu["2"])

        # display all tasks first to show which ones exist.
        print("The following is the list of all existing tasks:")
        self.tl.print_tasks()

        task_id = input("Enter the task id to modify: ")
        task_name = input("Enter updated task name: ")

        self.tl.modify_task(task_id, task_name)
        print("Task ID '{}' modified successfully.\n".format(task_id))

    def delete_task(self):
        """Action to delete the task"""
        self.__highlight_input_option(self.print_menu["3"])
        # display all tasks first to show which ones exist.
        self.tl.print_tasks()

        task_id = input("Enter the task id to delete a particular task: ")

        self.tl.delete_task(task_id)
        print("Task ID '{}' deleted successfully.\n".format(task_id))

    def search_task(self):
        """Action to search the tasks"""
        self.__highlight_input_option(self.print_menu["4"])
        search_string = input("Enter the string to search in tasks: ")

        searched_tasks = self.tl.search(search_string)
        self.tl.print_tasks(searched_tasks)

    def print_tasks(self):
        """Prints all the tasks in the task list"""
        self.__highlight_input_option(self.print_menu["5"])
        self.tl.print_tasks()

    @staticmethod
    def __highlight_input_option(option):
        """Highlights the option user chose and what he is doing currently"""
        print("\n######### Entered option to '{}' #########".format(option.lower()))

    def run(self):
        """RUns the app until user chooses to quit."""
        print("\nWelcome to To-Do application. Follow the menu options to navigate.\n")
        while True:
            self.get_input_from_user()


if __name__ == "__main__":
    menu = Menu()
    menu.run()
