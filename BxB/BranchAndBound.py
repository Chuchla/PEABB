from collections import defaultdict


class BranchAndBound():
    def GreedyMethod(self, graph):
        path = []
        distance = 0
        current_vertex = 0
        visited_vertecies = [False] * len(graph)
        visited_vertecies[current_vertex] = True
        path.append(current_vertex)
        for i in range(len(graph) - 1):
            nearest_vertex = None
            min_distance = float('inf')
            for neighbour in range(len(graph)):
                if visited_vertecies[neighbour] != True and min_distance > graph[current_vertex][neighbour] != 0 :
                    nearest_vertex = neighbour
                    min_distance = graph[current_vertex][nearest_vertex]
            path.append(nearest_vertex)
            distance += min_distance
            visited_vertecies[nearest_vertex] = True
            current_vertex = nearest_vertex
        path.append(path[0])
        distance += graph[current_vertex][0]
        return path, distance
    def BranchAndBound(self,graph):
        greedy_path, upper_bound = self.GreedyMethod(graph)
