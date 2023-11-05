import Utilities.IniHandling
import Utilities.GraphUtilities
import BxB.BranchAndBound

graph_utilities = Utilities.GraphUtilities.GraphUtilities()
ini_handling = Utilities.IniHandling.IniHandling()
bxb = BxB.BranchAndBound.BranchAndBound()
input_files, output_file = ini_handling.GetFiles('dane.ini')



graph = graph_utilities.ReadGraphsFromIni(input_files)

graph_utilities.PrintGraph(graph[0])
path = bxb.GreedyMethod(graph[0])
print(path)

