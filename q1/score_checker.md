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

| 90-100 | Outstanding |

| 80-89 | Very Satisfactory |

| 75-79 | Satisfactory |

| below 75 | Needs Improvement |

Scores below 0 or above 100 is considered invalid.

-----

#Part 1 - Analyze the Logic

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

##Boundary Condition
What condition will you use to determine whether the score is valid?
>The score is invalid if it is less than 0 or greater than 100.

##Multiple Decision Paths
Explain how the program decides which classification should be displayed.
>The program checks the score and follows the correct condition. If it displays Outstanding for 90-100, Very Satisfactory for 80-89, Satisfactory for 75-79, and Needs Improvement for scores below 75.
