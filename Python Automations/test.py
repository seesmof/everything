import math

# Step 1: Calculate the number of pixels diagonally
w = 1440  # device width in pixels
h = 3040  # device height in pixels
d_o = math.sqrt(w**2 + h**2)  # number of pixels in the diagonal of the device

# Step 2: Calculate PPI
d_i = 6.1  # device screen size in inches
PPI = d_o / d_i  # PPI

print("PPI =", round(PPI))
