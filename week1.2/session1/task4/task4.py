# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# the output nwill be{'Tomato'} because intrsection () returns the elelments that are present in both sets.
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#The union() method combines the whole uniqe elements in both sets, however although the total number of the items are 6 "tomato" appears in both sets and is only included once.
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("banana")
# Remove an item from vegetables
vegetables.discard("leek")
# Find and display symmetric difference of the two sets
difference = fruit.symmetric_difference(vegetables)
print(difference)
