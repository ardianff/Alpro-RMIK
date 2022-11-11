class Graph(object):
    def __init__(self, graph_dict=None):
  # inalisasi objek grafik
  # jika tidak ada kamus atau tidak ada yang diberikan kamu kosong akan digunakan
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
      # mengembalikan daftar semua tepi simpul
        return self._graph_dict[vertice]
        
    def all_vertices(self):
      # mengembalikan simpul grafik sebagai set
        return set(self._graph_dict.keys())

    def all_edges(self):
      # mengembalikan tepi/edge dari grafik
        return self.__generate_edges()

    def add_vertex(self, vertex):
      # kunci, kosong makan akan ditambahkan sebagai nilai ke kamus
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        # mengasumsi bahwa edge bertipe set, tuple, dan list
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
      # tepi dari simpul grafik
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
      # mencari iterasi dari object
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
      # mengulangi simpul
        return next(self._iter_obj)

    def __str__(self):
      # generate string dari object kita ubah atau cari dari edges dan vertices
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
      
g = { "a" : {"a","c","d","e","h"},
      "b" : {"c"},
      "c" : {"b", "a", "d"},
      "d" : {"a", "c","f"},
      "e" : {"a","f"},
      "f" : {"d","e","g"},
      "g" : {"f"},
      "h" : {"a"}
    }

graph = Graph(g)

for vertice in graph:
    print(f"Tepi dari simpul/Edge {vertice}: ", graph.edges(vertice))

graph.add_edge({"i","j"})

# print("\n")
print("\nSimpul dari graph:")
print(graph.all_vertices())

print("\nEdge dari graph:")
print(graph.all_edges())


# print("Add vertex:")
# graph.add_vertex("z")

# print("Add an edge:")
# graph.add_edge({"a", "d"})

# print("Vertices of graph:")
# print(graph.all_vertices())

# print("Edges of graph:")
# print(graph.all_edges())


# print('Adding an edge {"x","y"} with new vertices:')
# graph.add_edge({"x","y"})
# print("Vertices of graph:")
# print(graph.all_vertices())
# print("Edges of graph:")
# print(graph.all_edges())