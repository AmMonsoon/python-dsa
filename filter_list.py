# Filter List

## Pattern
Filtering / Array Traversal

## Optimized Solution
Traverse the list once using a list comprehension. For each element, check whether it is an
integer or float using `isinstance()`. If it is a numeric value, include it in the returned
list.

## Time Complexity
O(n)

Where `n` is the number of elements in the input list. Each element is checked exactly once.

## Space Complexity
O(n)

In the worst case, every element is a number, so the returned list contains all `n` elements.


def filter_list(l):
    return [el for el in l if isinstance(el, (int, float))]


print(filter_list([1, 2, 'a', 'b'])) #[1, 2], 'For input [1, 2, "a", "b"]')
print(filter_list([1, 'a', 'b', 0, 15])) # [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
print(filter_list([1, 2, 'aasf', '1', '123', 123])) # [1, 2, 123], 'For input [1, 2, "aasf", "1", "123", 123]')