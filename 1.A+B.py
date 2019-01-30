# import sys
import time
import numpy as np
t1 = time.time()
print(t1)
data = input('please input')

a = data.split(' ')
l1 = len(a[0])
l2 = len(a[1])

if l1 > 9 or l2 > 9:
    if l1 > l2:
        # l = l1-l2
        r1 = str(int(a[0][l1-l2:])+int(a[1]))
        if len(r1) > l2:
            r2 = str(int(a[0][l1-l2])+int(r1[0]))
        else:
            r2 = a[0][:l1-l2]
    else:
        r1 = str(int(a[0])+int(a[1][l2-l1]))
        if len(r1) > l1:
            r2 = str(int(a[1][l2-l1:])+int(r1[0]))
        else:
            r2 = a[1][:l2-l1]

    result = ''.join([r2, r1])
else:
    result = int(a[0])+int(a[1])
t2 = time.time()
print(t2)
print('result:', int(result),
      '\ntime:', t2-t1)
