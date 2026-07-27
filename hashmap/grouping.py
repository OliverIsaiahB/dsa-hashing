"""Grouping: a hash map from a derived KEY to a list of members. Compute a key
that collides exactly when items belong together (e.g. a sorted-letter signature)."""
from __future__ import annotations


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other. The key is the sorted letters,
    which is identical for all anagrams of a word."""
    groups: dict[str, list[str]] = {}
    for word in words:
        signature = "".join(sorted(word))    # anagrams share this signature
        groups.setdefault(signature, []).append(word)
    return list(groups.values())


def dedup_preserve_order(items: list[int]) -> list[int]:
    """Remove duplicates but keep first-seen order — a set tracks what we've seen."""
    seen: set[int] = set()
    out: list[int] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
