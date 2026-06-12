import pytest
from src.dependency_resolver import DependencyResolver


class TestDependencyResolver():
    def test_dependency_resolver_successful(self):
        assert DependencyResolver.resolve("A") == ["E", "G", "D", "F", "B", "A"]

    def test_dependency_resolver_no_dependency(self):
        assert DependencyResolver.resolve("E") == ["E"]

    def test_dependency_resolver_empty(self):
        assert DependencyResolver.resolve()

if __name__ == '__main__':
   pytest.main()
