import numpy as np


class PayOff:
    def __init__(self, strike, optionType):
        self.strike = strike
        self.optionType = optionType

    def __call__(self, spot):
        if self.optionType.lower() == 'call':
            return max(spot - self.strike, 0)
        elif self.optionType.lower() == 'put':
            return max(self.strike - spot, 0)
        else:
            raise Exception("unkown option type found")


def simpleMonteCarlo2(payOff, Expiry, Strike, Spot, Vol, r, NumberOfPaths):
    """Simple Monte Carlo implementation to price vanila call option

    Arguments:
        Expiry {float} -- time to expiry
        Strike {float} -- strike price
        Spot {float} -- spot/current price
        Vol {float} -- volatility
        r {float} -- continuous compounding rate
        NumberOfPaths {int} -- number of simulations

    Returns:
        {float} -- option price
    """
    variance = Vol*Vol*Expiry
    rootVariance = np.sqrt(variance)
    itoCorrection = -0.5 * variance
    
    W = np.random.randn(NumberOfPaths, 1)

    movedSpot = Spot * np.exp(r * Expiry + itoCorrection + rootVariance * W)
    avgPayOff = np.mean([payOff(s_t) for s_t in movedSpot])
    

    return np.exp( - r * Expiry) * avgPayOff


if __name__ == "__main__":
    Expiry = float(input("\nEnter expiry\n"))
    Strike = float(input("\nEnter strike\n"))
    Spot = float(input("\nEnter spot\n"))
    Vol = float(input("\nEnter vol\n"))
    r = float(input("\nEnter r\n"))
    NumberOfPaths = int(input("\nEnter number of paths\n"))

    payOffCall = PayOff(Strike, 'call')
    payOffPut = PayOff(Strike, 'put')
    call_price = simpleMonteCarlo2(payOffCall, 
                            Expiry,
                            Strike,
                            Spot,
                            Vol,
                            r,
                            NumberOfPaths)
    put_price = simpleMonteCarlo2(payOffPut, 
                            Expiry,
                            Strike,
                            Spot,
                            Vol,
                            r,
                            NumberOfPaths)


    print("Call price is {}".format(call_price))
    print("Put price is {}".format(put_price))
