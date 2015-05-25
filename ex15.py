# import argv from sys package
from sys import argv

# telling python that the arguments are the script name and a file name
script, filename = argv

# open the file name supplied and assigns to txt
txt = open(filename)

# print the name of the file
print "Here's your file %r:" % filename
# read the contents of txt and print it out
print txt.read()

print "Now appending a new line to the file"
new_line = raw_input("What do you want to say?>>>")
txt.close()

txt2 = file(filename, write)
txt2.write(new_line)
txt2.close()

txt_new = open(filename)
print txt_new.read()