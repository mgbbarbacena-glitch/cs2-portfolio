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
| Student Name | | | | | |
| Age | | | | | |
| Grade Level | | | | | |
| Email Address | | | | | |
| Registration Code | | | | | |

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
>The registration code had a limit of 6 characters.

# Part B - Program Design

## Pseudocode


START
    INPUT name
    INPUT age
    INPUT grade
    INPUT email
    INPUT reg

    IF name == "" THEN
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Student name is required."
        
    ELSE IF age.isdigit() == FALSE THEN
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Age must be a number."
        
    ELSE IF age == "11" OR age == "12" OR age == "13" OR age == "14" OR age == "15" OR age == "16" OR age == "17" OR age == "18" THEN
        
        IF grade == "7" OR grade == "8" OR grade == "9" OR grade == "10" OR grade == "11" OR grade == "12" THEN
            
            IF "@" IN email THEN
                
                IF LENGTH(reg_code) == 6 THEN
                    PRINT "------------------------------"
                    PRINT "REGISTRATION ACCEPTED"
                    PRINT "------------------------------"
                    PRINT "Student:", name
                    PRINT "Age:", age
                    PRINT "Grade Level:", grade
                    PRINT "Email:", email
                    PRINT "Registration Code:", reg_code
                    
                ELSE
                    PRINT "REGISTRATION NOT ACCEPTED"
                    PRINT "The registration code must contain exactly 6 characters."
                ENDIF
                
            ELSE
                PRINT "REGISTRATION NOT ACCEPTED"
                PRINT "Email must contain '@'."
            ENDIF
            
        ELSE
            PRINT "REGISTRATION NOT ACCEPTED"
            PRINT "Invalid grade level."
        ENDIF
        
    ELSE
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Age must be from 11 to 18."
    ENDIF
END
