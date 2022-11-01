"""
Import modules for use in app
"""
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

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
Title screen
"""
print("""\033[1;32;40m
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
\033[0;37;48m\n""")

CHOS_CAT = str("1")
PLYR_SCORE = 0
"""
Set the two global values used throughout our quiz
"""


def instructions():
    """
    Instructions function
    """
    print("\033[1;32;40mWELCOME TO THE QUIZ !\033[0;37;48m\n")
    print("In the main menu you can select a quiz category")
    print("A question list will then be built from an external spreadsheet")
    print("You will then answer each question by selecting A B or C\n")
    print("NOTE - YOU MUST ANSWER BY TYPING THE LETTER A, B OR C")
    print("No other input is allowed...\n")
    print("At game over you save your score and choose to play again!")
    print("\033[1;32;40mVIEW THE SCORETABLE AT MAIN MENU!\033[0;37;48m")
    print("______________________________________________________________\n")
    start_menu()


def scoretable():
    """
    Scoretable function
    """
    print("CHECK OUT OUR HIGH SCORE TABLE BELOW\n")
    get_scores = SHEET.worksheet('scores').get_all_values()
    score_list = get_scores
    print(tabulate(score_list, headers="firstrow"))
    print("______________________________________________________________\n")

    validated = 0
    while validated < 1:
        cont = input("PRESS A TO CONTINUE\n")
        print("                          \n")
        if cont.upper() == "A":
            validated += 1
            start_menu()
        else:
            print("\033[0;37;41mINVALID INPUT !\033[0;37;48m\n")


def start_menu():
    """
    Menu that allows players to select from instructions
    scoretable or play the game
    """
    global PLYR_SCORE
    PLYR_SCORE = 0
    print("\033[1;36;40mSELECT FROM THE MENU BELOW TO START:\033[0;37;48m")
    print("INSTRUCTIONS - A")
    print("SCORETABLE - B")
    print("PLAY GAME - C")
    men_choice = input("ENTER A, B OR C\n")
    print("______________________________________________________________\n")
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
    this value is held globally to avoid to much passing around
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
        print("\033[1;32;40mSELECT A QUIZ CATEGORY\033[0;37;48m\n")
        print("PYTHON = 1 | JS = 2 | HTML = 3\n")

        choice = input("ENTER CATEGORY HERE - 1, 2 or 3:\n")

        if validate_choice(choice):
            print("Thank you for validating\n")
            validated += 1
            set_cat(choice)
            q_l = set_questions()
            play_game(0, 1, q_l)


def set_questions():
    """
    This function uses the global chosen cat variable
    to grab the correct questions from our external spreadsheet
    this is then compiled to a list of lists and returned for use
    in other functions
    """
    print("\033[1;31;40mPLEASE ANSWER BY TYPING A, B or C !\033[0;37;48m")
    print("So you if you think the answer is B you would type B\n")
    get_quest = SHEET.worksheet(f'{CHOS_CAT}').get_all_values()
    return get_quest


def validate_question(answer):
    """
    Checks for valid answer
    This is explicitly set to only accept A, B or C
    but does convert small to upper case to avoid
    being overly picky
    """
    if answer.upper() not in ("A", "B", "C"):
        print("\033[0;37;41mANSWER IS NOT VALID !\033[0;37;48m")
        print("Please answer with A, B or C !")
        return False
    else:
        print("          \n")
        return True


def check_question(answer, rng1, rng2, q_l):
    """
    Checks to see if answer is correct or incorrect
    converts the input again to uppercase to avoid confusion
    then checks it against the answers pulled from out external sheet
    ranges are used to control this
    """
    global PLYR_SCORE
    if answer.upper() == q_l[rng2][4]:
        print("\033[1;32;40mCORRECT !\033[0;37;48m")
        print("\033[1;32;40mSCORE + 1\033[0;37;48m\n")
        PLYR_SCORE += 1
    else:
        print("\033[1;31;40mINCORRECT !\033[0;37;48m\n")

    play_game(rng1, rng2 + 1, q_l)


def ask_question(rng1, rng2, q_l):
    """
    Takes the range values from the the play game function and
    uses the them to print the relevant questions from our
    list of lists, checks valid input and then checks to
    see if the answer is correct in a while loop
    """
    quest_cnt = 1

    while quest_cnt < 2:
        print(f"QUESTION NUMBER: {rng2}")
        for i in range(0, 4):
            print(f"\033[1;34;40m{q_l[rng1][i]}:\033[0;37;48m {q_l[rng2][i]}")

        answer = input("\033[1;32;40mEnter answer here:\033[0;37;48m\n")

        if validate_question(answer):
            check_question(answer, rng1, rng2, q_l)
            quest_cnt += 1


def game_over():
    """
    accepts no values itself, runs on game over allows
    user to input their name (which we strip of all whitespace)
    and then stores this to our score spreadsheet, will not allow
    inputs under 5 characters.
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
            print("          \n")
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
    Passes the range values to our ask question function and also ensures
    our list of lists (questions) are correctly passed around for use in
    game loop. Each time this runs it increments a val which checks for
    the end of the game (no more questions) based on a known value (10)
    """
    print("\033[1;36;40mSCORE = " + f'{PLYR_SCORE}\033[0;37;48m')
    if val2 < 11:
        ask_question(val1, val2, q_l)
    else:
        game_over()


start_menu()
