import unittest


class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):
    for Node in graph:
        if Node in Node.neighbors:
            raise Exception

        invalid_colours = set()

        for neighbor in Node.neighbors:
            if (neighbor.color is not None):
                invalid_colours.add(neighbor.color)

        for i in range(len(colors)):
            color = colors[i]
            if color not in invalid_colours:
                Node.color = color
                break;
