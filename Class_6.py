# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []
i = 0
for candy in candyList:
    print("[" + str(i) +"]" + candy)

# Print out options
for i in range(len(candyList)):
    print("[" + str(i) + "] " + candyList[i])