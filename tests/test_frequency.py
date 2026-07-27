from hashmap.frequency import frequencies, are_anagrams, most_common


def test_frequencies():
    assert frequencies(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_frequencies_empty():
    assert frequencies([]) == {}


def test_anagrams_true():
    assert are_anagrams("listen", "silent") is True


def test_anagrams_false_length():
    assert are_anagrams("ab", "abc") is False


def test_most_common():
    assert most_common(["x", "y", "x", "z", "x"]) == "x"


def test_most_common_empty():
    assert most_common([]) is None
