"""Frequency counting: a hash map from item -> count is the workhorse behind
anagrams, top-k, majority element, and 'most/least common' problems."""
from __future__ import annotations

from collections import Counter


def frequencies(items: list[str]) -> dict[str, int]:
    """Count each item in one O(n) pass using get-with-default."""
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1   # default 0 for first sighting
    return counts


def are_anagrams(a: str, b: str) -> bool:
    """Anagrams iff identical character counts — O(n), beating O(n log n) sort."""
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)


def most_common(items: list[str]) -> str | None:
    """Return the most frequent item (ties broken by first to reach the max)."""
    if not items:
        return None
    counts = frequencies(items)
    return max(counts, key=lambda k: counts[k])
