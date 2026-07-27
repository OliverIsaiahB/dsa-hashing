"""Our hand-built maps must agree with Python's dict, and applications must
agree with a brute-force oracle."""
from hashmap.chaining_map import ChainingMap
from hashmap.open_map import OpenMap
from hashmap.lookup import two_sum


def test_chaining_matches_dict():
    keys = [f"key{i}" for i in range(40)]
    m = ChainingMap(num_buckets=2)
    ref = {}
    for i, key in enumerate(keys):
        m.put(key, i)
        ref[key] = i
    assert all(m.get(k) == ref[k] for k in keys)


def test_open_map_matches_dict():
    m = OpenMap(capacity=64)
    ref = {}
    for i, key in enumerate([f"k{i}" for i in range(30)]):
        m.put(key, i)
        ref[key] = i
    assert all(m.get(k) == ref[k] for k in ref)


def test_two_sum_matches_brute():
    nums = [5, 2, 7, 1, 9, 3]
    target = 10
    brute = None
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                brute = (i, j)
                break
        if brute:
            break
    res = two_sum(nums, target)
    assert (res is None) == (brute is None)
    if res:
        assert nums[res[0]] + nums[res[1]] == target
