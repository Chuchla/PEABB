import csv


class IniHandling():


    # def GetFiles(self, file_path):
    #     with open(fr'{file_path}', 'r') as file:
    #         files = file.read().strip().split()
    #     output_file = files.pop()
    #     input_files = []
    #     for file in files:
    #         input, number_of_repetition = file.split(',')
    #         input_files.append((input, int(number_of_repetition)))
    #     return input_files, output_file
    def GetFiles(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.read().strip().split('\n')  # Use splitlines to separate each line
        # Assuming the last line is the output file
        output_file = lines[-1].split(',')[0].strip()  # Extract the output file name

        input_files = []
        for line in lines[:-1]:  # Process all but the last line as input files
            parts = line.split(',')
            input_filename = parts[0].strip()
            number_of_repetition = int(parts[1].strip())
            input_files.append((input_filename, number_of_repetition))
        # Return both the list of input files with repetitions and the output file name
        return input_files, output_file

    def WriteCsv(self, output_file, paths_table, distance_table, time_table, vertices_number_table):
        with open(fr'{output_file}', 'w', newline='') as file:
            field_names = ['Path', 'Distance', 'Time[ms]', 'Size', 'JedenDodatkowyNieWiemCzemu']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for i in range(len(paths_table)):
                writer.writerow({
                    'Path': paths_table[i],
                    'Distance': distance_table[i],
                    'Time[ms]': time_table[i],
                    'Size': vertices_number_table[i]
                })
