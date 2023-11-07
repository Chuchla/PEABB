from queue import PriorityQueue
import math

class TSP():
    def calculate_lower_bound(self,adjacency_matrix, current_path):
        # Obliczanie sumy kosztów pokonanych ścieżek
        lower_bound = sum(adjacency_matrix[current_path[i]][current_path[i + 1]] for i in range(len(current_path) - 1))
        number_of_vertices = len(adjacency_matrix)

        # Dodawanie minimalnych kosztów dojścia do nieodwiedzonych miast
        for current_row in range(number_of_vertices):
            if current_row not in current_path:
                min_edge_cost = min(
                    (adjacency_matrix[current_row][column]
                     for column in range(number_of_vertices)
                     if column != current_row and column not in current_path and adjacency_matrix[current_row][column] > 0),
                    default=0)
                lower_bound += min_edge_cost

        return lower_bound


    def branch_and_bound_tsp(self,adjacency_matrix):
        number_of_vertices = len(adjacency_matrix)
        priority_queue = PriorityQueue()

        # Do kolejki priorytetowej dodajemy koszt scieżki 0 i 0 jako wierzchołek początkowy
        priority_queue.put((0, [0]))

        minimum_length = math.inf
        minimum_path = []

        while not priority_queue.empty():
            # Pobierz aktualna sciezke z najnizszym kosztem
            current_bound, current_path = priority_queue.get()

            # Pomin iteracje dla sciezki gorszej niz aktualna najlepsza
            if current_bound > minimum_length:
                continue

            # Sprawdzenie czy sciezka jest juz sciezka hamiltona
            if len(current_path) == number_of_vertices:
                # Sprawdzenie krawedzi prowadzacej z wierzcholka ostatniego do wierzcholka poczatkowego
                last_edge = adjacency_matrix[current_path[-1]][current_path[0]]
                if last_edge > 0:
                    path_cost = current_bound + last_edge
                    if path_cost < minimum_length:
                        minimum_length = path_cost
                        minimum_path = current_path
                continue

            # Sprawdzanie nieodwiedzonych wierzcholkow
            for vertex in range(number_of_vertices):
                if vertex not in current_path:
                    # Obliczanie nowej granicy z nowym wierzcholkiem w sciezce
                    new_path = current_path + [vertex]
                    new_bound = self.calculate_lower_bound(adjacency_matrix, new_path)
                    # Dodanie nowej sciezki do kolejki jezeli nowa sciezka jest lepsza niz aktualna najlepsza
                    if new_bound < minimum_length:
                        priority_queue.put((new_bound, new_path))


        return minimum_length, minimum_path + [minimum_path[0]]