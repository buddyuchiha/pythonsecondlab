import os #библиотека подключена, чтобы файлы выводились в папку 
import csv
current_path = os.getcwd()
task1_path = os.path.join(current_path, "task1")
input_file = os.path.join(current_path, "task1/dataset.csv")
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
num_rows = len(data)
x_file = os.path.join(task1_path, "X.csv")
y_file = os.path.join(task1_path, "Y.csv")
with open(x_file, 'w', newline='') as file_x, open(y_file, 'w', newline='') as file_y:
    writer_x = csv.writer(file_x)
    writer_y = csv.writer(file_y)
    writer_x.writerow([data[0][0]])  
    writer_y.writerow(data[0][1:])  
    for i in range(1, num_rows):
        writer_x.writerow([data[i][0]])  
        writer_y.writerow(data[i][1:])  
