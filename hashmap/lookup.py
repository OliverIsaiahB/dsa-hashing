"""Applying hashing: the complement trick turns 'find two numbers that sum to
target' from an O(n^2) double loop into one O(n) pass with a hash map."""
from __future__ import annotations


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Unsorted two-sum in ONE pass. For each value, ask the map whether its
    complement (target - value) was already seen."""
    seen: dict[int, int] = {}            # value -> index
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return (seen[complement], i)
        seen[value] = i
    return None


def first_duplicate(nums: list[int]) -> int | None:
    """Return the first value that appears twice, using a set as membership test."""
    seen: set[int] = set()
    for value in nums:
        if value in seen:
            return value
        seen.add(value)
    return None
