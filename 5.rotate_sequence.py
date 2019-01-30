def solution(line):
    n = line.split(',')
    m = sorted(list(map(int, n)))
    return m[(len(m)//2)]


print(solution('4,5,6,7,0,1,2'))
