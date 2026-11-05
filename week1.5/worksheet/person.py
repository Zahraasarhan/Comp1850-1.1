# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a Person with a nane and date of birth.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name == "":
            raise ValueError("name must not be empty")
        if not isinstance(birth, date):
            raise TypeError("birth must be a be a date object")
        
        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the uppercase initials of the person's name.
        """
        parts = self.name.split()
        result = ""

        for part in parts:
            result = result + part[0].upper()

        return result
    def is_birthday(self):
        """
        Returns True if today is the person's birthday,
        False otherwise.
        """
        today = date.today()
        return (today.month == self.birth.month 
                and today.day == self.birth.day)







    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
