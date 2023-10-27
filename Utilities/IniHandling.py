import csv

class IniHandling():

    def ReadIni(self,file_path):
        with open(fr'{file_path}','r') as file:
            files = file.read().strip().split()
        output_file = files.pop()
        input_files = []
        for file in files:
             input, number_of_repetition = file.split(',')
             input_files.append((input,int(number_of_repetition)))
        return input_files, output_file

    def WriteCsv(self,output_file, paths_table, distance_table, time_table, vertecies_number_table):
        with open(fr'{output_file}', 'w', newline='') as file:
            field_names = ['Path', 'Distance', 'Time[ns]', 'Size']
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            for i in range(len(paths_table)):
                writer.writerow({
                    'Path': paths_table[i],
                    'Distance': distance_table[i],
                    'Time[ns]': time_table[i],
                    'Size': vertecies_number_table[i]
                })
