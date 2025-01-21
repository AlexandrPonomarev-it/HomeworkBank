
from src.decorators import my_function


def test_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_decorator(capsys):
    my_function(1, '2')
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1, '2'), {}\n"

