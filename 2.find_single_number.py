
def solution(line):
    n = line.split(' ')
    m = set(n)
    for i in m:
        n.remove(i)
    num = set(n)
    result = m - num
    m = sorted(list(map(int, n)))
    for i in range((len(m))//2):
        if m[2*i] != m[2*i+1]:
            result = m[2*i]
        else:
            result = m[-1]

    return list(result)[0]


print(solution('10 10 11 12 12 11 16'))
