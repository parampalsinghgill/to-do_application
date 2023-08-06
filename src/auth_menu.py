from common import print_options_in_dict, highlight_input_option, quit_app
from pwinput import pwinput
from getpass import getpass
from auth import Authenticator
from exceptions import AuthException
from tasks_menu import TasksMenu
from colorama import Fore, init

init(autoreset=True)


class AuthMenu:
    """Menu to interact with auth module"""

    def __init__(self):
        """Initializes AithMenu with instance variables"""
        self.auth_menu_options = {
            "1": self.login,
            "2": self.signup,
            "3": quit_app
        }
        self.print_auth_menu_options = {
            "1": "Login",
            "2": "Signup",
            "3": "Quit"
        }

        self.authenticator = Authenticator()

    def signup(self):
        """Sign up a new user"""
        highlight_input_option(self.print_auth_menu_options["2"])

        email = AuthMenu.__ask_for_email()
        username, password = AuthMenu.__ask_for_username_and_password()

        try:
            self.authenticator.signup(username, email, password)
            print("Sign up successful. Continue to login? (y/n)")
            user_input = input()
            if user_input == 'y':
                self.login()
        except AuthException as ex:
            print(Fore.RED + "Sign up error: ", ex)

    def login(self):
        """Logs in existing user"""
        username, password = AuthMenu.__ask_for_username_and_password()

        try:
            self.authenticator.login(username, password)
            print("Login successful.")

            # user logged in, let user access his to do list
            user = self.authenticator.users[username]
            task_menu = TasksMenu(user.tasks)
            task_menu.run()
        except AuthException as ex:
            print(Fore.RED + "Log in error: ", ex)

    @staticmethod
    def __ask_for_username_and_password():
        """Ask username and password from the user"""
        username = input("Please provide a username: ")
        password = pwinput(prompt="Choose a password: ", mask='*')
        # password = getpass("Choose a password: ")

        return username, password

    @staticmethod
    def __ask_for_email():
        """Ask email from the user"""
        email = input("Please provide an email address: ")
        return email

    def run(self):
        """Run the command line options"""
        length_of_asterisk = 37
        welcome_msg = " Welcome to ToDo app "
        length_of_asterisk_around_welcome_msg = int((length_of_asterisk-len(welcome_msg))/2)

        print("*" * length_of_asterisk)
        print("*" * length_of_asterisk_around_welcome_msg +
              " Welcome to ToDo app " +
              "*" * length_of_asterisk_around_welcome_msg)
        print("*" * length_of_asterisk)

        while True:
            print_options_in_dict(self.print_auth_menu_options)
            user_input = input("Choose an option: ")

            try:
                action = self.auth_menu_options[user_input]
                action()
            except KeyError as e:
                print(Fore.RED + "Invalid Option\n")


if __name__ == "__main__":
    app = AuthMenu()
    try:
        app.run()
    except SystemExit as e:
        print(e)

