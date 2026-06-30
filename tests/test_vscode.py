"""Tests for dependency resolver."""
import pytest
from src.dependency_resolver import resolve


class TestDependencyResolver():
    """"This class checks if the packages are installed in the correct order."""
    def test_dependency_resolver_A(self):
        expected = ["E", "G", "D", "F", "B", "A"]
        result = resolve("A")
        assert expected == result

if __name__ == '__main__':
   pytest.main()
