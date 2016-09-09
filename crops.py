"""Some code to carry out monte carlo for an outreach event"""

from collections import namedtuple
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import binomial
from numpy import mean

def number_of_crops(small, medium, large, days=7, p=0):
    """
    The number of crops of each type of for a given number of days

    Note that the following number of days are required for each crop
    type to develop:

    - small: 7
    - medium: 3
    - large: 2

    p is the probability of any given crop not fully developing
    """

    nbr_small = binomial(small * int(days / 7), 1 - p)
    nbr_medium = binomial(medium * int(days / 7), 1 - p)
    nbr_large = binomial(large * int(days / 7), 1 - p)

    return nbr_small, nbr_medium, nbr_large

harvest = namedtuple("Harvest", ("small", "medium", "large"))

def monte_carlo(small, medium, large, days, p, repetitions):
    """
    Perform a monte carlo simulation of the
    number of crops we obtain

    p is the probability of a given crop dying
    repetitions is the number of simulations we want to carry out
    """
    harvests = [harvest(*number_of_crops(small, medium, large, days, p))
                for _ in range(repetitions)]
    return harvests

def experiment(small, medium, large, p, repetitions=10000, days=7):
    """Plot the results of a monte carlo simulation"""
    harvests = monte_carlo(small, medium, large, days, p, repetitions)
    plt.figure(0)
    x = [h.small for h in harvests]
    plt.hist(x, color='blue')
    plt.title('Small. Average={:.4}'.format(mean(x)))
    plt.figure(1)
    x = [h.medium for h in harvests]
    plt.hist(x, color='red')
    plt.title('Medium. Average={:.4}'.format(mean(x)))
    plt.figure(2)
    x = [h.large for h in harvests]
    plt.hist(x, color='green')
    plt.title('Large. Average={:.4}'.format(mean(x)))
    plt.show()
