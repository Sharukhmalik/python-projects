from slice import *

A = [1,2,3,4,5]
K= 2



def test_slice():
    assert solution(A,K)[1] == [1, 2, 3]
