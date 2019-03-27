#!/usr/bin/env python
# -*- coding: utf-8 -*-


from parameterized import parameterized, param
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal
import unittest
import math
import json


class TestParameterized(unittest.TestCase):

    @parameterized.expand([
        (2, 2, 4),
        (2, 3, 8),
        (1, 9, 1),
        (0, 9, 0),
    ])
    def test_pow(self,base, exponent, expected):
        assert_equal(math.pow(base, exponent), expected)

    # 方法的参数化
    # A list of tuples
    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0),
        ("large fraction", 1.6, 1),
    ])
    def test_floor(self, name, input, expected):
        print(name)
        assert_equal(math.floor(input), expected)

    # An iterable of params
    @parameterized.expand(param.explicit(*json.loads(line))
        for line in open("data.json")
    )
    def test_from_json_file(self,line):
        print(line)



# 类的参数化
@parameterized_class([
   { "a": 3, "expected": 2 },
   { "b": 5, "expected": -4 },
])
class TestMathClassDict(unittest.TestCase):
   a = 1
   b = 1

   def test_subtract(self):
      print("test_subtract")
      assert_equal(self.a - self.b, self.expected)


if __name__ == '__main__':
    unittest.main()