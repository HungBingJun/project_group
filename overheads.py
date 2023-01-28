from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    data_list=[]
    for line in reader:
        data_list.append(line)

# creating list to store filtered data sets
expense_list = []
most_expensive = []
less_expensive = []
def overheads():
    # extracting the numbers column
    for column in range(len(data_list)):
        expense_list.append(float(data_list[column][1]))
    # sort the 2nd column number values in ascending order
    expense_list.sort()

    # matching the number values back to the data list and extracting the first column
    for column in range(len(data_list)):
        # going through each value from data list to match which is the number values
        if float(data_list[column][1]) == expense_list[-1]:
            # if 2nd column of raw data matches the highest value, raw data will be filtered and appended to most expensive
            most_expensive.append(data_list[column])
        else:
            # if 2nd column of raw data does not macth the highest value, raw data will be filtered and appended to less expensive
            less_expensive.append(data_list[column])
    return(f"[HIGHEST OVERHEADS] {most_expensive[0][0].upper()}: {most_expensive[0][1]}")