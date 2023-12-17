import os
import csv
def split_csv(input_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    num_rows = len(data)
    output_folder = 'task1'
    x_file = os.path.join(output_folder, "X.csv")
    y_file = os.path.join(output_folder, "Y.csv")
    