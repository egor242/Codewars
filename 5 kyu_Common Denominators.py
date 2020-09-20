from functools import reduce


def convertFracts(lst):
    if len(lst) == 0:
        return []
    def lcm(a, b):
        m = a * b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return m // (a + b)

    denominators = [l[1] for l in lst]
    lcm_lst = reduce(lcm, denominators)

    return [[l[0] * lcm_lst // l[1], lcm_lst] for l in lst]


print(convertFracts([[1, 2], [1, 3], [1, 4]]))