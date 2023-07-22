from datetime import date, timedelta
from enum import Enum

task_id = 0


class Status(Enum):
    """Manage the status of the task object"""
    NEW = 0
    IN_PROGRESS = 1
    DONE = 2


class ToDoTask:
    """Creates a to do task"""

    def __init__(self, task_name, days_to_complete):
        self.task_name = task_name
        self.creation_date = date.today()
        self.completion_date = date.today() + timedelta(days=days_to_complete)
        self.status = Status.NEW

        global task_id
        task_id += 1
        self.id = task_id

    def match(self, filter_string):
        """Check if the task matches the filter text"""
        return str(filter_string) in str(self.task_name)
