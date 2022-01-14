def num_ways_with_1_2_to_get(n):
    """
    Test:
    >>> num_ways_with_1_2_to_get(3)
    1 + 1 + 1
    1 + 2
    2 + 1
    3
    >>> num_ways_with_1_2_to_get(4)
    1 + 1 + 1 + 1
    1 + 1 + 2
    1 + 2 + 1
    2 + 1 + 1
    2 + 2
    5
    """
    if n < 2:
        return 1
    return num_ways_with_1_2_to_get(n - 1) + num_ways_with_1_2_to_get(n - 2)


def num_ways_with_1_2_to_get_helper(n, i):
    if n == 1:
        print(f"{i} + 1")
    elif n == 2:
        print(f"{i} + 1 + 1")
        print(f"{i} + 2")
    else:
        if(i == " "):
            num_ways_with_1_2_to_get_helper(n-1, i + "1")
            num_ways_with_1_2_to_get_helper(n-2, i + "2")
            print(num_ways_with_1_2_to_get(n))
        else:
            num_ways_with_1_2_to_get_helper(n-1, i + " + 1")
            num_ways_with_1_2_to_get_helper(n-2, i + " + 2")

def num_ways_with_1_2_to_get_helper2(n):
    
    num_ways_with_1_2_to_get(n)
    num_ways_with_1_2_to_get_helper(n, "")
    
num_ways_with_1_2_to_get_helper2(4)