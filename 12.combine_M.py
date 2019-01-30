from math import factorial


def solution(line):
    n, m = line.split(' ')
    m = int(m)
    num = n.split(',')
    num = sorted(list(map(int, num)), reverse=True)
    count = 0
    for i in num:
        mx = m // i
        num1 = num.remove(i)
        if mx == 0:
            count += 1
        for j in range(1, mx):
            for k in num1:
                if (m - j * i) % k == 0:
                    l = j+(m - j * i) // k
                    count += factorial(l)/(factorial(l-j)*factorial(j))
