def martin_numbers(martin_number, increment):
    i = 0
    numbers = []
    print "Evaluator is %d" % martin_number
    print "Increment is %d" % increment

    while i < martin_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" %i

    print "The numbers: "

    for num in numbers:
        print num

martin_numbers(6, 2)

martin_numbers(9, 3)