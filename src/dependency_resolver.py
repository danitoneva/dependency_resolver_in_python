"""This algorithm is for packages and wheter they are installed correctly."""
import json 


class DependencyResolver:
    """This class if for the correct installation of the packages."""
    @staticmethod
    def load_data():
        with open('package.json', 'r') as file:
            data = json.load(file)
        return data
    
    def dfs_graph(node, graph, visited, result):
        if node in visited:
            return 
        visited.add(node)

        for dependency in reversed(graph.get(node, [])):
            DependencyResolver.dfs_graph(dependency, graph, visited, result)
        result.append(node)

    def resolve(start_node):
        graph = DependencyResolver.load_data()
        visited = set()
        result = []

        DependencyResolver.dfs_graph(start_node, graph, visited, result)
        return result