# definition of function cheese_and_crackers, which takes 2 arguments
# cheese_count - number of cheeses
# boxes_of_crackers - number of boxes of crackers
# It then outputs these variables as part of a text string
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# Using function and passing just numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# setting variables and passing these variables to function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# passing mathematical operations to function as arguments
print "We can even do math, inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# passing variables we defined earlier along with mathematical operations to
# the function as arguments.
print "And we can comibine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)