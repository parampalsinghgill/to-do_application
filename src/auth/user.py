import re
import hashlib
from exceptions.exceptions_auth import InvalidUsernameError, InvalidEmailError, InvalidPasswordError
from tasks import TaskList


class User:
    """Creates a user account"""

    user_id = 1
    __length_of_username = 3
    __length_of_password = 5
    __regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def __init__(self, username, email, password):
        """Initiates the user account with username, email and password"""
        self.username = username
        self.email = email
        self.__password = self.__encrypt_password(password)
        self.is_logged_in = False

        self.__id = User.user_id
        User.user_id += 1

        self.tasks = TaskList()

    @property
    def id(self):
        """Get the user id"""
        return self.__id

    @property
    def username(self):
        """Get the username"""
        return self.__username

    @username.setter
    def username(self, val):
        """Set the username"""
        if type(val) == str and len(val) >= User.__length_of_username:
            self.__username = val
        else:
            raise InvalidUsernameError("Username is not valid, must be >= ", User.__length_of_username, " characters")

    @property
    def email(self):
        """Get the email of the user"""
        return self.__email

    @email.setter
    def email(self, val):
        """Set the email of the user"""
        if re.fullmatch(User.__regex, val):
            self.__email = val
        else:
            raise InvalidEmailError("Email is not valid, must be username@domain.com")

    def __encrypt_password(self, password):
        """Sets the user password and checking the length and encrypting"""
        if len(password) >= User.__length_of_password:
            return self.__encrypt_string(self.username + password)
        else:
            raise InvalidPasswordError("Password must be at least ", User.__length_of_password, " characters")

    @staticmethod
    def __encrypt_string(string):
        """Encrypt the string with sha256"""
        byte_string = string.encode()
        sha_string = hashlib.sha256(byte_string).hexdigest()
        return sha_string

    def match(self, password):
        """Match the password and return a bool"""
        match = False
        if self.__encrypt_string(self.username + password) == self.__password:
            match = True
        return match
