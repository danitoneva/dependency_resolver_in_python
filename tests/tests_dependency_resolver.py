"""Tests for dependency resolver."""
import pytest
from src.dependency_resolver import resolve


class TestDependencyResolver():
    """"This class checks if the packages are installed in the correct order."""
    def test_dependency_resolver_A(self):
        expected = ["E", "G", "D", "F", "B", "A"]
        result = resolve("A")
        assert expected == result

    def test_dependency_resolver_B(self):
        expected = ["F", "B"]
        result = resolve("B")
        assert expected == result
    
    def test_dependency_resolver_C(self):
        expected = ["F", "B", "E", "G", "D", "F", "B", "G", "C"]
        result = resolve("C")
        assert expected == result

    def test_dependency_resolver_D(self):
        expected = ["G", "D"]
        result = resolve("D")
        assert expected == result

    def test_dependency_resolver_E(self):
        expected = ["E"]
        result = resolve("E")
        assert expected == result

    def test_dependency_resolver_F(self):
        expected = ["F"]
        result = resolve("F")
        assert expected == result

    def test_dependency_resolver_G(self):
        expected = ["G"]
        result = resolve("G")
        assert expected == result

    def test_dependency_resolver_H(self):
        expected = ["F", "B", "E", "G", "D", "F", "B", "A", "H"]
        result = resolve("H")
        assert expected == result

    def test_dependency_resolver_I(self):
        expected = ["F", "B", "E", "G", "D", "F", "B", "A", "H", "I"]
        result = resolve("I")
        assert expected == result

if __name__ == '__main__':
   pytest.main()
