""" This Module will have tests
"""
from calculator.lumpsum import lumpsum
from calculator.sip import sip
def test_lumpsum():
    """this funtion tests the lumpsum"""
    #assert(round(lumpsum(100000,18,15))==1197375)
    assert(round(lumpsum(25000,12,10))==77646)
def test_sip():
    """this funtion tests the lumpsum"""
    #assert(round(lumpsum(100000,18,15))==1197375)
    assert(round(sip(25000,12,10))==5808477)