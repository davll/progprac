from collections import deque, namedtuple
import operator as op

def median_sliding_window_v1(nums, k):
    queue = deque()
    results = []
    median = [0] * k
    for x in nums:
        while len(queue) >= k:
            queue.popleft()
        queue.append(x)
        if len(queue) == k:
            for j in range(k):
                median[j] = queue[j]
            median.sort()
            if k % 2 == 1:
                results.append(float(median[k//2]))
            else:
                results.append((median[k//2]+median[k//2-1])/2)
    return results

def median_sliding_window_v2(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return []
    leftheap = MaxHashHeap()
    rightheap = MinHashHeap()
    def median():
        if k % 2 == 1:
            assert len(leftheap) == len(rightheap) + 1
            return float(leftheap.peak()[1])
        else:
            assert len(leftheap) == len(rightheap)
            return (leftheap.peak()[1] + rightheap.peak()[1]) / 2
    for i in range(k):
        if i % 2 == 0:
            rightheap.add(i, nums[i])
            leftheap.add(*(rightheap.pop()))
        else:
            leftheap.add(i, nums[i])
            rightheap.add(*(leftheap.pop()))
    results = [median()]
    for i in range(k, n):
        j = i - k
        if j in rightheap:
            rightheap.remove(j)
            leftheap.add(i, nums[i])
            rightheap.add(*(leftheap.pop()))
        else:
            leftheap.remove(j)
            rightheap.add(i, nums[i])
            leftheap.add(*(rightheap.pop()))
        results.append(median())
    return results

class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        return median_sliding_window_v2(nums, k)

Entry = namedtuple('Entry', ['key', 'value'])

class HashHeap:
    def __init__(self, lt=op.lt):
        self._heap = [0]
        self._hash = {}
        self._less = lt
    #
    def __len__(self):
        return self._heap[0]
    def __bool__(self):
        return self._heap[0] > 0
    def __contains__(self, key):
        return key in self._hash
    def __getitem__(self, key):
        return self._heap[self._hash[key]].value
    def __str__(self):
        return "[{h}]".format(h=', '.join(map(lambda e: "{k}: {v}".format(k=e.key, v=e.value), self._heap[1:])))
    #
    @property
    def size(self):
        return self._heap[0]
    #
    def peak(self):
        if self._heap[0] == 0:
            raise IndexError()
        k, v = self._heap[1]
        return (k, v)
    #
    def pop(self):
        if self._heap[0] == 0:
            raise IndexError()
        k, v = self._heap[1]
        self._remove(1)
        return (k, v)
    #
    def add(self, key, value):
        if key in self._hash:
            raise IndexError()
        self._heap.append(Entry(key, value))
        index = self._heap[0] + 1
        self._hash[key] = index
        assert self._heap[index].key == key
        self._heap[0] += 1
        self._heapify(index)
    #
    def remove(self, key):
        if key not in self._hash:
            raise IndexError()
        index = self._hash[key]
        self._remove(index)
    #
    def _remove(self, index):
        last = self._heap[0]
        self._swap(index, last)
        del self._hash[self._heap[last].key]
        self._heap.pop()
        self._heap[0] -= 1
        if index <= self._heap[0]:
            self._heapify(index)
    #
    def _swap(self, a, b):
        h = self._heap
        h[a], h[b] = h[b], h[a]
        self._hash[h[a].key] = a
        self._hash[h[b].key] = b
    #
    def _heapify(self, i):
        n = self._heap[0]
        h = self._heap
        # upward
        while i > 1:
            p = i // 2 # parent
            if self._less(h[p].value, h[i].value):
                self._swap(p, i)
                i = p
            else:
                break
        # downward
        while i <= n:
            l = i * 2     # left child
            r = i * 2 + 1 # right child
            maxi = i
            if l <= n and self._less(h[maxi].value, h[l].value):
                maxi = l
            if r <= n and self._less(h[maxi].value, h[r].value):
                maxi = r
            if maxi != i:
                self._swap(i, maxi)
                i = maxi
            else:
                break
        return i

def MinHashHeap():
    return HashHeap(lt=op.gt)

def MaxHashHeap():
    return HashHeap(lt=op.lt)
