""" This Module will have tests
"""
from calculator.lumpsum import returns as lumpsum_returns
from calculator.sip import returns as sip_returns
def test_lumpsum():
    """this funtion tests the lumpsum"""
    #assert(round(lumpsum(100000,18,15))==1197375)
    assert(lumpsum_returns(25000,12,10)==776,46)
def test_sip():
    """this funtion tests the lumpsum"""
    #assert(round(lumpsum(100000,18,15))==1197375)
    assert(sip_returns(25000,12,10)==5,808,477)