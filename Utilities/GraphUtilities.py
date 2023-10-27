import random
import numpy

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

    def IniReadGraph(self,input_files):
        graphs_table = []
        for i in range(len(input_files)):
            graph = self.ReadGraph(input_files[i])
            graphs_table.append(graph)
        return graphs_table

    def PrintGraph(self,graph):
        for i in range(len(graph)):
            print(graph[i])

    def GenerateUndirectedGraph(self,vertecies_number):
        adjacency_matrix = numpy.zeros((vertecies_number,vertecies_number))
        for i in range(vertecies_number):
            for j in range(vertecies_number):
                if(i!=j):
                    weight = random.randint(10,99)
                    adjacency_matrix[i][j] = weight
                    adjacency_matrix[j][i] = weight
        return adjacency_matrix

    def GenerateDirectedGraph(self,vertecies_number):
        adjacency_matrix = numpy.zeros((vertecies_number,vertecies_number))
        for i in range(vertecies_number):
            for j in range(vertecies_number):
                if(i!=j):
                    weight = random.randint(10,99)
                    adjacency_matrix[i][j] = weight
        return adjacency_matrix