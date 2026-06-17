"""This algorithm is for packages and wheter they are installed correctly."""
import json 


def load_data(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

def filter_data():
    data = load_data('package.json')
    transformed = {data['name']: data['requires']}
    return transformed 
    
def dfs_graph(graph, start, visited = None):
    if visited is None:
        visited = set()

    visited.add(start)

    for dependency in reversed(graph.get(start, [])):
        if dependency not in visited:
            dfs_graph(graph, dependency, visited)    
    
    return visited     

def resolve(start_node):
    graph = filter_data()
    return dfs_graph(graph, start_node)
