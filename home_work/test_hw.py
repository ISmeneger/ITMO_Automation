def test_passing_one():
    assert ('home', 'work') == ('home', 'work')


def test_passing_two():
    assert 'QA' == 'QA'


def test_passing_three():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
