import unittest
from ddt import ddt,data,unpack

@ddt
class MyTesting(unittest.TestCase):


    @data(["java"], ["python"], ["php"])
    @unpack
    def test_serach(self,value):
        print(value)


if __name__ == '__main__':
    unittest.main()