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

print("Your answers are given by selecting the letter for each choice")
print("So you if you think the answer is B you would type B\n")

QLIST = []


def set_questions():
    """
    Question function
    """
    quest = SHEET.worksheet(f'{CHOS_CAT}')
    quest_num = 1
    print("\033[1;31;40mBuilding question database...\033[0;37;48m\n")

    while quest_num <= 7:
        for i in range(1, 6):
            QLIST.extend(
                [quest.col_values(i)[0], quest.col_values(i)[quest_num]]
                )

        quest_num += 1


set_questions()


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


def check_question(answer, rang1, rang2):
    """
    Checks to see if answer is correct or incorrect
    """
    global PLYR_SCORE
    if answer.upper() == QLIST[rang2 + 1]:
        print("CORRECT !\n")
        PLYR_SCORE += 1
    else:
        print("INCORRECT !\n")

    play_game(rang1 + 10, rang2 + 10)


def ask_question(rang1, rang2):
    """
    Question function
    """
    quest_cnt = 1

    while quest_cnt < 2:
        for i in range(rang1, rang2, 2):
            print(f"\033[1;32;40m{QLIST[i]}: {QLIST[i + 1]}\033[0;37;48m")

        answer = input("Enter your answer here:\n")

        if validate_question(answer):
            check_question(answer, rang1, rang2)
            quest_cnt += 1


def play_game(val1, val2):
    """
    Allows iteration through different questions sequences
    """
    print("\033[1;36;40mSCORE = " + f'{PLYR_SCORE}\033[0;37;48m')
    if val1 < 70:
        ask_question(val1, val2)
    else:
        # sys.exit("GAME OVER!")
        print("GAME OVER!")
        exec(open("run.py").read())


play_game(0, 8)


# NEXT we must track and itterate the players score
# THEN write that score to the worksheet with a username

# EXTRA WORK We must control the game over part and allow the user more control
# over when the run.py file is executed to play again
