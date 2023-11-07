import random
import numpy
import xml.etree.ElementTree as ET
import os
class GraphUtilities():

    def ReadGraph(self,path_file):
        path_file = fr'{path_file}'
        with open(path_file, 'r') as file:
            vertecies_number = int(file.readline().strip())
            adjacency_matrix = []
            for data in range(vertecies_number):
                row = list(map(int,file.readline().strip().split()))
                adjacency_matrix.append(row)
        return adjacency_matrix

    def ReadGraphsFromIni(self, input_files):
        graphs_table = []
        for file_path in input_files:
            extension = os.path.splitext(file_path)[1]
            if extension == ".txt":
                graph = self.ReadGraph(file_path)
            elif extension == ".xml":
                graph = self.read_tsp_xml(file_path)
            elif extension == ".tsp":
                graph = self.read_tsp_file(file_path)
            else:
                raise ValueError(f"Nieobsługiwane rozszerzenie pliku: {extension}")
            graphs_table.append(graph)

    def PrintGraph(self,graph):
        for i in range(len(graph)):
            print(graph[i])

    def GenerateUndirectedGraph(self,vertecies_number):
        adjacency_matrix = numpy.zeros((vertecies_number,vertecies_number))
        for i in range(vertecies_number):
            for j in range(vertecies_number):
                if(i!=j):
                    weight = int(random.randint(10,99))
                    adjacency_matrix[i][j] = weight
                    adjacency_matrix[j][i] = weight
        return adjacency_matrix

    def GenerateDirectedGraph(self,vertecies_number):
        adjacency_matrix = numpy.zeros((vertecies_number,vertecies_number))
        for i in range(vertecies_number):
            for j in range(vertecies_number):
                if(i!=j):
                    weight = int(random.randint(10,99))
                    adjacency_matrix[i][j] = weight
        return adjacency_matrix

    def save_graph_to_file(self,graph,filename):
        with open(filename, 'w') as file:
            file.write(f"{len(graph)}\n")
            for row in graph:
                row_string = ' '.join(str(int(num)) for num in row)
                file.write(f"{row_string}\n")



    def read_tsp_xml(self,filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        # Ustalamy liczbę wierzchołków na podstawie liczby elementów w tagu <vertex>
        number_of_vertices = len(root.findall(".//vertex"))
        graph = numpy.full((number_of_vertices, number_of_vertices), numpy.inf)

        # Wczytujemy krawędzie
        for vertex in root.findall(".//vertex"):
            id_from = int(vertex.get('id'))
            for edge in vertex.findall('edge'):
                id_to = int(edge.text)
                cost = float(edge.get('cost'))
                graph[id_from][id_to] = cost
                graph[id_to][id_from] = cost  # Graf nieskierowany

        return graph

    def read_tsp_file(self,file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Znajdź linię rozpoczynającą sekcję wag krawędzi
        edge_weight_section_start = lines.index("EDGE_WEIGHT_SECTION\n") + 1
        eof_line_index = lines.index("EOF\n")

        # Przetwórz sekcję wag krawędzi
        edge_weights = []
        for line in lines[edge_weight_section_start:eof_line_index]:
            # Oczyszczamy linię z białych znaków i dzielimy na pojedyncze wartości
            edge_weights.extend([int(weight) for weight in line.strip().split() if weight.isdigit()])

        # Ustalamy liczbę wierzchołków
        dimension_line = [line for line in lines if line.startswith("DIMENSION")][0]
        dimension = int(dimension_line.split(":")[1])

        # Tworzymy macierz sąsiedztwa
        adjacency_matrix = [[0 if i == j else float('inf') for j in range(dimension)] for i in range(dimension)]

        index = 0
        for i in range(dimension):
            for j in range(i + 1):
                if i != j:
                    adjacency_matrix[i][j] = adjacency_matrix[j][i] = edge_weights[index]
                index += 1

        return adjacency_matrix


