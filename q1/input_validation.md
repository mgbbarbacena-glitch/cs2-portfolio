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

```text
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
```

> Note: I used AI po to ask how to end the pseudocode if there are plenty of else and if


# Part C - Program Implementation

## Programming Language
> Python Compiler

## Source Code File
['workshop_validator.py'](workshop_validator.py)

## Final Code
```python
name = input("Enter student name: ")

if name == "":
    print("REGISTRATION NOT ACCEPTED")
    print("Student name is required.")

else:
    age = input("Enter age: ")

    if not age.isdigit():
        print("REGISTRATION NOT ACCEPTED")
        print("Age must be a number.")

    else:
        age = int(age)

        if age < 11 or age > 18:
            print("REGISTRATION NOT ACCEPTED")
            print("Age must be from 11 to 18.")

        else:
            gradelvl = int(input("Enter grade level: "))

            if gradelvl not in [7, 8, 9, 10, 11, 12]:
                print("REGISTRATION NOT ACCEPTED")
                print("Invalid grade level.")

            else:
                email = input("Enter email: ")

                if "@" not in email or "." not in email:
                    print("REGISTRATION NOT ACCEPTED")
                    print("Invalid email address.")

                else:
                    regcode = input("Enter registration code: ")

                    if len(regcode) != 6:
                        print("REGISTRATION NOT ACCEPTED")
                        print("The registration code must contain exactly 6 characters.")

                    else:
                        print("-------------------------")
                        print("REGISTRATION ACCEPTED")
                        print("-------------------------")
                        print("Student:", name)
                        print("Age:", age)
                        print("Grade Level:", gradelvl)
                        print("Email:", email)
                        print("Registration Code:", regcode)
```

## Validation Techniques Used

### Presence Validation
>I have used presence validation for the student name. This means that the program will check whether there is a value present or not in the student name. It will be done by using name == "", and if it is true, the registration will not be allowed.

### Data Type Validation
>I used the data type validation for the age. This is because the program checks if the age has only numbers by using the age.isdigit() function before converting it to an integer.

### Range Validation
>I used the range validation for the age. This is because the program checks if the age is between the range of 11 and 18 years using the age < 11 or age > 18 statement.

### Acceptable Value Validation
>I used the acceptable value validation for the grade level. This is because the program checks only the grade level values from 7 to 12 using the gradelvl not in [7, 8, 9, 10, 11, 12] statement.

### Pattern Validation
>I used the pattern validation for the email. This is because the program checks for patterns in the email by using the if '@' in email and '.' in email statement.

### Length Validation
>I used the length validation for the registration code. This is because the program checks for the length of the registration code using the len(regcode)!=6 statement.

----

# Part D- Testing

| # | Test | Input/ Condition | Validation Being Tested | Expected Output | Actual Output | Result |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | All inputs valid | Normal case | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 2 | Blank student name | Presence | REGISTRATION NOT ACCEPTED/ Student name is required. | REGISTRATION NOT ACCEPTED/ Student name is required. | PASS |
| 3 | Age = fourteen | Data type | REGISTRATION NOT ACCEPTED/ Age must be a number. | REGISTRATION NOT ACCEPTED / Age must be a number. | PASS |
| 4 | Age = 11 | Minimum boundary | Registration continues to next input | Registration continues to next input | PASS |
| 5 | Age = 18 | Maximum boundary | Registration continues to next input | Registration continues to next input | PASS |
| 6 | Age = 10 | Range | REGISTRATION NOT ACCEPTED/ Age must be from 11 to 18. | REGISTRATION NOT ACCEPTED/ Age must be from 11 to 18. | PASS |
| 7 | Grade level = 13 | Acceptable value | REGISTRATION NOT ACCEPTED/ Invalid grade level. | REGISTRATION NOT ACCEPTED/ Invalid grade level. | PASS |
| 8 | Email = studentpshs.edu.ph | Pattern | REGISTRATION NOT ACCEPTED/ Invalid email address | REGISTRATION NOT ACCEPTED/ Invalid email address. | PASS |
| 9 | Registration Code = ABC | Length | REGISTRATION NOT ACCEPTED/ Code must contain exactly 6 characters. | REGISTRATION NOT ACCEPTED/ Code must contain exactly 6 characters. | PASS |
| 10 | Registration Code = CS2026 | Valid Length | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
        
---

# Part E- Output Verification

## Verification Test 1
**Input:**
```text
Student Name: Maria
Age: 14
Grade Level: 8
Email: maria@pshs.edu.ph
Registration Code: CS2026
```
**Expected Output:**
```text
-------------------------
REGISTRATION ACCEPTED
-------------------------
Student: Maria
Age: 14
Grade Level: 8
Email: maria@pshs.edu.ph
Registration Code: CS2026
```
**Actual Output:**
```text
-------------------------
REGISTRATION ACCEPTED
-------------------------
Student: Maria
Age: 14
Grade Level: 8
Email: maria@pshs.edu.ph
Registration Code: CS2026
```
**Result:** PASS
**Explanation:**
> The output is correct because all of the inputs pass the program’s validation tests.
---

## Verification Test 2
**Input:**
```text
Student Name: Maria
Age: fourteen
```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
Age must be a number.
```
**Actual Output:**
```text
REGISTRATION NOT ACCEPTED
Age must be a number.
```
**Result:** PASS
**Explanation:**
> The output is correct because fourteen has letters so age.isdigit() returns false
---
## Verification Test 3
**Input:**
```text
Student Name: Maria
Age: 14
Grade Level: 8
Email: maria@pshs.edu.ph
Registration Code: ABC
```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
The registration code must contain exactly 6 characters.
```
**Actual Output:**
```text
REGISTRATION NOT ACCEPTED
The registration code must contain exactly 6 characters.
```
**Result:** PASS
**Explanation:**
> The output is correct because ABC only has 3 characters, not exactly 6.
---

# Reflection

### 1. Why should a program validate input before processing it?
> The program should validate the input before processing to avoid any error, and ensure the inputted data are valid and acceptable.

### 2. What is the difference between input validation and output verification?
> Input validation is the process of checking whether the input data are correct whereas output verification is the process of checking if a program produces the expected output.

### 3. Which validation technique was easiest for you to implement? Why?
> The easiest technique for me to implement is presence validation because it only checks if the input is blank or not.

### 4. Which validation technique was most challenging? Why?
> The most challenging technique is pattern validation because considering all the special characters that should be in an email is difficult.

### 5. How did testing invalid inputs help you improve your program?
> Testing the invalid inputs helped improve my program by ensuring there are no errors in the system and it satisfies all the requirements.

