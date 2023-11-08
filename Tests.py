import Utilities.IniHandling
import Utilities.GraphUtilities
from TSP import TSP
import time

tsp = TSP.TSP()
graph_utilities = Utilities.GraphUtilities.GraphUtilities()
ini_handling = Utilities.IniHandling.IniHandling()

def testFromGivenGraph(graph, repetition_number):
    output_file = input("Podaj nazwe pliku wyjsciowego csv: ")
    graphs = []
    distance_table = []
    path_table = []
    time_table = []
    vertecies_number_table = []
    graphs.append(graph)
    print(f"Graf {len(graph)} wierzcholkow")
    total_time = 0
    for rep in range(repetition_number):
        time1 = time.time_ns()
        minimum_lenght, minimum_path = tsp.branch_and_bound_tsp(graph)
        time2 = time.time_ns()
        time_of_rep = time2 - time1
        print(f"{rep + 1}. {time_of_rep}[ns]")
        total_time += time_of_rep
    total_time /= repetition_number
    total_time /= 1000000
    print(f"Sredni czas {total_time}[ms]")
    time_table.append(total_time)
    distance_table.append(minimum_lenght)
    path_table.append(minimum_path)
    vertecies_number_table.append(len(graph))
    ini_handling.WriteCsv(fr"{output_file}", path_table, distance_table, time_table, vertecies_number_table)
def generateOneTestUndirected(vertecies_number,repetition_number):
    output_file = input("Podaj nazwe pliku wyjsciowego csv: ")
    graphs = []
    distance_table = []
    path_table = []
    time_table = []
    vertecies_number_table = []
    graph = graph_utilities.GenerateUndirectedGraph(vertecies_number)
    graphs.append(graph)
    print(f"Graf {len(graph)} wierzcholkow")
    total_time = 0
    for rep in range(repetition_number):
        time1 = time.time_ns()
        minimum_lenght, minimum_path = tsp.branch_and_bound_tsp(graph)
        time2 = time.time_ns()
        time_of_rep = time2 - time1
        print(f"{rep + 1}. {time_of_rep}[ns]")
        total_time += time_of_rep
    total_time /= repetition_number
    total_time /= 1000000
    print(f"Sredni czas {total_time}[ms]")
    time_table.append(total_time)
    distance_table.append(minimum_lenght)
    path_table.append(minimum_path)
    vertecies_number_table.append(len(graph))
    ini_handling.WriteCsv(fr"{output_file}", path_table, distance_table, time_table, vertecies_number_table)

def generateOneTestDirected(vertecies_number,repetition_number):
    output_file = input("Podaj nazwe pliku wyjsciowego csv: ")
    graphs = []
    distance_table = []
    path_table = []
    time_table = []
    vertecies_number_table = []
    graph = graph_utilities.GenerateDirectedGraph(vertecies_number)
    graphs.append(graph)
    print(f"Graf {len(graph)} wierzcholkow")
    total_time = 0
    for rep in range(repetition_number):
        time1 = time.time_ns()
        minimum_lenght, minimum_path = tsp.branch_and_bound_tsp(graph)
        time2 = time.time_ns()
        time_of_rep = time2 - time1
        print(f"{rep + 1}. {time_of_rep}[ns]")
        total_time += time_of_rep
    total_time /= repetition_number
    total_time /= 1000000
    print(f"Sredni czas {total_time}[ms]")
    time_table.append(total_time)
    distance_table.append(minimum_lenght)
    path_table.append(minimum_path)
    vertecies_number_table.append(len(graph))
    ini_handling.WriteCsv(fr"{output_file}", path_table, distance_table, time_table, vertecies_number_table)
def generateInstancesUndirected(vertecies_number_start,vertecies_number_end, repetition_number):
    #output_file = input("Podaj nazwe pliku wyjsciowego csv: ")
    graphs = []
    distance_table = []
    path_table = []
    time_table = []
    vertecies_number_table = []
    for i in range(vertecies_number_start, vertecies_number_end+1):
        graph = graph_utilities.GenerateUndirectedGraph(i)
        graphs.append(graph)
    for graph in graphs:
        print(f"Graf {len(graph)} wierzcholkow")
        total_time = 0
        graph_utilities.save_graph_to_file(graph,f"graf_nieskierowany_{len(graph)}.txt")
        for rep in range(repetition_number):
            time1 = time.time_ns()
            minimum_lenght, minimum_path = tsp.branch_and_bound_tsp(graph)
            time2 = time.time_ns()
            time_of_rep = time2 - time1
            print(f"{rep+1}. {time_of_rep}[ns]")
            total_time += time_of_rep
        total_time /= repetition_number
        total_time /=1000000
        print(f"Sredni czas {total_time}[ms]")
        time_table.append(total_time)
        distance_table.append(minimum_lenght)
        path_table.append(minimum_path)
        vertecies_number_table.append(len(graph))
    ini_handling.WriteCsv(fr"nieskierowane_od_{vertecies_number_start}_do_{vertecies_number_end}.csv",path_table,distance_table,time_table,vertecies_number_table)

def generateInstancesDirected(vertecies_number_start,vertecies_number_end, repetition_number):
    #output_file = input("Podaj nazwe pliku wyjsciowego csv: ")
    graphs = []
    distance_table = []
    path_table = []
    time_table = []
    vertecies_number_table = []
    for i in range(vertecies_number_start,vertecies_number_end+1):
        graph = graph_utilities.GenerateDirectedGraph(i)
        graphs.append(graph)
    for graph in graphs:
        print(f"Graf {len(graph)} wierzcholkow")
        total_time = 0
        graph_utilities.save_graph_to_file(graph, f"graf_skierowany_{len(graph)}.txt")
        for rep in range(repetition_number):
            time1 = time.time_ns()
            minimum_lenght, minimum_path = tsp.branch_and_bound_tsp(graph)
            time2 = time.time_ns()
            time_of_rep = time2 - time1
            print(f"{rep+1}. {time_of_rep}[ns]")
            total_time += time_of_rep
        total_time /= repetition_number
        total_time /=1000000
        print(f"Sredni czas {total_time}[ms]")
        time_table.append(total_time)
        distance_table.append(minimum_lenght)
        path_table.append(minimum_path)
        vertecies_number_table.append(len(graph))
    ini_handling.WriteCsv(fr"skierowane_od_{vertecies_number_start}_do_{vertecies_number_end}.csv",path_table,distance_table,time_table,vertecies_number_table)

def iniTest():
    distance_table = []
    path_table = []
    time_table = []
    vertecies_number_table = []
    file_path = input("Podaj nazwe pliku ini, z ktorego chcesz zczytać dane: ")
    input_files, output_file = ini_handling.GetFiles(fr'{file_path}')
    graphs = graph_utilities.ReadGraphsFromIni(input_files)
    for graph in graphs:
        print(f"Graf {len(graph[0])} wierzcholkow")
        total_time = 0
        for rep in range(graph[1]):
            time1 = time.time_ns()
            minimum_lenght, minimum_path = tsp.branch_and_bound_tsp(graph[0])
            time2 = time.time_ns()
            time_of_rep = time2 - time1
            print(f"{rep + 1}. {time_of_rep}[ns]")
            total_time += time_of_rep
        total_time /= graph[1]
        total_time /= 1000000
        print(f"Sredni czas {total_time}[ms]")
        time_table.append(total_time)
        distance_table.append(minimum_lenght)
        path_table.append(minimum_path)
        vertecies_number_table.append(len(graph[0]))
    ini_handling.WriteCsv(output_file, path_table, distance_table, time_table, vertecies_number_table)