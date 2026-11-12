#Programming Exercises

##Exercise 1: Count Even Numbers
for number in range(2, 20, 2):
  print(number)
###Explanation: It asked to make me display even numbers in the range of 2-20 using the for loop. If I only put (2, 20), it would display numbers from 2-19, since it's asking for even numbers only, I added a step of 2 to skip two numbers.

##Exercise 2: The Countdown Timer
number = 10

while number >= 1:
  print(number)
  number -=1

print("Time is up!")
###Explanation: I used the code displayed in Sir Roffe's previous lesson as a base and experimented it. I made the number 10 because it's the starting number of the output. Then, for the "while number >= 1:", this means that if the number is smaller or equal than 1, it's gonna keep printing numbers from 10-1. For the "number -=1", I made it negative because the numbers are decreaasing, then I printed the Time is up.
