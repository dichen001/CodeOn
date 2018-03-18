# ( ) = True
# ( = False
# ""  = True

# checking when an open ( is added, then looking for a ), otherwise, count the ( till several ) are added
# then see if they equal each other


def insVals(vals):
    # Time : O(n)
    # Space : O(1)

    print "Test Case: ", vals

    openCtr = 0
    closeCtr = 0

    # Corner cases
    if (len(vals) == 0):
        return True
    if (len(vals) == 1):
        return False
    if vals[0] == ")":
        return False
    if vals[-1] == "(":
        return False


    for c_val in vals:

        if c_val == "(":
            openCtr+= 1

        if c_val == ")":
            if (openCtr == 1):
                if (closeCtr == 1):
                    openCtr = 0
                    closeCtr = 0
                if (closeCtr > 1):
                    return False
            if (openCtr > 1):
                openCtr -= 1
                closeCtr = 0

        if c_val == ")" and openCtr == 0:
            return False

    return True


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