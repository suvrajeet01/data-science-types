from typing import overload

from . import ndarray

def assert_allclose(
    actual: ndarray, desired: ndarray, rtol: float = 1e-7, atol: float = 0
) -> None: ...
def assert_array_equal(actual: ndarray, desired: ndarray) -> None: ...
@overload
def assert_almost_equal(actual: ndarray, desired: ndarray, decimal: float) -> None: ...
@overload
def assert_almost_equal(actual: float, desired: float, decimal: float) -> None: ...
