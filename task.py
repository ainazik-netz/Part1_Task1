def is_even(num):
    if num %2 == 0:
        return True
    else:
        return False
def test_is_even():
     assert is_even(2) == True
     assert is_even(101) == False
     assert is_even(10) == True
     assert is_even(7) == False
     print('Your code is correct!')
test_is_even()