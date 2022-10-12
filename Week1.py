import csv #import csv file

with open('TB_burden_countries_2014-09-29.csv') as f: 
    f_csv = csv.reader(f, delimiter=',', quotechar='"')
    header = next(f_csv)
    col_n = header.index('year')
    total_year = 0
    avg_year = 0
    for i, line in enumerate(f_csv):
        total_year += int(line[col_n])
    avg_year = total_year/i

#count the number of rows in csv file including header
print("Number of rows:", i+2)

#calculate the average year from column "year"
print("The average year is: ", round(avg_year))