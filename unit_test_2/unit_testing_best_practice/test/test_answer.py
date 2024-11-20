import sys

#print(sys.path)
# Always run from unit_testing_best_practice/test

sys.path += ['..\\src'] 

#sys.path.insert(1, 'C:/Users/Afra Muhammad/unit_testing_best_practice/src')

from sample import *

def test_answer():
   assert func(4) == 5