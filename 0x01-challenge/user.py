#!/usr/bin/python3
"""
User class
"""


class User():
    """Implement User class"""

    def __init__(self):
        """Initialize user object"""
        self.__email = None

    @property
    def email(self):
        """gets email for user"""
        return self.__email

    @email.setter
    def email(self, value):
        """Sets email for user"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
