def get_output_data():
    import csv
    with open('telefdirect1.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|', quoting=csv.QUOTE_NONE)
        for row in reader:
            print('| '.join(row))

def get_output_name():
    import csv
    with open('telefdirect1.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|', quoting=csv.QUOTE_NONE)
        for row in reader:
            print('| '.join(row[1:3]))