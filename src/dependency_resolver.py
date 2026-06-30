"""This algorithm is for packages and whether they are installed correctly."""
import json


def load_data(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

def filter_data():
    data = load_data('package.json')
    filtered_dict = {}
    for k in data['packages']:
        filtered_dict.update({k.get('name'): k.get('requires')})
    return filtered_dict

def dfs_graph(graph, start, visited =set()):
    if visited is None:
        visited = set()

    visited.add(start)

    for dependency in reversed(graph.get(start, set())):
        if dependency not in visited:
            visited.add(dependency)
            dfs_graph(graph, dependency, visited)
    return visited

def resolve(start_node):
    """fi"""
    graph = filter_data()
    return dfs_graph(graph, start_node)
