import math
from scipy.special import comb

# Calculate binomial coefficient
binomial_coefficient = comb(70, 30, exact=True)

# Calculate powers
power1 = math.pow(0.4, 30)
power2 = math.pow(0.6, 40)

power1 = 0.4**30
power2 = 0.6**40

print(binomial_coefficient * power1 * power2)
