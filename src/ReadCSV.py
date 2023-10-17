import csv


def ReadCSV(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
