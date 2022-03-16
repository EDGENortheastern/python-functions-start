import pytest

from addition import add_nums
from subtraction import subtract_nums
from perimeter import find_perimeter
from area import area_rectangle

from random import randint

def test_smoke():
    assert 1+1==2

def test_add_nums():
    assert add_nums(3,5) == 8

def test_subtract_nums():
    assert subtract_nums(10,5) == 5

def test_area_rectangle():
    assert area_rectangle(10,4) == 40

def test_find_perimeter():
    assert find_perimeter(10,4) == 28