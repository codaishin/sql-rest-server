"""validators"""

from typing import Any, TypeGuard


def is_tuple_int_str_str(value: Any) -> TypeGuard[tuple[int, str, str]]:
    """validate value to be of type `tuple[int, str, str]`"""

    if not isinstance(value, tuple):
        return False

    if not len(value) == 3:
        return False

    fst, snd, trd = value

    if not isinstance(fst, int):
        return False

    if not isinstance(snd, str):
        return False

    if not isinstance(trd, str):
        return False

    return True


def has_tuple_int_str_str(
    value: list[Any],
) -> TypeGuard[list[tuple[int, str, str]]]:
    """
    validates that list contains only elements of type `tuple[int, str, str]`
    """

    return all(is_tuple_int_str_str(item) for item in value)
