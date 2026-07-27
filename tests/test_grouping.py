from hashmap.grouping import group_anagrams, dedup_preserve_order


def test_group_anagrams():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    as_sets = sorted([sorted(g) for g in groups])
    assert ["ate", "eat", "tea"] in as_sets
    assert ["bat"] in as_sets


def test_group_empty():
    assert group_anagrams([]) == []


def test_dedup_preserves_order():
    assert dedup_preserve_order([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_dedup_empty():
    assert dedup_preserve_order([]) == []
