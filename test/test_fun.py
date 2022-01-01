import unittest
import fun

class TestFun(unittest.TestCase):
  def test_3_4(self):
    self.assertEqual(7,fun.ff(3,4)) 
