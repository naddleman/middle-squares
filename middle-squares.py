"""
implements von Neumann's middle-square method for generating pseudorandom
numbers of even digit counts. It's a rather bad method, in fact.
"""
import sys
import bisect
def mid_square(n):
    """ returns a 'pseudorandom' integer with the same number of digits as n.
    n must have an even number of digits
    """
    sqr = n**2
    val = sqr // (10**(dig_count / 2))
    val = int(val % (10**dig_count) )
    return val

def mid_square_list(n, length):
    lis = []
    a = n
    for _ in range(length):
        lis.append(a)
        a = mid_square(a)
    return lis

if __name__ == '__main__':
    args = sys.argv
    usage = 'Usage: %s <initial integer> <length>' % (args[0], )
    if (len(args) != 3):
        raise Exception(usage)
    n, length = map(int, (args[1], args[2]))
    dig_count = len(str(n))
    if dig_count % 2 != 0:
        raise Exception('must have even number of digits')
    lis = mid_square_list(n, length)
    print(lis)
