"""A hash map using OPEN ADDRESSING with linear probing: all pairs live in ONE
flat array. On a collision, probe the next slot until an empty one is found."""
from __future__ import annotations

from hashmap.hashing import string_hash

_EMPTY = object()      # never-used slot
_DELETED = object()    # a "tombstone": was used, now removed


class OpenMap:
    def __init__(self, capacity: int = 8) -> None:
        self._slots: list = [_EMPTY] * capacity   # each slot: _EMPTY, _DELETED, or (key, value)

    def _probe(self, key: str):
        """Yield slot indices starting at the key's home, walking forward."""
        start = string_hash(key) % len(self._slots)
        for step in range(len(self._slots)):
            yield (start + step) % len(self._slots)   # wrap around the array

    def put(self, key: str, value: int) -> None:
        first_free = None
        for idx in self._probe(key):
            slot = self._slots[idx]
            if slot is _EMPTY:
                self._slots[first_free if first_free is not None else idx] = (key, value)
                return
            if slot is _DELETED:
                if first_free is None:
                    first_free = idx          # remember a reusable tombstone
                continue
            if slot[0] == key:
                self._slots[idx] = (key, value)   # overwrite existing key
                return

    def get(self, key: str) -> int | None:
        for idx in self._probe(key):
            slot = self._slots[idx]
            if slot is _EMPTY:
                return None                   # an empty slot means key absent
            if slot is _DELETED:
                continue                      # skip tombstones, keep probing
            if slot[0] == key:
                return slot[1]
        return None

    def delete(self, key: str) -> None:
        for idx in self._probe(key):
            slot = self._slots[idx]
            if slot is _EMPTY:
                return
            if slot is not _DELETED and slot[0] == key:
                self._slots[idx] = _DELETED   # tombstone, don't break the probe chain
                return
