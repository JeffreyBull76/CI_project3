"""
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz_questions')

"""
Welcome message and basic instructions text
then ask for player input
"""

print("""
 ██████  ██████  ██████  ███████ 
██      ██    ██ ██   ██ ██
██      ██    ██ ██   ██ █████   
██      ██    ██ ██   ██ ██  
 ██████  ██████  ██████  ███████ 

 ██████  ██    ██ ██ ███████
██    ██ ██    ██ ██    ███      
██    ██ ██    ██ ██   ███   
██ ▄▄ ██ ██    ██ ██  ███        
 ██████   ██████  ██ ███████
\n""")
print("WELCOME HUMAN... ARE YOU READY TO PLAY?")
CHOS_CAT = str("1")
PLYR_SCORE = 0


def set_cat(choice):
    """
    This function sets the chosen category for the player
    once the input has been validated
    """
    global CHOS_CAT
    if choice == "1":
        CHOS_CAT = str("1")
        print("category is Python\n")
    elif choice == "2":
        CHOS_CAT = str("2")
        print("category is JS\n")
    else:
        CHOS_CAT = str("3")
        print("category is HTML\n")


def validate_choice(choice):
    """
    This function validates the user input to prevent error
    and allows the while loop in other function to continue on
    return false
    """
    if choice not in ("1", "2", "3"):
        print("\033[0;37;41mChoose category by typing 1, 2 or 3\033[0;37;48m")
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
        print("SELECT A CATEGORY TO CHOOSE YOUR QUIZ SUBJECT\n")
        print("Python = 1 | JS = 2 | HTML = 3\n")

        choice = input("Enter your category here 1, 2 or 3:\n")

        if validate_choice(choice):
            print("Thank you for validating\n")
            validated += 1
            set_cat(choice)


quest_catg()

exec(open("quiz.py").read())
