# CSV = Comma Separate Values
import csv

def read_csv_data(filename):
    # create an empty list to store rows
    rows = []

    # open the CSV file
    data_file = open(filename, "r")  # permission = r (Read Mode)

    # create a CSV Reader from CSV file -> iterate on the data rows
    reader = csv.reader(data_file)

    # skip the headers (row from CSV file)
    next(reader)

    # add rows from reader to list - use for loop
    for row in reader:
        rows.append(row)  # append row data to rows list

    return rows  # return list that we created


