

def solution(line):
    n = line.split(',')
    m = sorted(list(map(int, n)))
    l_max = 1
    i = 0
    while i < len(m):
        j = 0
        while m[i]+j == m[i+j]:
            ll = j+1
            if i+j < len(m)-1:
                j += 1
            else:
                break

        l_max = max(l_max, ll)
        if i+j < len(m)-1:
            i += j
        else:
            break
    return l_max


print(solution('1,2,3,4,5,6,10'))
