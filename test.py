from lowercase_booleans import true, false


def test_true():
    assert true


def test_false():
    assert not false


def test_if_true():
    if true:
        assert True
    else:
        assert False


def test_if_false():
    if false:
        assert False
    else:
        assert True


def test_false_false():
    assert false == false
    assert false == False
    assert False == false
    assert False == False


def test_false_true():
    assert false != true
    assert false != True
    assert False != true
    assert False != True


def test_true_false():
    assert true != false
    assert true != False
    assert True != false
    assert True != False


def test_true_true():
    assert true == true
    assert true == True
    assert True == true
    assert True == True


def test_false_false():
    assert false is false
    assert false is False
    assert False is false
    assert False is False


def test_false_true():
    assert false is not true
    assert false is not True
    assert False is not true
    assert False is not True


def test_true_false():
    assert true is not false
    assert true is not False
    assert True is not false
    assert True is not False


def test_true_true():
    assert true is true
    assert true is True
    assert True is true
    assert True is True
