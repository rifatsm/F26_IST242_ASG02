"""
Layer 1: Personal Library Manager - List of Titles
=====================================================
Purpose
-------
This is the FIRST layer of the Personal Library Manager project.
The goal here is not efficiency or good design -- it is to practice
basic Python control flow (loops, conditionals) and basic list
operations before introducing more advanced data structures.

Data Model
----------
The entire library is represented as a single list of strings:

    library = ["Dune", "1984", "The Hobbit"]

Limitations (intentional, to motivate Layer 2)
-----------------------------------------------
- Only the title is stored; there is no place for author or year.
- Checking for a duplicate title requires an O(n) linear scan.
- There is no structure for "author" statistics at all.

These limitations are exactly why the project moves on to Layer 2.
"""

def display_menu():
    """Display the main menu options for the Personal Library Manager.

    This menu is invoked by the main function on entry point, grabs an input later in the main function,
    and forwards to that execution by other functions

    Parameters:
        None
    Returns:
        None
    """
    print("\n========== Personal Library Manager =========")
    print("Please select an option:")
    print("1. Add a book title")
    print("2. Remove a book")
    print("3. List all book titles")
    print("4. Search a book title")
    print("5. Exit")

def main():
    display_menu()

# __name__ dunder method ensure the main is executed when the file is ran 
# but not when it is imported library
if __name__ == "__main__":
    main()