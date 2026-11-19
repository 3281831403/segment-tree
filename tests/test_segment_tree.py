import pytest

from range import segment_tree as mod

CASES = [
    ('build', [[1, 2, 3]], [0, 6, 3, 3, 1, 2, 0, 0, 0, 0, 0, 0], False),
    ('build', [[]], [0, 0, 0, 0], False),
    ('query_sum', [[0, 6, 3, 3, 1, 2, 0, 0, 0, 0, 0, 0], 0, 1, 3], 3, False),
    ('query_sum', [[0, 6, 3, 3, 1, 2, 0, 0, 0, 0, 0, 0], 1, 2, 3], 5, False),
    ('update', [[0, 6, 3, 3, 1, 2, 0, 0, 0, 0, 0, 0], 1, 5, 3], [0, 9, 6, 3, 1, 5, 0, 0, 0, 0, 0, 0], False),
    ('query_min', [[0, 13, 6, 7, 4, 2, 0, 0, 0, 0, 0, 0], 0, 2, 3], 13, False),
    ('tree_height', [3], 3, False),
    ('tree_height', [0], 0, False),
    ('build', [[5]], [0, 5, 0, 0], False),
    ('query_sum', [[0, 6, 3, 3, 1, 2, 0, 0, 0, 0, 0, 0], 2, 2, 3], 3, False),
    ('query_sum', [[0, 0, 0, 0], 0, 0, 1], 0, False),
    ('update', [[0, 3, 1, 2, 0, 0, 0, 0], 0, 9, 2], [0, 11, 9, 2, 0, 0, 0, 0], False),
    ('query_min', [[0, 6, 3, 3, 1, 2, 0, 0, 0, 0, 0, 0], 1, 1, 3], 2, False),
    ('tree_height', [1], 1, False),
    ('tree_height', [4], 3, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_segment_tree_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
