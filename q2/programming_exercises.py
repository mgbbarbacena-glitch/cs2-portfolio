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


##Exercise 3: Skip Multiples
for number in range(1, 15):
  if number % 3 != 0:
    print(number)
###Explanation: I started with setting a range 1 to 15. For the second line, it means if number is divided by 3, then it will only look at the remainder, if it's not equal to zero, it will print the original number.


##Exercise 4: Multiplication Table Generator
def show_table(number):
  for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

numask = int(input("Enter a number:"))

show_table(numask)
###Explanation: The first line creates a reusable block of code that waits to reveive a value number. For the second line, it loops the numbers 1-10 and it assigns each one to i. For the third line, I admit to have used generative ai to understand how to do it. I understood that it formats the output so that each line shows the full equation and its answer. For the input, it asked the user for the number. For the last line, it defines and calls the function.
