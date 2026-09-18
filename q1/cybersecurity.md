# Fundamentals of Cybersecurity and Data Privacy

**Activity:** PSHS Secure Club Registration System

**Name:** Ma. Gia B. Barbacena

**Section:** Dahlia

**Quarter:** 1

---

## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.

---

# Part A - Cybersecurity Threat Analysis
## Assigned Case
**Case Number:** 1
**Case Title:** Fake Login Alert
> A Fake Login Alert is a message falsely claiming that the student's account will be disabled and the student must log in by clicking on a link and entering the username and password.

---

### 1. What cybersecurity threat is shown?
> The cyber security threat is phishing. It tricks the student into revealing their username and password.
### 2. What warning signs make the situation suspicious?
> It threatens the student that their account will be disabled if they don't click on a link and enter their password.
### 3. What may be affected?
- Data
- Account
- Application
- Device
- Financial information
> It says not to collect passwords, OTPs, home address, or banking information.
### 4. What information could be exposed or misused?
> Their username and password can be obtained and used to endanger the student's account.
### 5. What should the user do to reduce the risk?
> The user shouldn't click on the link and enter their password. They should confirm the request through an official school website or report it if it's suspicious.

---

# Part B - Data Privacy and Secure Data Capture
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | To identify the student. |
| Section | Collect | To identify the student's class. |
| Club Choice | Collect | To know which club the student chose. |
| School Email | Collect |  To communicate for school-related stuff. |
| Attendance Status | Collect | To record attendance. |
| Password | Do not collect| Not needed for club registration |
| OTP | Do not collect| Not needed for this activity. |
| Home Address | Do not collect | Not needed because its unnecessary personal information. |
| Parent Bank Account | Do not collect | Not needed because its unnecessary financial information. |

---

## Privacy Question
Why is it safer to collect only information that the program actually needs?
> It's safer because it collects less personal information which can then lead to having less information that could be exposed.

----

# Part C - Security-Focused Validation Rules
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message | 
| --- | --- | --- | --- | --- | --- |
| Student Name | Student's name | Missing identification | Blank | Must not be blank | Student name is required. |
| Section | Teacher-approved section | Incorrect class information | Gaming | Must match an allowed section | Invalid section. |
| Club Choice | Robotics, Science, Mathematics, Programming | Invalid club selection | Gaming | Must be one of the allowed clubs | Please enter a valid club. |
| School Email | School email containing @ and . | Incorrect email format | studentpshs.edu.ph | Must contain both @ and . | Invalid school email. |
| Attendance Status | Present, Absent, Late | Incorrect attendance record | Maybe | Must be "Present, Absent, or Late" | Invalid attendance status. |

---

## Secure Data Capture Questions
### 1. What should your program accept?
> The program should take only the necessary student information that must pass the validation tests.
### 2. What should your program reject?
> The program should reject blank names, invalid sections, invalid club choices, invalid e-mail formats, and invalid attendance statuses.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> Validation rules prevent the entry of wrong information and ensure that only correct data is stored.

---

# Part D - Secure Program Implementation

## Program

Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email
- Attendance Status

It should **not request passwords, OTPs, banking information, or unnecessary personal information**

---
## Source Code File
[`secure_registration.py`](secure_registration.py)

---
## Final Code
```python
ame = input("Enter student name: ")

if name == "":
    print("REGISTRATION NOT ACCEPTED")
    print("Student name is required.")

else:
    section = input("Enter section: ")

    if section != "Dahlia", "dahlia":
        print("REGISTRATION NOT ACCEPTED")
        print("Invalid section.")

    else:
        club = input("Enter club choice: ")

        if club not in ["Robotics", "Science", "Mathematics", "Programming", "robotics", "science", "mathematics", "programming"]:
            print("REGISTRATION NOT ACCEPTED")
            print("Please choose a valid club.")

        else:
            email = input("Enter school email: ")

            if "@" not in email or "." not in email:
                print("REGISTRATION NOT ACCEPTED")
                print("Invalid school email.")

            else:
                attendance = input("Enter attendance status: ")

                if attendance not in ["Present", "Absent", "Late", "present", "absent", "late"]:
                    print("REGISTRATION NOT ACCEPTED")
                    print("Invalid attendance status.")

                else:
                    print("--------------------------------")
                    print("REGISTRATION ACCEPTED")
                    print("--------------------------------")
                    print("Student:", name)
                    print("Section:", section)
                    print("Club:", club)
                    print("Email:", email)
                    print("Attendance:", attendance)
                  
```
---

## Security Practices Applied
### Required Input
> A blank input is an invalid input and it will display the error message and validation rule.
### Allowed Values
> Explain which fields accept only predefined values.
### Format Check
> The email must contain @ and . to check the email is in the basic valid format.
### Error Messages
> Clear  error messages help users in quickly fixing what has gone wrong and how to fix it.
### Data Minimization
> I didn't collect unnecessary information like passwords or personal details to protect user privacy.

---

# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 2 | Blank student name | REGISTRATION NOT ACCEPTED, Student name is required. | REGISTRATION NOT ACCEPTED, Student name is required. | PASS |
| 3 | Invalid section | REGISTRATION NOT ACCEPTED, Invalid section. | REGISTRATION NOT ACCEPTED, Invalid section. | PASS |
| 4 | Invalid club choice | REGISTRATION NOT ACCEPTED, Please choose a valid club. | REGISTRATION NOT ACCEPTED, Please choose a valid club. | PASS |
| 5 | Email missing `@` | REGISTRATION NOT ACCEPTED, Invalid school email. | REGISTRATION NOT ACCEPTED, Invalid school email. | PASS |
| 6 | Email missing `.` | REGISTRATION NOT ACCEPTED, Invalid school email. | REGISTRATION NOT ACCEPTED, Invalid school email. | PASS |
| 7 | Invalid attendance status | REGISTRATION NOT ACCEPTED, Invalid attendance status. | REGISTRATION NOT ACCEPTED, Invalid attendance status. | PASS |
| 8 | Different valid inputs | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |

---

# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> One type of cyber threat is known as phishing where users are lured into providing private information.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Users can avoid clicking on misleading links by checking who sent them, and verifying information with an official source.
### 3. How can validation rules improve the security of user input?
> Validation rules ensure that invalid or unexpected information is not entered into the program.A
### 4. Why should a program avoid collecting unnecessary personal information?
> A program should avoid unnecessary information because less collected data has less information that can be exposed or misused.
### 5. How did SG7's input validation concepts become security practices in SG8?
> The input validation concepts described in SG7 are implemented as security practices by the careful checking of the user input and only accepting the data which follows the rules.

