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

(Note: I also used AI here po for the character limit only, my prompt was "how to make a limit in characters in python like for example the character limit in the input is 6")
