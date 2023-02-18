import pytest



#this modue contains basic unit tests for math operators
#a most basic test function

def test_one_plus_one():
    assert 1 + 1 == 2

#-----------
 # A test funtion to show assertion introspection
 #----------

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c  # this test case should fail  a+b not equal c if c is 0



#---------
# A test funtion that verifies an exception
#----------

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0  
    assert 'division by zero' in str(e.value)

# -------
# Parametized Test funtions 
#---------
# Multipplication test ideas
# two positive integers
# identity: multiplying any number by 1
# zero: multipling any number by 0
# positive by negative
# negative by positive
# multiply floats 
#-------

def test_multiply_two_positive_ints():
    assert 2 * 3 == 6 

def test_multiply_identitty():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0

#DRY principle : Don`t repeat yourself 

products = [
    (2, 3 ,6),       #positive integers
    (1, 99, 99),     #identity
    (0, 99, 0),      #zero
    (3, -4, -12),    #positive by negative
    (-5, -5, 25),    #negative by negative
    (2.5, 6.7, 16,75)#floats
]

@pytest.mark.parametrize('a, b, product', products)
def tesst_multiplication(a, b,product):
    assert a * b == product


