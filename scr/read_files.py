import csv


def read_lexica(file_path):
    with open(file_path, 'r', encoding='utf8', errors="ignore") as f_input:
        csv_input = csv.reader(f_input, delimiter='\t', skipinitialspace=True)
        csv_output = []
        for cols in csv_input:
            csv_output.append((cols[0], float(cols[1])))

    return csv_output


def read_tsv(file_path):
    with open(file_path, 'r', encoding='utf8', errors="ignore") as f_input:
        csv_input = csv.reader(f_input, delimiter='\t', skipinitialspace=True)
        csv_output = []
        for cols in csv_input:
            csv_output.append([cols[2], cols[3]])

    return csv_output
