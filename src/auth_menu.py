from common import print_options_in_dict, highlight_input_option, quit_app
from pwinput import pwinput
from getpass import getpass
from auth import Authenticator
from exceptions import AuthException


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

        username, email = AuthMenu.__ask_for_username_and_email()
        password = pwinput(prompt="Choose a password: ", mask='*')
        # password = getpass("Choose a password: ")

        try:
            self.authenticator.signup(username, email, password)
            print("Sign up successful. Continue to login? (y/n)")
            user_input = input()
            if user_input == 'y':
                self.login()
        except AuthException as e:
            print("Sign up error: ", e)

    def login(self):
        """Logs in existing user"""
        username, email = AuthMenu.__ask_for_username_and_email()

        try:
            self.authenticator.login(username, email)
            print("Login successful.")
        except AuthException as e:
            print("Log in error: ", e)

    @staticmethod
    def __ask_for_username_and_email():
        """Ask username and email from the user"""
        username = input("Please provide a username: ")
        email = input("Please provide an email address: ")
        return username, email

    def run(self):
        """Run the command line options"""
        print("Welcome to ToDo app.")
        while True:
            print_options_in_dict(self.print_auth_menu_options)
            user_input = input("Choose an option: ")

            try:
                action = self.auth_menu_options[user_input]
                action()
            except KeyError as e:
                print("Invalid Option\n")


if __name__ == "__main__":
    app = AuthMenu()
    app.run()

