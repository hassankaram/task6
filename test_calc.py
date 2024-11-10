import unittest

class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)
        
    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(2, -3), -1)
        
    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 5), 5)

if _name_ == '_main_':
    unittest.main()
