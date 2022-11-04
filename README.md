# **PYTHON QUIZ**

Welcome to my Code Institute Project 3 python app.

## [**Table of Contents**](<#table-of-contents>)

[**OVERVIEW**](<#overview>)

[**EARLY CONCEPT**](<#early-concept>)

[**FLOWCHART**](<#flowchart>)

[**DEPLOYED APP**](<#deployed-app>)
   * [**Menu**](<#menu>)
   * [**Instructions**](<#instructions>)
   * [**Scoretable**](<#scoretable>)
   * [**Choose category**](<#choose-category>)
   * [**Play Game**](<#play-game>)
   * [**UI UX**](<#ui-ux>)
   * [**Notes**](<#notes>)

[**FUTURE FEATURES**](<#future-features>)

[**TESTING**](<#testing>)
   * [**Bugs squashed**](<#bugs-squashed>)
   * [**Known issues**](<#known-issues>)

[**TECH USED**](<#tech-used>)

[**DEPLOYMENT**](<#deployment>)

[**ACKNOWLEDGEMENTS**](<#acknowledgements>)

### OVERVIEW

* The purpose of this project was to show a working app created with Python from scratch. No code base or examples were used (save for the occasional code hint for a specific problem) but all functions were custom designed for this project. My early idea was to design some form of text based adventure, but I didn't want to get bogged down writing a story when displaying what I have learned in terms of coding was the desired result.

* Eventually I decided on a quiz app, it still combined a slightly light hearted fun game concept but required less creative writing and allowed me focus more on showing what I had learned.

* I decided to store all the questions and scores in an external spreadsheet to show I had understood that part of the previous lesson. But in reality there is little reason to store the questions in this manner.

* It is worth noting were a quiz app really required, there are far better technologies to build that in. But again this was purely to show what I had learned.

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### EARLY CONCEPT

#### NOTE - THE TEST VERSION DETAILED BELOW NO LONGER FUNCTION AND ARE PRESENTED PURELY TO SHOW MY WORKFLOW FROM TEST TO FINISHED APP
#### THE LINK TO THE REPO CAN BE FOUND [HERE](https://github.com/JeffreyBull76/quiz-test)

* Once a quiz game had been settled on I took a little time to build a test version on github, I chose not to publish this to Heroku. It was purely for testing how I might construct a quiz. So a very basic question and answer function was created that accessed questions from an external spreadsheet. 

* This early version used iteration to grab the questions from the excel sheet one by one and then passed them to the app to ask the question. While this worked it required many back and forth data requests with the spreadsheet. As this is running on a free version of the google API, this resulted in API errors when the user entered invalid inputs. As it requested the data each time the question was asked, so the user could easily accidentally crash the app.

* This was then addressed with a more efficient pull request from the spreadsheet which rather than asking each question from the sheet, pulled the data row by row and built a list of lists, held as a global variable. We could then iterate through that list. This worked far better and was initially the version I built the main app with. It can be seen in the above link under the file name ***RUN.PY*** (as noted above this no longer functions correctly but is presented as proof of concept)

* The test.py file shows a test of another even more efficient way to access the questions, this was eventually used in the early versions of the main app see [***DEPLOYED APP***](<#deployed-app>) section for more information.

* The quiz.py file is presented as it contains a now defunct version of the code used in the final app. I presented this here to show how much more efficient I made the process after initial testing. But it was not initially part of this test version.

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### FLOWCHART

* Here you can see the general overview the app and how the user navigates through it. 
* Each arrow has at least one validation process in place to prevent invalid inputs.

![](assets/rmimages/Project3FlowChart.jpeg)

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### DEPLOYED APP

[LINK TO DEPLOYED APP](https://ciproject3-python-quiz.herokuapp.com/)

* ### Menu
   * The main menu screen:
   * ![](assets/rmimages/menu_1.png)
   * This is our deployed landing page. It presents the user with 3 options (see flowchart)
   * As you will see throughout the project, a function is used here to explicitly check for the required input or a loop will continue asking the player to select correctly.
   * Instructions gives a brief overview of how to use the app and returns the user automatically to the menu
   * Scoretable loads the saved scores from out external spreadsheet and uses an imported library called [Tabulate](https://pypi.org/project/tabulate/) to build a scoretable
   * And play game takes us to a catgeory choice screen
--------------------------------------------------------
* ### Instructions
   * ![](assets/rmimages/instructions1.png)
   * As detailed above this lays out how to use the app
   * A choice was made to automatically send the user back to the menu as no further interaction is required. 
   * This cuts down on code and pointless requests for user input.
--------------------------------------------------------
* ### Scoretable
   * ![](assets/rmimages/score1.png)
   * This function pulls the data from our spreadsheet (all saved scores are grabbed) and uses the imported tabulate library to display those for the user
   * It works by using the gspread get_all_values function to build a list of lists with one easy request.
   * This then requires a user input to return to the main menu. That works on a very simple while loop inside the function itself to validate input.
--------------------------------------------------------
* ### Choose category
   * ![](assets/rmimages/select1.png)
   * 
--------------------------------------------------------
* ### Play game
   * ![](assets/rmimages/quiz1.png)
   * ![](assets/rmimages/gameover1.png)
--------------------------------------------------------
* ### UI UX
   * ![](assets/rmimages/invalidname1.png)
   * ![](assets/rmimages/invalidquest1.png)
--------------------------------------------------------
* ### Notes
--------------------------------------------------------
### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### FUTURE FEATURES

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### TESTING

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### TECH USED

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### DEPLOYMENT

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------
### ACKNOWLEDGEMENTS

### [Contents Menu](<#table-of-contents>)
--------------------------------------------------------