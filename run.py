print("Hi please choose a category")
print("Python JS HTML")
CHOS_CAT = str("1")


def set_cat(choice):
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
    if choice not in ("1", "2", "3"):
        print("Please choose category by typing 1, 2 or 3")
        return False
    else:
        return True


def quest_catg():
    validated = 0
    while validated < 1:
        choice = input("Enter your category here 1, 2 or 3:")

        if validate_choice(choice):
            print("Thank you for validating")
            validated += 1
            set_cat(choice)


quest_catg()
print(CHOS_CAT)