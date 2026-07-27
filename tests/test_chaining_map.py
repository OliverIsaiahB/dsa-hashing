from hashmap.chaining_map import ChainingMap


def test_put_get():
    m = ChainingMap()
    m.put("a", 1)
    m.put("b", 2)
    assert m.get("a") == 1
    assert m.get("b") == 2


def test_overwrite():
    m = ChainingMap()
    m.put("a", 1)
    m.put("a", 9)
    assert m.get("a") == 9
    assert len(m) == 1                # overwrite must not grow size


def test_missing_key():
    m = ChainingMap()
    assert m.get("nope") is None
    assert m.contains("nope") is False


def test_collisions_still_work():
    m = ChainingMap(num_buckets=1)
    for i, key in enumerate(["a", "b", "c", "d"]):
        m.put(key, i)
    assert [m.get(k) for k in ["a", "b", "c", "d"]] == [0, 1, 2, 3]


def test_resize_preserves_everything():
    m = ChainingMap(num_buckets=2)
    keys = [f"k{i}" for i in range(50)]
    for i, key in enumerate(keys):
        m.put(key, i)
    assert len(m) == 50
    assert all(m.get(f"k{i}") == i for i in range(50))
