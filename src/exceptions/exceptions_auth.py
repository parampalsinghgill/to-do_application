class AuthException(Exception):
    """Parent exception for all exceptions in auth module"""
    pass


class InvalidUsernameError(AuthException):
    """Exception if the username is invalid"""
    pass


class InvalidEmailError(AuthException):
    """Exception if the email is invalid"""
    pass


class InvalidPasswordError(AuthException):
    """Exception if the password being registered is invalid"""
    pass


class WrongPasswordError(AuthException):
    """Exception if the entered password is wrong"""
    pass

