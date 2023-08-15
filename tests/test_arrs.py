from utils import arrs
import pytest


@pytest.mark.parametrize("arr, indx, deflt, result", [
	([1, 2, 3], 1, "test", 2),
	([1, 2, 3], -1, 3, 3),
	([1, 2, 3], -1, None, None)
])
def test_get(arr, indx, deflt, result):
	assert arrs.get(arr, indx, deflt) == result


def test_get_errors():
	with pytest.raises(IndexError):
		assert arrs.get([], 0, 'test' == 'test')


@pytest.mark.parametrize("coll, start, end, result", [
	([1, 2, 3, 4], 1, 3, [2, 3]),
	([1, 2, 3], 1, None, [2, 3]),
	([], 0, None, []),
	([1, 2, 3], -4, None, [1, 2, 3]),
	([1, 2, 3], -3, -1, [1, 2])
])
def test_slice(coll, start, end, result):
	assert arrs.my_slice(coll, start, end) == result
