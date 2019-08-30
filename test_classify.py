#!/usr/bin/python3

import pytest

# The first set of test cases test the is_xyz functions

def test_invalid_zero():
    """
    Test that an null size triangle returns 'invalid'
    """
    assert 1 == 0

def test_inf():
    """
    Test that a invlaid triangle with an infinite length returns 'invalid'
    """
    assert 1 == 0

def test_nan():
    """
    Test that a invlaid triangle with a not a number length returns 'invalid'
    """
    assert 1 == 0

def test_invalid_scalene():
    """
    Test that an invlaid triangle with three different lengths returns 'invalid'
    """
    assert 1 == 0

def test_invalid_isosceles():
    """
    Test that an invlaid triangle with two equal sides returns 'invalid'
    """
    assert 1 == 0

def test_equalateral():
    """
    Test that a triangle with three equal sides returns 'equalateral'
    Note: equalateral triangles are also isosceles
    """
    assert 1 == 0

def test_isosceles():
    """
    Test that a triangle with two equal sides returns 'isosceles'
    """
    assert 1 == 0

def test_scalene():
    """
    Test that a triangle with three differnt sides returns 'scalene'
    """
    assert 1 == 0

def test_right():
    """
    Test that a tirangle with a**2 + b**2 = c**2 triangle returns 'right'
    Note: right triangles are also scalene.
    """
    assert 1 == 0
