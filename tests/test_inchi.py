from __future__ import print_function

import unittest

import six
from pychemy.inchi import InChI

class InchiTest(unittest.TestCase):

  def test_unicode_inchi(self):
    inchi_str = six.u('InChI=1S/C14H18O8/c1-20-9-4-7(5-15)2-3-8(9)21-14-13(19)12(18)11(17)10(6-16)22-14/h2-5,10-14,16-19H,6H2,1H3/t10-,11-,12+,13-,14-/m1/s1')
    inchi = InChI(inchi_str)
    formula = inchi.formula
    self.assertEqual(formula.formula, 'C14H18O8')
