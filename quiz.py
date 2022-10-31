"""
Onload text and define global list that holds the questions chosen
"""
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

    while quest_num <= 6:
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


def game_over():
    """
    end game and save score function
    """
    print(f"Your score was {PLYR_SCORE}/6")
    print("GAME OVER!\n")
    name_val = 1

    while name_val < 2:
        ply_nam = input("ENTER YOUR NAME TO SAVE YOUR SCORE\n")

        if ply_nam and len(ply_nam) >= 5:
            str1 = ply_nam
            str2 = PLYR_SCORE
            final_str = f'{str1} ' + f'{str2}'
            final_score = list(final_str.split(" "))
            score_value = SHEET.worksheet("scores")
            score_value.append_row(final_score)
            name_val += 1
        else:
            print("\033[0;37;41mEnter a valid name...\033[0;37;48m")
            print("\033[0;37;41mMinimum 5 characters !\033[0;37;48m\n")


def play_game(val1, val2):
    """
    Allows iteration through different questions sequences
    """
    print("\033[1;36;40mSCORE = " + f'{PLYR_SCORE}\033[0;37;48m')
    if val1 < 60:
        ask_question(val1, val2)
    else:
        # sys.exit("GAME OVER!")
        game_over()     
        # exec(open("run.py").read())


play_game(0, 8)
