def martin_numbers(martin_number, increment):
    numbers = []
    print "Evaluator is %d" % martin_number
    print "Increment is %d" % increment

    for i in range(0, martin_number, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" %i

    print "The numbers: "

    for num in numbers:
        print num

martin_numbers(6, 2)

martin_numbers(9, 3)