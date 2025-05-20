import pytest
import os
from pythonproject.decorators import log_to_file, log_to_console

# Используем актуальные декораторы
@log_to_file
def risky_function(a: int, b: int) -> float:
    return a / b

@log_to_console
def safe_function(text: str) -> str:
    return text.upper()

def test_log_to_file() -> None:
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    risky_function(10, 2)  # Успешный вызов
    with pytest.raises(ZeroDivisionError):
        risky_function(5, 0)  # Ошибочный вызов

    with open("test_log.txt", "r", encoding="utf-8") as f:
        logs = f.read()
        assert "risky_function ok" in logs
        assert "risky_function error: ZeroDivisionError. Inputs: (5, 0)" in logs

def test_log_to_console(capsys: pytest.CaptureFixture) -> None:
    safe_function("hello")
    captured = capsys.readouterr()
    assert "Результат: 'HELLO'" in captured.out

def test_error_logging() -> None:
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    with pytest.raises(ZeroDivisionError):
        risky_function(1, 0)

    with open("test_log.txt", "r", encoding="utf-8") as f:
        logs = f.read()
        assert "risky_function error: ZeroDivisionError. Inputs: (1, 0)" in logs