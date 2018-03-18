# ( ) = True
# ( = False
# ""  = True

# checking when an open ( is added, then looking for a ), otherwise, count the ( till several ) are added
# then see if they equal each other


def insVals(vals):
    # Time : O(n)
    # Space : O(n)

    s = []
    # Current Value
    for c_val in vals:
        if (c_val == "("):
            s.append(c_val)
        if (c_val == ")"):
            # Target Value
            if (len(s) == 0):
                return False
            else:
                s.pop()
    return s == []



test1=insVals("()")
test2 = insVals("")
test3 = insVals("()()")
test4 = insVals("())(")
test5 = insVals("((")
test6 = insVals("()()(())")
tests = [test1, test2, test3, test4, test5, test6]
testsAns = [True, True, True, False, False, True]

correctOnAll = True
for index, test in enumerate(tests):
    print "Testing test: ", (index + 1)
    if (test == testsAns[index]):
        print "**** Finished ****"
    else:
        correctOnAll = False
        print "Wrong Answer"
if (correctOnAll):
    print "********** Completed All **********"