# graph = { "a" : {"c"},
#           "b" : {"c", "e"},
#           "c" : {"a", "b", "d", "e"},
#           "d" : {"c"},
#           "e" : {"c", "b"},
#           "f" : {}
#         }

# # Menghasilkan tepi atau edge 
# def generate_edges(graph):
#     edges = []
#     for node in graph:
#         for neighbour in graph[node]:
#             edges.append({node, neighbour})

#     return edges
# # Mencari simpul node yang terisolasi  
# def find_isolated_nodes(graph):
#     """ returns a set of isolated nodes. """
#     isolated = set()
#     for node in graph:
#         if not graph[node]:
#             isolated.add(node)
#     return isolated
# print(generate_edges(graph))
# print("\n",find_isolated_nodes(graph))

 
class Graph(object):
  
    def __init__(self, graph_dict=None):
      # menginisialisasi objek grafik 
      #       Jika tidak ada kamus atau Tidak ada yang diberikan, 
      #       kamus kosong akan digunakan
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        # mengembalikan daftar semua tepi sebuah simpul
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        # mengembalikan simpul grafik sebagai set
        return set(self._graph_dict.keys())

    def all_edges(self):
        # mengembalikan tepi/edge grafik
        return self.__generate_edges()

    def add_vertex(self, vertex):
        # Jika vertex "vertex" tidak ada di 
        #     self._graph_dict, kunci "vertex" dengan 
        #     daftar kosong sebagai nilai ditambahkan ke kamus. 
        #     Jika tidak, tidak ada yang harus dilakukan
        
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        # mengasumsikan bahwa edge bertipe set, tuple atau list
        
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
    #  Metode statis yang menghasilkan tepi dari 
    #         graf "grafik". Tepi direpresentasikan sebagai himpunan 
    #         dengan satu (perulangan kembali ke simpul) atau dua 
    #         simpul 
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        # memungkinkan kita untuk mengulangi simpul
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
      
g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }

graph = Graph(g)

for vertice in graph:
    print(f"Tepi dari simpul/Edge {vertice}: ", graph.edges(vertice))

graph.add_edge({"ab", "fg"})
graph.add_edge({"xyz", "bla"})

print("\n")
print("Simpul dari graph:")
print(graph.all_vertices())

print("Edge dari graph:")
print(graph.all_edges())


print("Add vertex:")
graph.add_vertex("z")

print("Add an edge:")
graph.add_edge({"a", "d"})

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())


print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())