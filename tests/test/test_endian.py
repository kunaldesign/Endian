import unittest
from  src.endian import big_to_little_str

class Test(unittest.TestCase):
    def test_endian(self):
        self.assertEqual(big_to_little_str('112122'), '222111')

unittest.main()