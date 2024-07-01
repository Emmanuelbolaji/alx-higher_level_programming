#!/usr/bim/python3
"""
This module defines the MyList class, which inherits from list.
"""


class MyList(list):
    """
    MyList class that inherits from list.

    This class extends the built-in list class with an additional
    method to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list.
        It creates a new sorted list and prints it.
        """
        print(sorted(self))
