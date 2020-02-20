import csv


def find_year(reader, year):
    for row in reader:
        if len(row) > 4:
            break
    
    if year in row:
        return row.index(year)
    return None


def get_years(reader):
    for row in reader:
        if len(row) > 4:
            break
    years = []
    for year in row[4:-3]:
        if year:
            years.append(year)
    return years


def get_chart_data(country, filename):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            years = get_years(reader)
            rates = get_data(country, reader)
            return years, rates
    except FileNotFoundError:
        print("ERROR file does not exist: " + filename)
        exit()
    


def get_data(country, reader):
    rates = []
    for row in reader:
        if len(row) > 4 and row[0] == country:
            for num in row[4:-3]:
                rates.append(float(num))
    if rates:
        return rates
    else:
        print("Wrong name of the country! Try once again!")
        exit()


def find_min_max(list1, list2):
    maxl1 = max(list1)
    maxl2 = max(list2)
    minl1 = min(list1)
    minl2 = min(list2)
    end_min = min(minl1, minl2)
    end_max = max(maxl1, maxl2)
    return end_min, end_max
