import numpy as np


def lucky_number(name: str, left: int, right: int) -> str:
    """
    Example function.

    :param name:
    :param left:
    :param right:
    :return:
    """
    if left > right:
        raise ValueError("left <= right violated!")
    num = np.random.choice(list(range(left, right)), 1)[0]
    return f"Hello {name}! Your lucky number is {num}!"
