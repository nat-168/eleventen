# a unit test script verifying that a1.py is working correctly.

"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Katherine Son ks2395, River Strumwasser rns88
Date:   9/14/23
"""

import introcs
import a1

def testA():
    """
    Test procedure for Part A

    Tests functions before_space and after_space. Prints all in-test statements
    and all tests passed statement if ran correctly. Tests follow
    specifications given in a1 function docstrings.
    """

    #before_space and after_space alternate test cases, except for
    #after_space's two space test, as before_space doesn't need an equivalent
    #test for representativeness

    #basic test before_space
    print('Testing function before_space')
    input = 'A B'
    result = a1.before_space(input)
    introcs.assert_equals('A',result)

    #basic test after_space
    print('Testing function after_space')
    input = 'A B'
    result = a1.after_space(input)
    introcs.assert_equals('B',result)

    #testing before_space with multiple spaces
    print('Testing function before_space')
    input = 'A  B'
    result = a1.before_space(input)
    introcs.assert_equals('A',result)

    #testing after_space with multiple spaces
    print('Testing function after_space')
    input = 'A  B'
    result = a1.after_space(input)
    introcs.assert_equals(' B',result)

    #testing before_space with a space at the start
    print('Testing function before_space')
    input = ' AB'
    result = a1.before_space(input)
    introcs.assert_equals('',result)

    #testing after_space with the only space at the end
    print('Testing function after_space')
    input = 'AB '
    result = a1.after_space(input)
    introcs.assert_equals('',result)

    #testing before_space when the entire string is one space
    print('Testing function before_space')
    input = ' '
    result = a1.before_space(input)
    introcs.assert_equals('',result)

    #testing after_space when the entire string is one space
    print('Testing function after_space')
    input = ' '
    result = a1.after_space(input)
    introcs.assert_equals('',result)

    #testing after_space when the entire string is two spaces
    print('Testing function after_space')
    input = '  '
    result = a1.after_space(input)
    introcs.assert_equals(' ',result)

    #testing before_space with multiple non-consecutive spaces, & at end
    print('Testing function before_space')
    input = 'x x x '
    result = a1.before_space(input)
    introcs.assert_equals('x',result)

    #testing after_space with multiple non-consecutive spaces, & at start
    print('Testing function after_space')
    input = ' x x x'
    result = a1.after_space(input)
    introcs.assert_equals('x x x',result)

    #testing before_space with a backslash
    print('Testing function before_space')
    input = 'xxx\ '
    result = a1.before_space(input)
    introcs.assert_equals('xxx\\',result)

    #testing after_space with a backslash
    print('Testing function after_space')
    input = '\ xxx'
    result = a1.after_space(input)
    introcs.assert_equals('xxx',result)


def testB():
    """
    Test procedure for Part B

    Tests functions first_inside_quotes, get_lhs, get_rhs, and has_error. Prints
    all in-test statements and all tests passed statement if ran correctly.
    Tests follow specifications given in a1 function docstrings
    """

    #basic test first_inside_quotes
    print('Testing function first_inside_quotes')
    input = 'Hi "Mom"!'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals('Mom',result)

    #testing first_inside_quotes with more than 2 quotes inside string
    print('Testing function first_inside_quotes')
    input = 'Hi "Mom"!"'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals('Mom',result)

    #testing first_inside_quotes with an empty substring
    print('Testing function first_inside_quotes')
    input = 'Hi ""!'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals('',result)

    #testing first_inside_quotes with a backslash in the substring
    print('Testing function first_inside_quotes')
    input = 'Hi "Mom\'"!'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals("Mom'",result)

    #testing first_inside_quotes with a sum of strings
    print('Testing function first_inside_quotes')
    input = 'Hi'+'"Mom"'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals('Mom',result)

    #For get_lhs and get_rhs, first_inside_quotes testing covers capabilities,
    #so the main consideration is the possible values for the JSON, as a
    #response to a currency query with a rigid format.

    #basic test get_lhs
    print('Testing function get_lhs')
    input = ('{ "ok":true, "lhs":"2.5 United States Dollars",'
    +' "rhs":"64.375 Cuban Pesos", "err":"" }')
    result = a1.get_lhs(input)
    introcs.assert_equals('2.5 United States Dollars', result)

    #testing get_lhs with 0 value for currency
    print('Testing function get_lhs')
    input = ('{ "ok":true, "lhs":"0 United States Dollars",'
    +' "rhs":"0 Cuban Pesos", "err":"" }')
    result = a1.get_lhs(input)
    introcs.assert_equals('0 United States Dollars', result)

    #testing get_lhs with JSON with error
    print('Testing function get_lhs')
    input = ('{ "ok":false, "lhs":"",'
    +' "rhs":"", "err":"Source currency code is invalid." }')
    result = a1.get_lhs(input)
    introcs.assert_equals('', result)

    #basic test get_rhs
    print('Testing function get_rhs')
    input = ('{ "ok":true, "lhs":"2.5 United States Dollars",'
    +' "rhs":"64.375 Cuban Pesos", "err":"" }')
    result = a1.get_rhs(input)
    introcs.assert_equals('64.375 Cuban Pesos', result)

    #testing get_lhs with 0 value for currency
    print('Testing function get_rhs')
    input = ('{ "ok":true, "lhs":"0 United States Dollars",'
    +' "rhs":"0 Cuban Pesos", "err":"" }')
    result = a1.get_rhs(input)
    introcs.assert_equals('0 Cuban Pesos', result)

    #testing get_lhs with JSON with error
    print('Testing function get_rhs')
    input = ('{ "ok":false, "lhs":"",'
    +' "rhs":"", "err":"Source currency code is invalid." }')
    result = a1.get_rhs(input)
    introcs.assert_equals('', result)

    #Again, because has_error can only deal with responses to currency queries
    #in the precondition, it only needs a true and a false test case.

    #test has_error for a JSON with an error
    print('Testing function has_error')
    input = ('{ "ok":false, "lhs":"",'
    +' "rhs":"", "err":"Source currency code is invalid." }')
    result = a1.has_error(input)
    introcs.assert_equals(True,result)

    #test has_error for a JSON without an error
    print('Testing function has_error')
    input = ('{ "ok":true, "lhs":"2 Namibian Dollars",'
    +' "rhs":"2 Lesotho Maloti", "err":"" }')
    result = a1.has_error(input)
    introcs.assert_equals(False,result)


def testC():
    """
    Test procedure for Part C

    Tests function currency_response. Prints all in-test statements and all
    tests passed statement if ran correctly. Tests follow specifications
    given in a1 function docstrings.
    """

    #basic test currency_response
    print('Testing function currency_response')
    src = 'USD'
    dst = 'CUP'
    amt = 2.5
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":true, "lhs":"2.5 United '
    +'States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }'))

    #empty src test for currency_response
    print('Testing src in function currency_response')
    src = ''
    dst = 'CUP'
    amt = 2.5
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":false, "lhs":"",'
    +' "rhs":"", "err":"Source currency code is invalid." }'))

    #invalid src test for currency_response
    print('Testing src in function currency_response')
    src = 'usd'
    dst = 'CUP'
    amt = 2.5
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":false, "lhs":"",'
    +' "rhs":"", "err":"Source currency code is invalid." }'))

    #src with operation test for currency_response
    print('Testing src in function currency_response')
    src = 'US'+'D'
    dst = 'CUP'
    amt = 2.5
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":true, "lhs":"2.5 United '
    +'States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }'))

    #empty dst test for currency_response
    print('Testing dst in function currency_response')
    src = 'USD'
    dst = ''
    amt = 2.5
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":false, "lhs":"",'
    +' "rhs":"", "err":"Exchange currency code is invalid." }'))

    #invalid dst test for currency_response
    print('Testing dst in function currency_response')
    src = 'USD'
    dst = 'cup'
    amt = 2.5
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":false, "lhs":"",'
    +' "rhs":"", "err":"Exchange currency code is invalid." }'))

    #dst with operation test currency_response
    print('Testing dst in function currency_response')
    src = 'USD'
    dst = 'CU'+'P'
    amt = 2.5
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":true, "lhs":"2.5 United '
    +'States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }'))

    #empty amt test for currency_response
    print('Testing amt in function currency_response')
    src = 'USD'
    dst = 'CUP'
    amt = float()
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":true, "lhs":"0 United '
    +'States Dollars", "rhs":"0 Cuban Pesos", "err":"" }'))

    #amt with operation test for currency_response
    print('Testing amt in function currency_response')
    src = 'USD'
    dst = 'CUP'
    amt = float('2.5')
    result = a1.currency_response(src, dst, amt)
    introcs.assert_equals(result, ('{ "ok":true, "lhs":"2.5 United '
    +'States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }'))


def testD():
    """
    Test procedure for Part D

    Tests functions is_currency and exchange. Prints all in-test statements and all
    tests passed statement if ran correctly. Tests follow specifications given
    in a1 function docstrings.
    """

    #basic test for is_currency
    print('Testing function is_currency')
    input = 'USD'
    result = a1.is_currency(input)
    introcs.assert_equals(True, result)

    #invalid test for is_currency
    print('Testing function is_currency')
    input = ''
    result = a1.is_currency(input)
    introcs.assert_equals(False, result)

    #valid test with operation for is_currency
    print('Testing function is_currency')
    input = 'US'+'D'
    result = a1.is_currency(input)
    introcs.assert_equals(True, result)

    #basic test for exchange
    print('Testing function exchange')
    src = 'USD'
    dst = 'CUP'
    amt = 2.5
    result = a1.exchange(src, dst, amt)
    introcs.assert_floats_equal(result, 64.375)

    #basic test with new inputs for exchange
    print('Testing function exchange')
    src = 'EUR'
    dst = 'CAD'
    amt = 1
    result = a1.exchange(src, dst, amt)
    introcs.assert_floats_equal(result, 1.3043417820311)

    #empty amt test for exchange
    print('Testing function exchange')
    src = 'USD'
    dst = 'CUP'
    amt = float()
    result = a1.exchange(src, dst, amt)
    introcs.assert_floats_equal(result, 0.0)

    #operation for amt in exchange
    print('Testing function exchange')
    src = 'USD'
    dst = 'CUP'
    amt = 1.5+1
    result = a1.exchange(src, dst, amt)
    introcs.assert_floats_equal(result, 64.375)

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
