print("Hi please choose a category")
print("Python JS HTML")
CHOS_CAT = str("1")


def set_cat(choice):
    """
    This function sets the chosen category for the player
    once the input has been validated
    """
    global CHOS_CAT
    if choice == "1":
        CHOS_CAT = str("1")
        print("category is Python")
    elif choice == "2":
        CHOS_CAT = str("2")
        print("category is JS")
    else:
        CHOS_CAT = str("3")
        print("category is HTML")


def validate_choice(choice):
    """
    This function validates the user input to prevent error
    and allows the while loop in other function to continue on
    return false
    """
    if choice not in ("1", "2", "3"):
        print("Please choose category by typing 1, 2 or 3")
        return False
    else:
        return True


def quest_catg():
    """
    This function asks the player to select a quiz category then
    passes that value to the validator
    """
    validated = 0
    while validated < 1:
        choice = input("Enter your category here 1, 2 or 3:")

        if validate_choice(choice):
            print("Thank you for validating")
            validated += 1
            set_cat(choice)


quest_catg()
print(CHOS_CAT)
