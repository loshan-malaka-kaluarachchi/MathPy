import sys
sys.path.insert(0,'/home/mypc/gitHub/MathPy/')

import unittest
from classes.symbolic import Math_Symb


class Testcase_symbolic_methods(unittest.TestCase):
    def test_init_method(self):
        self.assertIsInstance(Math_Symb(0,'X',0),Math_Symb)
        self.assertEqual(print(Math_Symb(0,'X',0)),None)
        
    def test__add__method(self):
        symb1 = Math_Symb(1,'X',0)
        symb2 = Math_Symb(2,'X',0)
        self.assertIsInstance(symb1,Math_Symb)
        self.assertIsInstance(symb2,Math_Symb)
        self.assertEqual(symb1 + symb2, Math_Symb(3,'X',0))
        
        
        
if __name__ == '__main__':
    unittest.main()
    