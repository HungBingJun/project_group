from pathlib import Path
import csv
fp = Path.cwd()/"Project_group"/"csv_reports"/"cash-on-hand-usd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    data_list = []
    for line in reader:
        data_list.append(line)

def cash_on_hand():
    negative = []
    for column in range(1,len(data_list)):
        difference = (float(data_list[column][1]) - float(data_list[column-1][1]))
        if difference < 0:
            negative.extend([data_list[column][0],difference])
        elif difference < 0:
            continue

    if len(negative) == 0:
        print("cash surplus")
    else:
        for values in range(0,len(negative),2):
            print(f"{negative[values]} and {negative[values +1]}")