#Problem 1
supplies = ["Glue", "Scissors", "Paper"]

print("Science Club Supply Organizer")
print("Original Supplies: ")
print(supplies)

supplies.append("Tape")
print("After Adding Tape:")
print(supplies)

supplies.insert(1, "Markers")
print("After Inserting Markers")
print(supplies)

supplies.remove("Glue")
print("After Removing Glue")
print(supplies)

print("Total Supplies:", len(supplies))

#Problem 2
attendance = ["Present", "Absent", "Present", "Present", "Absent", "Present"]


print("Classroom Attendance Counter")

studentnum = 1

for record in attendance:
  print("Student", studentnum, ":", record)
  studentnum = studentnum + 1

present = attendance.count("Present")
absent = attendance.count("Absent")

total = len(attendance)

print()
print("Attendance Summary")
print("Total Students: ", total)
print("Present: ", present)
print("Absent: ", absent)
