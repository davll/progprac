# Bubble Sort
#
# Worst case: O(n^2) comparisons, O(n^2) swaps
# Avg case: O(n^2) comparisons, O(n^2) swaps
# Best case: O(n) comparisons, O(1) swaps
# Worst case space: O(1) auxiliary
#

from typing import TypeVar, MutableSequence

T = TypeVar('T', int, float)

def bubblesort(a: MutableSequence[T]) -> None:
    n = len(a)
    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
