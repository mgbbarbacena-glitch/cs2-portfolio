# Clean Decision Code Makeover: Student Score Checker
**Name:** Ma. Gia B. Barbacena

**Section:** Dahlia

--------

## Activity Overview
In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

-----

The classifications are:
| Score | Classification |
| --: | --- |
| 90-100 | Outstanding |
| 80-89 | Very Satisfactory |
| 75-79 | Satisfactory |
| below 75 | Needs Improvement |

Scores below 0 or above 100 is considered invalid.

-----

# Part 1 - Analyze the Logic

##Input:
What information does the program need?
>The program needs a student's score.

##Valid Range

**Minimum valid score:**
>0

**Maximum valid score:**
>100

##Possible Outputs:
List all possible outputs of the program.
1. Outstanding
2. Very Satisfactory
3. Satisfactory
4. Needs Improvement
5. Invalid Score

##Boundary Condition:
What condition will you use to determine whether the score is valid?
>The score is invalid if it is less than 0 or greater than 100.

##Multiple Decision Paths:
Explain how the program decides which classification should be displayed.
>The program checks the score and follows the correct condition. It displays Outstanding for 90-100, Very Satisfactory for 80-89, Satisfactory for 75-79, and Needs Improvement for scores below 75.

# Part 2 - Flowchart
##Flowchart
[Score Checker Flowchart](q1/score_checker_flowchart.png)

# Part 3 - Pseudocode

START

INPUT score

IF score <0 OR score > 100 THEN
    DISPLAY "Invalid Score"
ELSE IF score >= 90 THEN
    DISPLAY "Outstanding"
ELSE IF score >= 80 THEN
    DISPLAY "Very Satisfactory"
ELSE IF score >= 75 THEN
    DISPLAY "Satisfactory"
ELSE
    DISPLAY "Needs Improvement"
....
END

--------------

# Part 4 - Clean Code Implementation
## Source code: 
[Score Checker Source Code](q1/score_checker.py)

----------

# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
| --- | ---: | ---| --- |--- | --- |
| 1 | -1 | Below minimum | Invalid Score | Invalid Score | Pass |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | Pass |
| 3 | 74 | Below satisfactory boundary | Needs Improvement | Needs Improvement | Pass |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | Pass |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | Pass |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | Pass |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | Pass |
| 8 | 101 | Above maximum | Invalid Score Invalid Score | Pass |

...
