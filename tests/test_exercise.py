import pytest
from src.exercise import smallest

def test_exercise():
    assert smallest(3,2) == 2
    assert smallest(2,7) == 2
