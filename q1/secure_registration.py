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
                  
