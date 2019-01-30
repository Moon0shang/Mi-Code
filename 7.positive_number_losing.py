
def solution(line):
    n = line.split(',')
    n = map(int, n)
    p = list(filter(positive, n))
    if p:
        m = max(p)+2
        for i in range(1, m):
            if i not in p:
                return i
    else:
        return 1


def positive(i):
    return i > 0


print(solution('-1,-10,0'))
