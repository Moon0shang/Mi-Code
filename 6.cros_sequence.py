
def solution(line):

    l1, l2, s = line.split(',')
    if len(s) != len(l1)+len(l2):
        return 'false'
    if len(s) == 2:
        if s == l1 + l2 or s == l2 + l1:
            return True
        else:
            return False

    idx_s = 0
    idx_l1 = 0
    idx_l2 = 0
    while idx_s < len(s)-1:
        idx_l1, idx_s, i1 = match(l1, s, idx_l1, idx_s)
        idx_l2, idx_s, i2 = match(l2, s, idx_l2, idx_s)
        if i1 == 0 and i2 == 0:
            return False

    return True


def match(l, s, idx_l, idx_s):

    i = 0
    while l[idx_l + i] == s[idx_s + i]:
        if idx_l+i <= len(l)-1:
            i += 1
            if idx_l + i > len(l) - 1:
                idx_l -= 1
                break
        else:
            break
    if idx_s + i > len(s) - 1:
        idx_s -= 1
    idx_s += i
    idx_l += i

    return idx_l, idx_s, i


print(solution('aabcc,dbbca,aadbbcbca'))
