import os
import csv
def write_to_file(file_name, data):
    """
    Записывает данные в отдельный файл.
    """
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
def split_csv(input_file):
    """
    Разбивает исходный csv файл на N файлов, где каждый отдельный файл будет соответствовать одному году.
    Записывает файлы в папку task2.
    """
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    years = set()
    for row in data:
        date = row[0].split('-')[0]
        years.add(date)
    output_folder = 'task2'
    for year in years:
        new_file_name = os.path.join(output_folder, f'{year}0101_{year}1231.csv')
        filtered_data = [row for row in data if row[0].startswith(year)]
        write_to_file(new_file_name, filtered_data)