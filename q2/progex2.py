#Programming Exercises 2

##Exercise 1: My School Bag
school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

print(school_items[0])
print(school_items[1])
print(school_items[2])
print(school_items[3])
print(school_items[4])

print("First item: ", school_items[0])
print("Last item: ", school_items[4])
###Explanation: First I created a list named school_items that has five school supplies. Next, I used print() statements with index numbers to display each item in the list individually. The index starts at 0 so thats why school_items[0] displays the first item and [4] displays the last item.

##Exerccise 2: Travel Destination Manager
dest = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

print("All Destinations:")
for destination in dest:
    print(destination)

print("Destinations from index 1 to 3:")
print(dest[1:4])


search = input("Enter a destination to search for (Destination should start with a CAPITAL LETTER): ")

if search in dest:
    print("The destination exists in the list.")
else:
    print("The destination does not exist in the list.")



dest[2] = "Iloilo"
###Explanation: Firest, I displayed all the destinations using a for loop. Then, I used slicing to display the destinations in index 1-3. Next, I asked the user to input their destination, the code then checks if its in the list or not. The dest[2] replaces index 2 with Iloilo. Finally, it displays and updates the list. 

print("Updated Destinations:")
print(dest)
