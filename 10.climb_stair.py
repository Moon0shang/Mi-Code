from math import factorial


def solution(line):
    n = int(line)
    max2 = n // 2
    p = 0
    for i in range(max2+1):
        m = n - i * 2
        l = i + m
        if m == 0 or m == l:
            p += 1
        else:
            p += factorial(l)/(factorial(l-m)*factorial(m))

    return int(p)


print(solution('5'))
