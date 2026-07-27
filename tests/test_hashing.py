from hashmap.hashing import string_hash, bucket_index


def test_deterministic():
    assert string_hash("hello") == string_hash("hello")


def test_order_matters():
    assert string_hash("ab") != string_hash("ba")


def test_bucket_in_range():
    for key in ["a", "bb", "ccc", "apple", "zebra"]:
        idx = bucket_index(key, 8)
        assert 0 <= idx < 8


def test_empty_key():
    assert string_hash("") == 0
