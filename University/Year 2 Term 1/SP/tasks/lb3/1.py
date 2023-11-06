def can_introduce(n, a):
    if n == 0:
        return True
    if a[n - 1] > n - 1:
        return False
    a_sorted = sorted(a[: n - 1], reverse=True)
    for i in range(a[n - 1]):
        if a_sorted[i] > 0:
            a_sorted[i] -= 1
        else:
            return False
    return can_introduce(n - 1, a_sorted)


# Example usage:
n = 5
a = [3, 2, 1, 2, 0]
print(can_introduce(n, a))  # Output: True
