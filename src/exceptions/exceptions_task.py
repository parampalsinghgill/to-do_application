class TaskException(Exception):
    """Parent exception for all exceptions in tasks module"""


class InvalidStatusError(TaskException):
    """Exception if the status of the task is invalid"""
    pass


class InvalidDateError(TaskException):
    """Exception if the date of the task is invalid"""
    pass


class InvalidTaskError(TaskException):
    """Exception if the task is not found"""
    pass
