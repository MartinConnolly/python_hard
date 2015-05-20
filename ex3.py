# This prints out that I'm counting chickens
print "I will now count my chickens:"

# This prints Hens and counts 25 + 30 / 6 i.e. 30
print "Hens", 25 + 30 / 6
# This prints Roosters and counts 100 - 25 * 3 % 4
# the % operator returns the remainder of a division
# so this equates to 
# 1. 25 * 3 = 75
# 2. (25 * 3) % 4 = 75 % 4 = 3
# 3. 100 - ((25 * 3) % 3) = 100 - 3 = 97
print "Roosters", 100 - 25 * 3 % 4

# printing that I'm counting the eggs
print "Now I will count the eggs:"

# Evaluated as follows;
# (3 + 2 + 1) - 5 + (4 % 2)) - ((1 / 4) + 6)
# (3 + 2 + 1) - (5 + (0)) - ((0) + 6)
# Note above that 1 /4 = 0
# (6) - (5) + 0  - 0 + (6)  = 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# asking if it's true
print "Is it tue that 3 + 2 < 5 - 7?"

# this evaluates the test and returns result - FALSE
print 3 + 2 < 5 - 7

# breaking it down print the sum, then show result
print "What is 3 + 2?", 3 + 2
# breaking it down print the subtraction, then show result
print "What is 5 - 7?", 5 - 7

# Explaining that's why it's false
print "Oh, that's why it's False."

#Some more
print "How about some more."

# Is it greater, then check result
print "Is it greater?", 5 > -2
# Is it greater or equal, then check result
print "Is it greater or equal?", 5 >= -2
# Is it less or equal, then check result
print "Is it less or equal?", 5 <= -2