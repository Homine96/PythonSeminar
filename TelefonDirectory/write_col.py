import csv
with open("telefdirect1.csv", mode="w", encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter = "|", lineterminator="\r")
    file_writer.writerow(["ID", "Name", "Surname", 'Number', 'Comment'])