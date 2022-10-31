"""
Import modules for use in app
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
PLYR_SCORE = 0
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

CHOS_CAT = str("1")
PLYR_SCORE = 0


def instructions():
    """
    Instructions function
    """
    print("Welcome to the quiz")
    print("""
    In the main menu you can select a quiz category 
    Upon selecting a question list will be built from an external spreadsheet
    You will then answer each question by selecting A B or C
    NOTE YOU MUST ANSWER WITH A B OR C for each question
    No other input is allowed...
    Or you can view the scores of the top 3 players by selecting the scoretable
    """)
    start_menu()


def start_menu():
    """
    test menu
    """
    global PLYR_SCORE
    PLYR_SCORE = 0
    print(PLYR_SCORE)
    print("SELECT FROM THE MENU BELOW TO START:")
    print("INSTRUCTIONS - A")
    print("SCORETABLE - B")
    print("PLAY GAME - C")
    men_choice = input("ENTER A, B OR C\n")
    if men_choice.upper() == "A":
        instructions()
    elif men_choice.upper() == "B":
        scoretable()
    elif men_choice.upper() == "C":
        quest_catg()
    else:
        start_menu()


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
            q_l = set_questions()
            play_game(0, 1, q_l)
# exec(open("quiz.py").read())


def set_questions():
    """
    Question function
    """
    print("Your answers are given by selecting the letter for each choice")
    print("So you if you think the answer is B you would type B\n")
    get_quest = SHEET.worksheet(f'{CHOS_CAT}').get_all_values()
    return get_quest


def validate_question(answer):
    """
    Checks for valid answer
    """
    if answer.upper() not in ("A", "B", "C"):
        print("\033[0;37;41mANSWER IS NOT VALID !\033[0;37;48m")
        print("Please answer with A, B or C !")
        return False
    else:
        print("Answer is valid!\n")
        return True


def check_question(answer, rng1, rng2, q_l):
    """
    Checks to see if answer is correct or incorrect
    """
    global PLYR_SCORE
    if answer.upper() == q_l[rng2][4]:
        print("CORRECT !\n")
        PLYR_SCORE += 1
    else:
        print("INCORRECT !\n")

    play_game(rng1, rng2 + 1, q_l)


def ask_question(rng1, rng2, q_l):
    """
    Question function
    """
    quest_cnt = 1

    while quest_cnt < 2:
        for i in range(0, 4):
            print(f"\033[1;34;40m{q_l[rng1][i]}:\033[0;37;48m {q_l[rng2][i]}")

        answer = input("\033[1;32;40mEnter answer here:\033[0;37;48m\n")

        if validate_question(answer):
            check_question(answer, rng1, rng2, q_l)
            quest_cnt += 1


def game_over():
    """
    end game and save score function
    """
    print(f"Your score was {PLYR_SCORE}/10")
    print("GAME OVER!\n")
    name_val = 1

    while name_val < 2:
        def remove(play_name):
            return play_name.replace(" ", "")

        play_name = input("ENTER YOUR NAME TO SAVE YOUR SCORE\n")
        ply_nam = remove(play_name)

        if ply_nam and len(ply_nam) >= 5:
            str1 = ply_nam
            str2 = PLYR_SCORE
            final_str = f'{str1} ' + f'{str2}'
            final_score = list(final_str.split(" "))
            score_value = SHEET.worksheet("scores")
            score_value.append_row(final_score)
            name_val += 1
            start_menu()
        else:
            print("\033[0;37;41mEnter a valid name...\033[0;37;48m")
            print("\033[0;37;41mNo blankspaces allowed...\033[0;37;48m")
            print("\033[0;37;41mMinimum 5 characters !\033[0;37;48m\n")


def play_game(val1, val2, q_l):
    """
    Allows iteration through different questions sequences
    """
    print("\033[1;32;40mSCORE = " + f'{PLYR_SCORE}\033[0;37;48m')
    if val2 < 11:
        ask_question(val1, val2, q_l)
    else:
        game_over()


start_menu()
