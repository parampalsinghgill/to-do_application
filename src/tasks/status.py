import inspect
from collections import namedtuple


named_tuple = namedtuple("Status", "value name")


class Status(named_tuple):
    """Manage the status of the task object"""
    NEW = named_tuple(0, "new")
    IN_PROGRESS = named_tuple(1, "in progress")
    DONE = named_tuple(2, "done")

    @classmethod
    def get_class_attribute_list(cls):
        """
        Gets the attribute list of the class
        :return: list of class attributes
        """
        # get all the class attributes in a list
        attributes = []
        for i in inspect.getmembers(cls):
            if not i[0].startswith('_'):
                if isinstance(i[1], named_tuple):
                    attributes.append(i[1])
        return attributes

    @classmethod
    def get_member(cls, val):
        """
        Returns the value of the tuple for which the string matches
        :param val: the input string value
        :return: int value matching the string in the tuple
        """
        attributes = cls.get_class_attribute_list()
        return_value = None
        for item in attributes:
            if val == item.name or val == item.value:
                return_value = item
                break

        return return_value
