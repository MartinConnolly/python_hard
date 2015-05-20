from sys import argv

script, one, two, three, four = argv

print "The script is called:", script
print "Your first variable is:", one
print "Your second variable is:", two
print "Your third variable is:", three
print "Your fourth variable is:", four

five = raw_input("And finally input the fifth variable?>")
print "Your fifth variable is:", five