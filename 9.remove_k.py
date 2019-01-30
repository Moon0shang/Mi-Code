
def solution(line):
    n, k = line.split(' ')
    k = int(k)
    keep = min(map(int, list(n[:(k + 1)])))
    if keep == 0 and k + 1 == len(n):
        s = 0
    elif keep == 0:
        s = n[(k + 1):]
    else:
        s = ''.join([str(keep), n[(k + 1):]])

    return s

#     if '0' in n:
#         s = zero_split(n, k)
#     else:
#         s = rm(n, k)

#     return s


# def zero_split(n, k):
#     s1, s2 = n.split('0', maxsplit=1)
#     if len(s1) > k:
#         s = rm(s1, k)
#     elif len(s1) == k:
#         if s2 == '':
#             s = 0
#         else:
#             s = s2
#     else:
#         if '0' in s2:
#             s = zero_split(s2, k)

#     return s


# def rm(n, k):

#     keep = min(map(int, list(n[:(k+1)])))
#     s = ''.join([str(keep), n[(k + 1):]])

#     return s


print(solution('1432219 3'))
