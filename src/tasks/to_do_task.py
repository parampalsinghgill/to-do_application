from datetime import datetime, date, timedelta
from status import Status
from exceptions import InvalidStatusError, InvalidDateError


task_id = 0


class ToDoTask:
    """Creates a to do task"""

    def __init__(self, task_name, days_to_complete):
        self.__task_name = task_name
        self.__creation_date = date.today()
        self.__completion_date = date.today() + timedelta(days=int(days_to_complete))
        self.__status = Status.NEW

        global task_id
        task_id += 1
        self.__id = task_id

    def match(self, filter_string):
        """
        Check if the task matches the filter text and return a boolean
        @param filter_string: the string to match
        """
        return str(filter_string) in str(self.task_name)

    @property
    def task_id(self):
        """Get the task id"""
        return self.__id

    @property
    def creation_date(self):
        """Get the creation date of the task"""
        return self.__creation_date

    @property
    def task_name(self):
        """
        Get or set the name of the task.
        """
        return self.__task_name

    @task_name.setter
    def task_name(self, val):
        self.__task_name = val

    @property
    def completion_date(self):
        """Get or set the target completion date of the task"""
        return self.__completion_date

    @completion_date.setter
    def completion_date(self, val):
        try:
            self.__completion_date = datetime.strptime(val, '%Y%m%d')
        except TypeError:
            raise InvalidDateError("Completion date for ", self.__id, " was not updated due to invalid format.")

    @property
    def status(self):
        """Get or set the status of the task"""
        return self.__status

    @status.setter
    def status(self, val):
        valid_values = [item.value for item in Status.get_class_attribute_list()]

        if val in valid_values:
            self.__status = Status.get_member(val)
        else:
            raise InvalidStatusError("Status for ", self.__id, " was not updated due to invalid status.")
