import Utilities.IniHandling
import Utilities.GraphUtilities

graph_utilities = Utilities.GraphUtilities.GraphUtilities()
ini_handling = Utilities.IniHandling.IniHandling()

input_files, output_file = ini_handling.ReadIni('dane.ini')
print(input_files)
print(output_file)