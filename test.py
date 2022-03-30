import simple

def test_add():
    assert simple.add(3, 4) == 7
    assert simple.add(7,8) == 15
    assert simple.add(1,2) == 3

def test_sub():
    assert simple.sub(8, 2) == 6
    assert simple.sub(4, 4) == 0
    