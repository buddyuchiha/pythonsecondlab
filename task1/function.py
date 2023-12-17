import os #библиотека подключена, чтобы файлы выводились в папку 
import csv
def get_csv(input_file):
    """
    Получаем путь к папке, чтобы файлы X.csv и Y.csv записывались в папку и не терялись.
    """
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    num_rows = len(data)
    output_folder = 'task1'
    x_file = os.path.join(output_folder, "X.csv")
    y_file = os.path.join(output_folder, "Y.csv")
def split_csv(input_file):
    get_csv(input_file)
    """
    Разбивает исходный csv файл на файлы X.csv и Y.csv с одинаковым количеством строк.
    Первый файл содержит даты, второй файл содержит данные.
    input_file (str): Путь к исходному csv файлу.
    """
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    num_rows = len(data)
    output_folder = 'task1'
    x_file = os.path.join(output_folder, "X.csv")
    y_file = os.path.join(output_folder, "Y.csv")
    with open(x_file, 'w', newline='') as file_x, open(y_file, 'w', newline='') as file_y:
        writer_x = csv.writer(file_x)
        writer_y = csv.writer(file_y)
        writer_x.writerow([data[0][0]])  
        writer_y.writerow(data[0][1:]) 
        for i in range(1, num_rows):
            writer_x.writerow([data[i][0]])  
            writer_y.writerow(data[i][1:]) 
if __name__ == "__main__":
    input_file = 'task1/dataset.csv'
    split_csv(input_file)