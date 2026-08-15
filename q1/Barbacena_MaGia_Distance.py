import math

x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))

distance = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

print("The distance between the two points is:", round(distance, 2))

# Reflection:
# I learned that using a library is more practical because it makes the calculations easier.
# The sqrt and pow functions helped me calculate the distance more easily.
