import zip_util
import function
import csv

with open("zip_codes_states.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader('zip_codes_states.csv', delimiter=",")
    count = 0
    # Считывание данных из CSV файла

    print(r_file)


