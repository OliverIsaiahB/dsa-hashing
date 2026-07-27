"""A hash function maps a key to an integer, which we squeeze into a bucket
index with modulo. Good hashing is deterministic and spreads keys evenly."""
from __future__ import annotations


def string_hash(key: str) -> int:
    """A simple polynomial rolling hash. Deterministic: same key -> same number.
    Multiplying by 31 mixes character positions so 'ab' and 'ba' differ."""
    h = 0
    for ch in key:
        h = h * 31 + ord(ch)         # combine the running hash with the next char
    return h


def bucket_index(key: str, num_buckets: int) -> int:
    """Squeeze an arbitrary hash into a valid bucket index [0, num_buckets)."""
    return string_hash(key) % num_buckets
