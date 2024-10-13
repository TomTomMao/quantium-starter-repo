import csv

# read csv and put them into data
data = []
for i in range(3):
    with open(f"./data/daily_sales_data_{i}.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t {row[2]} {row[0]}s sold at {row[4]} with {row[1]} on {row[3]}')
                line_count += 1
                data.append(row)
print(len(data))

# write data into output.csv\
with open("./data/output.csv", mode='w', newline='') as csv_file:
    fieldnames = ['Sales', 'Date', 'Region']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        price = float(row[1][1:])
        quantity = float(row[2])
        sales = price * quantity
        date = row[3]
        region = row[4]
        if row[0] == 'pink morsel':
            writer.writerow({'Sales': sales, 'Date': date, 'Region': region})
