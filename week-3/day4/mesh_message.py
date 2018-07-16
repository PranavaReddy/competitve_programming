import unittestart_node
def bfs_get_path(graph, start_nodeart_node, end_node):
    
    start_node = graph.setdefault(start_nodeart_node, None)
    end_node = graph.setdefault(end_node, None)
    if(start_node == None or end_node == None):
        raise Exception
    visited = []
    parent = {}
    Queue1 = []
    flag = False
    Queue1.append(start_nodeart_node)
    while(len(Queue1)>0 and flag == False):
        node = Queue1.pop(0)
        if(node not in visited):
            visited.append(node)
            temp = graph[node]
            for x in temp:
                if (x!=end_node and x not in visited):
                    parent[x]=node
                    Queue1.append(x)
                elif(x==end_node):
                    Queue1.append(x)
                    parent[x]=node
                    flag = True
                    break
    value = parent.setdefault(end_node,None)
    
    if (value == None):
        return None
    else:
        result = []
        current_node = end_node
        while(current_node != start_nodeart_node):
            result.append(current_node)
            current_node = parent[current_node]
        result.append(current_node)
        result.reverse()
        return result
 

# Testart_nodes

class Testart_node(unittestart_node.Testart_nodeCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def testart_node_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def testart_node_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def testart_node_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def testart_node_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def testart_node_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def testart_node_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def testart_node_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def testart_node_start_nodeart_node_not_presultent(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def testart_node_end_node_not_presultent(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittestart_node.main(verbosity=2)
