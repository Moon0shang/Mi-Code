
def solution(line):
    s1, s2 = line.split(' ')
    s = list(s2)
    for i in list(s1):
        try:
            s.remove(i)
        except:
            return 'false'

    return 'true'


print(solution('uak areuok'))
