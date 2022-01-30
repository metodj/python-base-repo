import numpy as np


def hello_with_lucky_number(name: str, a: int, b: int, seed: int = 0) -> str:
    """

    :param name:
    :param a:
    :param b:
    :param seed:
    :return:
    """
    np.seed(seed)
    num = np.random.choice(list(range(a, b)), 1)[0]
    return f"Hello {name}! Your lucky number is {num}."
