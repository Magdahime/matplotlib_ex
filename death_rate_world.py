import csv

import help_functions as hp
from country_codes import get_country_code

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS , RotateStyle as RS

filename = input("Enter the name of csv data file: ")
year = input("Enter the year from which you want your data to be processed: ")
data_dict = {}
try:
    with open(filename) as file:
        reader = csv.reader(file)
        index = hp.find_year(reader, year)
        for row in reader:
            country_name = row[0]
            death_rate = row[index]
            country_code = get_country_code(country_name)
            if country_code and death_rate:
                data_dict[country_code] = int(float(death_rate))              
except FileNotFoundError:
    print("ERROR incorrect file name  : " + filename)
    
#DIVISION INTO THREE GROUPS   
low, average, high = {}, {}, {}
for country, deaths in data_dict.items():
    if deaths < 10:
        low[country] = deaths
    if deaths >10 and deaths < 20:
        average[country] = deaths
    if deaths >20:
        high[country] = deaths
        
#CREATING CHART
wm_style = RS('#cd823f', base_style=LCS)
wm = World(style = wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Death rate per 1000 people in ' + year
wm.add("Less than 10 people", low)
wm.add("More than 10 people and less than 20", average)
wm.add("20 and more", high)
save_filename = input("Enter new name of the chart: ")
wm.render_to_file(save_filename)
