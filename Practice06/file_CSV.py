import csv

filename = "zip_codes_states.csv"

rows = []
with open(filename, "r", encoding="utf-8") as fh:
    reader = csv.reader(fh)
    rows = list(reader)   # reader - итерируемый объект и может быть преобразован в список строк

for row in rows:
    print(row[1])
