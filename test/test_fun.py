import unittest
import fun

class TestFun(unittest.TestCase):
  def test_3_4(self):
    self.assert_equal(7,fun.ff(3,4)) 
