#!/usr/bin/python3

"""
function: lazy_matrix_mul
args: m_a, m_b
multiples 2 matrices using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    return np.matmul(m_a, m_b)
