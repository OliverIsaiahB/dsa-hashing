from hashmap.open_map import OpenMap


def test_put_get():
    m = OpenMap()
    m.put("a", 1)
    m.put("b", 2)
    assert m.get("a") == 1
    assert m.get("b") == 2


def test_overwrite():
    m = OpenMap()
    m.put("x", 1)
    m.put("x", 5)
    assert m.get("x") == 5


def test_delete_then_probe_still_finds_later_key():
    # Tiny capacity forces probing; deleting a middle key must not hide a later one.
    m = OpenMap(capacity=4)
    m.put("a", 1)
    m.put("b", 2)
    m.put("c", 3)
    m.delete("b")
    assert m.get("c") == 3
    assert m.get("b") is None


def test_reuse_tombstone():
    m = OpenMap(capacity=4)
    m.put("a", 1)
    m.delete("a")
    m.put("a", 7)
    assert m.get("a") == 7
