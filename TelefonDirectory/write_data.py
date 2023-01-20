
def get_new_write(data):
    import csv
    with open("telefdirect1.csv", "a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "|", lineterminator="\n")
        file_writer.writerow(list(data))