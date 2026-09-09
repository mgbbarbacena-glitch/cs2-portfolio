# Input Validation and Output Verification

**Activity:** PSHS Workshop Registration Validator

**Name:** Ma. Gia B. Barbacena

**Section:** Dahlia

**Quarter:** 1

-------------

## Activity Overview

In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

--------

# Part A - Validation Requirements

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
| --- | --- | --- | --- | --- | --- |
| Student Name | Text | Presence | Blank | Name must not be blank | Student name is required. |
| Age | Integer from 11-18 | Data Type and Range | "fourteen", "25" | Must be an integer and between 11 and 18 | Age must be a number./ Age must be from 11 to 18.|
| Grade Level | 7, 8, 9, 10, 11, 12 | Acceptable Value | 13 | Must be one of the accepted grade levels | Invalid grade level. |
| Email Address | Text containing @ and . | Pattern |studentpshs.edu.ph | Must contain both @ and .| Invalid email address. |
| Registration Code | Exactly 6 characters | Length | ABC | Must contain exactly 6 characters | The registration code must contain exactly 6 characters. |

----

## Validation Questions
### 1. Why should the student name not be blank?
>To make sure that each submission has a valid identifier and isn't left blank or anonymous.

### 2. Why should age be checked for both data type and range?
>To ensure that the input is a correct data type like a number and is within the correct range for the participants of the workshop from 11 to 18 years old.

### 3. Why should grade level only accept specific values?
>To limit entries to only those corresponding to grade levels 7-12 and to ensure that invalid entries or typos can be prevented.

### 4. What format requirements did you use for the email address?
>The email address should contain the '@' symbol.

### 5. What length requirement did you use for the registration code?
>The registration code has a limit of 6 characters.

# Part B - Program Design

## Pseudocode

START

INPUT student name

IF student name is blank THEN
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY "Student name is required."
ELSE
    INPUT age

    IF age is not a number THEN
        DISPLAY "REGISTRATION NOT ACCEPTED"
        DISPLAY "Age must be a number."
    ELSE
        CONVERT age to integer

        IF age is less than 11 OR age is greater than 18 THEN
            DISPLAY "REGISTRATION NOT ACCEPTED"
            DISPLAY "Age must be from 11 to 18."
        ELSE
            INPUT grade level

            IF grade level is not 7, 8, 9, 10, 11, or 12 THEN
                DISPLAY "REGISTRATION NOT ACCEPTED"
                DISPLAY "Invalid email address."
            ELSE
                INPUT registration code

                IF registration code does not have exactly 6 characters THEN
                    DISPLAY "REGISTRATION NOT ACCEPTED" 
                    DISPLAY "The registration code must contain exactly 6 characters
                ELSE
                    DISPLAY "REGISTRATION ACCEPTED"
                    DISPLAY student name
                    DISPLAY age
                    DISPLAY grade level
                    DISPLAY email
                    DISPLAY registration code
                END IF
            END IF
        END IF
    END IF
    
    END

>Note: I used AI po to ask how to end the pseudocode if there are plenty of else and if

# Part C - Python Code Link:
[Workshop Validator](workshop_validator.py)

            
        



