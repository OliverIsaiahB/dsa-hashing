"""A hash map using SEPARATE CHAINING: each bucket holds a list of (key, value)
pairs. Collisions — two keys in the same bucket — just append to that list.
We resize when the load factor crosses a threshold to keep chains short."""
from __future__ import annotations

from hashmap.hashing import bucket_index


class ChainingMap:
    def __init__(self, num_buckets: int = 8) -> None:
        self._buckets: list[list[tuple[str, int]]] = [[] for _ in range(num_buckets)]
        self._size = 0                       # number of stored keys
        self._max_load = 0.75                # resize when size / buckets exceeds this

    def __len__(self) -> int:
        return self._size

    def put(self, key: str, value: int) -> None:
        bucket = self._buckets[bucket_index(key, len(self._buckets))]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)     # key exists -> overwrite its value
                return
        bucket.append((key, value))          # new key -> add to the chain
        self._size += 1
        if self._size / len(self._buckets) > self._max_load:
            self._resize(len(self._buckets) * 2)

    def get(self, key: str) -> int | None:
        bucket = self._buckets[bucket_index(key, len(self._buckets))]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def _resize(self, new_num_buckets: int) -> None:
        """Grow and REHASH every pair: bucket indices change with bucket count."""
        old_pairs = [pair for bucket in self._buckets for pair in bucket]
        self._buckets = [[] for _ in range(new_num_buckets)]
        for key, value in old_pairs:
            idx = bucket_index(key, new_num_buckets)   # recompute the index
            self._buckets[idx].append((key, value))
