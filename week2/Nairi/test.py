def heappush(heap, val):
    le = len(heap)
    heap.append(val)
    while le > 0:
        parent = (le - 1) // 2
        if heap[parent] <= heap[le]: 
            break
        heap[le], heap[parent] = heap[parent], heap[le]
        le = parent
        pass
    pass

h = [1,2,3,5]
n = 2
print(heappush(h,n))
print(5)