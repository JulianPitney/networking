# enumerate()
# Iterate over a sequence with both index and value cleanly.
seq1 = (25, 2546, 35937, 'fries', int)
for i, v in enumerate(seq1):
    print(f"{i}:{v}")


# zip()
# Combine multiple iterables elementwise into tuples.
l1 = [636, -3636, 0, 34, 2, 2, 34]
t1 = ('fries', 'shrimps', 14, 55, True, 5, 0)
for i in zip(l1, t1):
    print(f"{i}")



# map() / filter() | Functional programming patterns — lazy and clean transformations.
# sorted() | Custom sorting with key=, e.g., sort by multiple fields, lambda sorting.
# any() / all() | Quick checks over iterables — compact for validations, checks, guards.
# sum() | Fast summing of numbers or simple reduction operations.
# min() / max() | Find smallest/largest, often with custom key functions (e.g., by length, by score).
# reversed() | Reverse iterables without copying (especially important for memory efficiency).
# isinstance() / issubclass() | Type checking (important for defensive programming and duck-typing edge cases).