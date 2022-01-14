# Make this code DRY

# def same_length(a, b):
#     """Return whether positive integers a and b have the same number of digits."""

#     a_digits = 0
#     while a > 0:
#         a = a // 10
#         a_digits = a_digits + 1
#     b_digits = 0
#     while b > 0:
#         b = b // 10
#         b_digits = b_digits + 1
#     return a_digits == b_digits

# print(same_length(50, 70))
# print(same_length(50, 100))
# print(same_length(10000, 12345))

# ----------------------------------
# dier

def digits(n):
    """Return digits of integer n"""
    n_digits = 0
    while n > 0:
        n //= 10
        n_digits += 1
    return n_digits


def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits.

    >>> same_length(50, 70)
    True
    >>> same_length(50, 100)
    False
    >>> same_length(10000, 12345)
    True
    """
    return digits(a) == digits(b)
