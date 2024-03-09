from timeit import default_timer as timer

# decorator that wraps the function and measures the execution time
def timer_func(func):
    def wrapper(*args, **kwargs):
        t1 = timer()
        result = func(*args, **kwargs)
        t2 = timer()
        print(f'{func.__name__}() executed in {(t2-t1):.6f}s')
        return result
    return wrapper


#########################################################################################
"""
-Euclid's algorithm
The algorithm involves iteratively dividing the larger integer by the smaller one 
and replacing the larger integer with the remainder until the remainder becomes zero. 
At this point, the last non-zero remainder is the GCD of the two numbers. 
"""
@timer_func
def gcd1(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a


##########################################################################################
"""
-Stein's algorithm
We replace the division operations in the Euclidean algorithm with faster bitwise operations.
"""
@timer_func
def gcd2(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    # we find K, where K is the greatest power of 2 that divides both a and b.
    k = 0
    #we do right shift on a and b by one position, equivalent to dividing by 2
    #a | b - checks if there's at least one "1" bit in either a or b
    #((a | b) & 1) - checks the least significant bit (the rightmost bit) of the result of a | b to see if it's 1 or 0
    while (((a | b) & 1) == 0):
        a = a >> 1
        b = b >> 1
        k = k + 1
    # Dividing a by 2 until a becomes odd
    while ((a & 1) == 0):
        a = a >> 1

    # From here on, 'a' is always odd.
    while (b != 0):

        # If b is even, remove all
        # factor of 2 in b
        while ((b & 1) == 0):
            b = b >> 1

        # Now a and b are both odd. Swap if necessary so a <= b, then set b = b - a (which is even).
        if (a > b):
            # Swap u and v.
            temp = a
            a = b
            b = temp

        b = (b - a)

    # restore common factors of 2
    return (a << k)
########################################################################################
@timer_func
def gcd3(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    dMax = 1
    d = 2
    while (d <= min(a, b)):
        if a%d == 0 and b%d == 0:
            dMax = d
        d = d+1
    return dMax

######################################################################################48
if __name__ == '__main__':
    result = gcd1(48, 18)
    print(f"GCD of 48 and 18 is {result}")
    result = gcd1(60, 48)
    print(f"GCD of 60 and 48 is {result}")
    result = gcd1(1024, 512)
    print(f"GCD of 1024 and 512 is {result}")
    result = gcd1(105, 35)
    print(f"GCD of 105 and 35 is {result}")
    result = gcd2(48, 18)
    print(f"GCD of 48 and 18 is {result}")
    result = gcd2(60, 48)
    print(f"GCD of 60 and 48 is {result}")
    result = gcd2(105, 35)
    print(f"GCD of 105 and 35 is {result}")
    result = gcd3(48, 18)
    print(f"GCD of 48 and 18 is {result}")
    result = gcd3(60, 48)
    print(f"GCD of 105 and 35 is {result}")
    result = gcd3(105, 35)
    print(f"GCD of 105 and 35 is {result}")


    print("Insert 2 numbers: ")
    a = int(input("a: "))
    b = int(input("b: "))
    print(gcd1(a, b))
    print(gcd2(a, b))
    print(gcd3(a, b))


