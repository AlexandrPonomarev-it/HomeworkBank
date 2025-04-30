from functools import wraps
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор позволяет логировать время, результатов работы функции и возможных ошибок,
    а также вывода полученных данных в консоль или их записи в текстовый файл
    """
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as error:
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")
        return inner
    return wrapper


@log()
def my_function(x: int, y: int):
    return x / y

my_function(1, 2)
my_function(1, 0)