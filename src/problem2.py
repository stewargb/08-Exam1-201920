"""
Exam 1, problem 2.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Grant Stewart.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_factor_sum()


def test_factor_sum():
    """ Tests the   factor_sum   function. """
    ###########################################################################
    #  TODO: 2. Implement this TEST function, as follows:
    #
    #    1. Read the  doc-string of the   factor_sum   function defined below.
    #
    #    2. Add to THIS function at least ** 5 ** tests that, taken together,
    #       would form a    ** REASONABLY GOOD test set **
    #       for testing the   factor_sum   function defined below.
    #
    #     Use the usual format:
    #       Test XXX:
    #       expected = XXX
    #       actual = XXX
    #       print()
    #       print('Expected:', expected)
    #       print('Actual:  ', actual)
    #
    #  IMPORTANT:
    #  The function that you are TESTING is PURPOSELY implemented INCORRECTLY
    #  (it just returns 0).  Do NOT implement the   factor_sum   function.
    #  Just write these TESTS of that function after reading its doc-string.
    ###########################################################################
    print()
    print('---------------------------------------------------------')
    print('Testing the   factor_sum   function:')
    print('---------------------------------------------------------')

    ###########################################################################
    # WRITE YOUR TESTS BELOW HERE:
    ###########################################################################
    # Test 1
    expected = 11
    actual = factor_sum(28)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', actual)

    # Test 2
    expected = 4
    actual = factor_sum(28)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', actual)

    # Test 3
    expected = 3
    actual = factor_sum(11) #test prime number 1 + 11 = 12 => 3
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', actual)

    # Test 4
    expected = 1
    actual = factor_sum(1) # giving it 1 it should go 1 = 1 => 1
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', actual)

    # Test 5
    expected = 9
    actual = factor_sum(10) # 1+2+5+10=18=9
    print()
    print('Test 5 expected:', expected)
    print('       actual:  ', actual)

def factor_sum(n):
    
    """
    Given a positive integer n,
    returns the sum of the digits of the sum of the distinct factors of n,
    where a FACTOR of n is an integer that divides evenly into n.

    For example, if n is 28, this function returns 11, because:
      -- the distinct factors of n are:
             1  2  4  7  14  28
      -- and the sum of those numbers is   1 + 2 + 4 + 7 + 14 + 28,
             which is 56
      -- and the sum of the digits of 56 is 11,
    so this function returns 11 when n is 28.

    As another example, if n is 25, this function returns 4, because:
    -- the distinct factors of n are:
             1  5  25
      -- and the sum of those numbers is   1 + 5 + 25,
             which is 31
      -- and the sum of the digits of 31 is 4,
    so this function returns 4 when n is 28.

       *** ASK FOR AN EXPLANATION IF YOU DO NOT UNDERSTAND THE ABOVE. ***
    """
    ###########################################################################
    #  This function is PURPOSELY implemented INCORRECTLY (it just returns 0).
    #  DO NOT IMPLEMENT  factor_sum.  Just leave it as it is (returning 0).
    ###########################################################################
    return 0
    ###########################################################################
    # DO NOT modify the above line of code!
    ###########################################################################
