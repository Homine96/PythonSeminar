def get_write_data():
    import csv
    with open("telefdirect1.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "|", lineterminator="\r")
        file_writer.writerow(["ID", "Name", "Surname", 'Number', 'Comment'])


def get_new_write(data):
    import csv
    with open("telefdirect1.csv", "a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "|", lineterminator="\n")
        file_writer.writerow(list(data))

def check_row1():
    import os
    isempty=os.stat('telefdirect1.csv').st_size
    if isempty == 0:
        get_write_data()