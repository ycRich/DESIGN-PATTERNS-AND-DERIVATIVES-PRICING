import numpy as np

def simpleMonteCarlo1(Expiry, Strike, Spot, Vol, r, NumberOfPaths):
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
    avgPayOff = np.mean([max(s_t, 0) for s_t in movedSpot])
    

    return np.exp( - r * Expiry) * avgPayOff


if __name__ == "__main__":
    Expiry = float(input("\nEnter expiry\n"))
    Strike = float(input("\nEnter strike\n"))
    Spot = float(input("\nEnter spot\n"))
    Vol = float(input("\nEnter vol\n"))
    r = float(input("\nEnter r\n"))
    NumberOfPaths = int(input("\nEnter number of paths\n"))

    res = simpleMonteCarlo1(Expiry,
                            Strike,
                            Spot,
                            Vol,
                            r,
                            NumberOfPaths)

    print("The price is {}".format(res))
