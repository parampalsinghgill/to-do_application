from .user import User
from exceptions.exceptions_auth import AuthException, InvalidUsernameError, WrongPasswordError


class Authenticator:
    """Authenticates the users to log in or offer them to sign up"""

    def __init__(self):
        """Initializes the class with set of users"""
        self.users = {}

    def signup(self, username, email, password):
        """
        Create new user and add to the user dictionary
        :param username: the username of the user
        :param email: user email
        :param password: user password
        :return: boolean, True if the signup was successful else False
        """
        try:
            self.users[username] = User(username, email, password)
        except AuthException as e:
            print(e)

    def login(self, username, password):
        """
        Login existing user with username and password
        :param username: the name of the user
        :param password: the password of the user
        :return: True or False if login was successful
        """
        if username in self.users:
            if self.users[username].match(password):
                self.users[username].is_logged_in = True
                return True
            else:
                raise WrongPasswordError("The password does not match.")
        else:
            raise InvalidUsernameError("The user does not exist. Please sign up to continue.")
