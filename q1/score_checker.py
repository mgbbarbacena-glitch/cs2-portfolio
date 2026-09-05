# Ask the user to enter a student score
score = int(input("Enter student score: "))

# Check if the score is outside the valid range
if score < 0 or score > 100:
  print("Invalid Score.")

# Classify the score if it is valid
elif score >= 90:
  print("Outstanding")
elif score >= 80:
  print("Very Satisfactory")
elif score >= 75:
  print("Satisfactory")
else:
  print("Needs Improvement")
