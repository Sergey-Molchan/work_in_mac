from typing import Callable, Optional, Any
import functools
import sys

def log_to_file(func: Callable) -> Callable:
    """Логирует результат выполнения функции в файл."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            result = func(*args, **kwargs)
            with open("test_log.txt", "a", encoding="utf-8") as f:
                f.write(f"{func.__name__} ok\n")
            return result
        except Exception as e:
            with open("test_log.txt", "a", encoding="utf-8") as f:
                f.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}\n")
            raise
    return wrapper

def log_to_console(func: Callable) -> Callable:
    """Логирует результат выполнения функции в консоль."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        print(f"Результат: {repr(result)}")
        return result
    return wrapper