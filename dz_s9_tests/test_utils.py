import pytest
from utils import create_grid
from utils import delete_words
from utils import sum_digit
from utils import mix_list


def test_create_grid_good():
    assert create_grid() == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.mark.parametrize('a, text, expected_result', [('р', 'над пропастью во ржи', 'над во'),
                                                   ('l', 'hello world', ''),
                                                   ('r', 'hello world', 'hello')])
def test_delete_words_good(a, text, expected_result):
    assert delete_words(a, text) == expected_result


@pytest.mark.parametrize('expected_exception, message, value', [(TypeError, 'hello world', 4)])
def test_type_error(expected_exception, message, value):
    with pytest.raises(expected_exception):
        delete_words(value, message)


@pytest.mark.parametrize('a,expected_result', [('0,56', 11),
                                               ('6,33', 12),
                                               ('10,1', 2)])
def test_sum_digit_good(a, expected_result):
    assert sum_digit(a) == expected_result


@pytest.mark.parametrize('seq', [([1, 2, 3, 4, 5]),
                                (['f', 'r', 4])])
def test_mix_list_good(seq):
    set1 = seq
    set2 = mix_list(seq)
    assert set1 != set2





