import heapq
def solution(operations):
    heap = []
    op = [o.split(' ') for o in operations]
    for x, y in op:
        if x == 'I':
            heapq.heappush(heap, int(y))
        else:
            y = int(y)
            if y  > 0:
                if heap:
                    heap_max = max(heap)
                    heap.remove(heap_max)
                    heapq.heapify(heap)
                else:
                    pass
            else:
                if heap:
                    heap_min = heapq.heappop(heap)
                else:
                    pass

    if not heap:
        return [0,0]
    else:
        return [max(heap), heapq.heappop(heap)]