from common import print_options_in_dict, highlight_input_option
from pwinput import pwinput
from auth import Authenticator
from exceptions import AuthException


class AuthMenu:
    """Menu to interact with auth module"""

    def __init__(self):
        """Initializes AithMenu with instance variables"""
        self.auth_menu_options = {
            "1": self.login,
            "2": self.signup,
            "3": quit
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

        username = input("Please provide a username: ")
        email = input("Please provide an email address: ")
        password = pwinput(prompt="Choose a password:", mask='*')

        try:
            self.authenticator.signup(username, email, password)
        except AuthException as e:
            print("Sign up error: ", e)

    def login(self):
        """Logs in existing user"""
        pass

    def run(self):
        """Run the command line options"""
        print("Welcome to ToDo app.")
        while True:
            print_options_in_dict(self.print_auth_menu_options)
            user_input = input("Choose an option: ")

            try:
                action = self.auth_menu_options["user_input"]
                action()
            except KeyError as e:
                print("Invalid Option\n")



