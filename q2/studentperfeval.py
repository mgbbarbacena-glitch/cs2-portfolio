score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
completed_tasks = int(input("Completed tasks (0-5): "))


def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


def get_performance(average):
    if 85 <= average <= 100:
        return "Mastery"
    elif 70 <= average < 85:
        return "Developing"
    else:
        return "Needs Review"


def is_eligible(average, completed_tasks):
    return average >= 85 and completed_tasks >= 3


avg = calculate_average(score1, score2, score3)
performance = get_performance(avg)
eligible = is_eligible(avg, completed_tasks)

print("Average:", round(avg, 2))
print("Performance:", performance)
print("Eligible for Challenge:", eligible)


# DOCUMENTATION QUESTIONS

# 1. The "calculate_average" gives back a number, "get_performance" gives back a category as text, and "is_eligible" gives back True or False.

# 2. The average is calculated by "calculate_average" and returned to the program. Then, it's saved in avg and used in get_performance.

# 3. If the student has a high average, they still can't join the challenge if they have completed less than 3 tasks. They need to meet both requirements to be eligible.

# 4. return lets the program keep and reuse a function's result, while print only displays the result on the screen.
