from hashmap.lookup import two_sum, first_duplicate


def test_two_sum_unsorted():
    assert two_sum([3, 1, 4, 2], 6) == (2, 3)


def test_two_sum_none():
    assert two_sum([1, 2, 3], 100) is None


def test_two_sum_uses_earlier_index():
    assert two_sum([0, 4, 3, 0], 0) == (0, 3)


def test_first_duplicate():
    assert first_duplicate([1, 2, 3, 2, 1]) == 2


def test_first_duplicate_none():
    assert first_duplicate([1, 2, 3]) is None
