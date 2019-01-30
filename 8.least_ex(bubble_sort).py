
def solution(line):
    n = line.split(',')
    n = list(map(int, n))
    l = len(n)
    count = 0
    for i in range(l-1):
        for j in range(l-i-1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
                count += 1
    return count


print(solution('2,3,1,5,7,8,6,9,4,0'))
