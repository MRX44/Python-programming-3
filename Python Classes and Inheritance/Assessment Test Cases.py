#The function mySum is supposed to return the sum of a list of numbers
#(and 0 if that list is empty), but it has one or more errors in it.
#Use this space to write test cases to determine what errors there are.
#You will be using this information to answer the next set of multiple
#choice questions.

import test


def mySum(list):
    if len(list) > 0:
        res = 0
        for i in list:
            res += i
        return res
    else:
        return 0





#test-4-1: Which of the following cases fail for the mySum function?
# [A. an empty list , C. a list with more than one item]





#test-4-2: Are there any other cases, that we can determine based on the
#current structure of the function, that also fail for the mySum function?
# [B. No]




#test-4-3: Which of the following cases fail for the Student class?
# [C. the attributes/instance variables are not correctly assigned in the constructor
#  D. the method study does not increase self.knowledg]




#test-4-4: Are there any other cases, that we can determine based on the current structure of the class, that also fail for the Student class?
#[A. Yes]



