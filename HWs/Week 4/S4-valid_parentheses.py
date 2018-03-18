"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Example:

Input1: "(){}[]", output1: True
Input2: "",       output2: True
Input3: "{[}{}(", output3: False
"""

def valid_parentheses(s):
    """
    :type s: str
    :rtype: bool

    Hint: Stack. Think about the question we discussed in the class.
          This has 2 more types need to take care.
    """





"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ("{}[]()", True)
        test1 = ("{}{{]][]", False)
        test2 = ("", True)
        test3 = ("(({}", False)
        test4 = ("))}}]]", False)
        tests = [test0, test1, test2, test3, test4]
        for i, test in enumerate(tests):
                print("------------- Test " +str(i) + " -------------")
                print("-Test Input:")
                print(test[0])
                print("-Expected Output:")
                print(test[1])
                print("-Your Output:")
                your_ans = valid_parentheses(test[0])
                print(your_ans)
                assert your_ans == test[1], "Wrong return. Please try again."
        print('\n**** Congratulations! You have passed all the tests! ****')

