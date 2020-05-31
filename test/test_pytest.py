from simpleMonteCarlo1 import simpleMonteCarlo1
from simpleMonteCarlo2 import simpleMonteCarlo2, PayOff
import numpy as np
from scipy.stats import norm


def optionPrice(s, x, r, sigma, t, type='call'):
    a = (np.log(s/x) + (r + sigma * sigma/2.0) * t) / \
        (sigma * np.sqrt(t))
    b = a - sigma * np.sqrt(t)
    if type == 'call':
        return s * norm.cdf(a) - x * np.exp(-r * t) * norm.cdf(b)
    elif type == 'put':
        return norm.cdf(-b) * x * np.exp(-r * t) - s * norm.cdf(-a)



def test_simpleMonteCarlo1():
    s = 42
    x = 40
    t = 0.5
    r = 0.1
    sigma = 0.2
    assert abs(simpleMonteCarlo1(t,x,s,sigma,r,500000) - optionPrice(s, x, r, sigma, t)) <= 1e-2


def test_simpleMonteCarlo2():
    s = 42
    x = 40
    t = 0.5
    r = 0.1
    sigma = 0.2
    payOffCall = PayOff(x, 'call')
    payOffPut = PayOff(x, 'put')
    assert abs(simpleMonteCarlo2(payOffCall, t,x,s,sigma,r, 500000) - optionPrice(s, x, r, sigma, t)) <= 1e-2
    assert abs(simpleMonteCarlo2(payOffPut, t,x,s,sigma,r, 500000) - optionPrice(s, x, r, sigma, t, 'put')) <= 1e-2