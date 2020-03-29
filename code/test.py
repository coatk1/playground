#import unittest
import geo as g

def test_add():
    assert g.Calc().add(2, 3) == 5, 'Should be 5'

def test_mul():
    assert g.Calc().multiply(2, 3) == 6, 'Should be 6'
    
def test_power():
    assert g.Distance(2).power(2) == 4, 'Should be 4'