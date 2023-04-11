import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series


def test_fibonacci_zero():
    actual=fibonacci(0)
    expected=0
    assert actual == expected

def test_fibonacci_one():
    actual=fibonacci(1)
    expected=1
    assert actual == expected

def test_fibonacci_two():
    actual=fibonacci(2)
    expected=1
    assert actual == expected

def test_lucas_zero():
    actual=lucas(0)
    expected=2
    assert actual == expected

def test_lucas_one():
    actual=lucas(1)
    expected=1
    assert actual == expected


def test_lucas_two():
    actual=lucas(2)
    expected=3
    assert actual == expected


def test_sum_series():
    actual=sum_series(3,2,1)
    expected=4
    assert actual == expected

def test_sum_series_one():
    actual=sum_series(2)
    expected=1
    assert actual == expected

def test_sum_series_one2():
    actual=sum_series(4,0,1)
    expected=3
    assert actual == expected


def test_sum_series_two():
    actual=sum_series(5,2,1)
    expected=11
    assert actual == expected

def test_sum_series_three():
    actual=sum_series(5,4,3)
    expected=27
    assert actual == expected