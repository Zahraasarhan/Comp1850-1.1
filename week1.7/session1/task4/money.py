# from Week 1.5, Session 2: Task 3

class Money:
    """
    Represents an amount of money, in British Pounds Sterling.
    The amount is stored as pounds and pence.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        Args:
            pounds (int): Number of pounds (must be non-negative).
            pence (int): Number of pence (must be between 0 and 99).

       Raises:
           TypeError: If pounds or pence is not an integer.
           ValueError: If pounds or pence is outside the vaild range.
        """
        #Check that pounds is an integer.
        if not isinstance(pounds, int):
            raise TypeError("pounds must be an integer")
        
        #Check that pence is an integer.
        if not isinstance(pence, int):
            raise TypeError("pence must be an integer")
        
        #Negative amounts of pounds are not allowed.
        if pounds < 0:
            raise ValueError("pounds must be >= 0")
        
        #Pence must be between 0 and 99.
        if pence < 0 or pence > 99:
            raise ValueError("pence must be in range 0-99")
        
        #Store the vaildated values in the object.
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # :02d ensures pence always has two digits.
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.

        Args:
             other (Money): The amount to add.
        Returns:
            Money: A new object containing the total amount.
        Raises:
            TypeError: If the other object is not a Money abject.
        """
        #Only Money objects can be added together.
        if not isinstance(other, Money):
            raise TypeError("other object must be a Money")
        #Add the pounds from both objects.
        sum_pounds = self.pounds + other.pounds
        #Convert every 100 pence into one extra pound. 
        extra_pound = (self.pence + other.pence) // 100
        # Keep the remaining pence after conversion.
        sum_pence = (self.pence + other.pence) % 100
        # Return the result as a new money object.
        return Money(sum_pounds + extra_pound, sum_pence)
    