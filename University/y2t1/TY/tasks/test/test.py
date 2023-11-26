P1 = 1 - 0.6
P2 = 1 - 0.8
P3 = 1 - 0.9

P_not_fail = P1 * P2 * P3

P_fail = 1 - P_not_fail

print(P_not_fail)
