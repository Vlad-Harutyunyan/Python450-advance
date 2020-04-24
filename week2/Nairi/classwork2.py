from array import array
import sys
from collections import defaultdict
from queue import Queue
a1 = array('f',[1,2,3])
print(sys.getsizeof(array('l',[])))
print(sys.getsizeof(array('l',[1])))
print(sys.getsizeof(array('l',[1,2])))

a2 = array('u',['a','b','s'])
print(a2)

s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
d = defaultdict(list)

for k , v in s:
    d[k].append(v)
print(d)

#practical problem is_polyndrome
s = 'abbab'
d1 = defaultdict(int)

for k in s:
    d1[k] = d1[k]+1

print(d1)

a3 = frozenset({1,2,3})
print(sys.getsizeof(a3))
print(a3)
q = Queue(maxsize = 10)

from heapq import heappush , heappop

def heapsort(arr):
    
    h = []
    for value in arr :
        heappush(h,value)
        print(h)
    return [heappop(h) for i in range(len(h))]


heapsort([1,2,4,2,1,3,5,10,2,6,345,3,89,41])