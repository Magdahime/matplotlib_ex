import csv
import help_functions as hp
import matplotlib.pyplot as plt 
import numpy as np

d_filename = input("CSV file with death rates: ")
b_filename = input("CSV file with birth rates: ")
country = input("Enter the name of the country, you are interested in: ")

years, death_rates = hp.get_chart_data(country, d_filename)
years, birth_rates = hp.get_chart_data(country, b_filename)
lmin, lmax = hp.find_min_max(death_rates, birth_rates)
    
plt.style.use('seaborn')
fig = plt.figure(dpi=128, figsize=(20, 10))
plt.xticks(np.arange(int(years[-1]), step=2))
plt.ylim(auto=True)

plt.plot(years, death_rates, c='purple', linewidth=2.0, label='deaths')
plt.plot(years, birth_rates, c='red', linewidth=2.0, label='births')
plt.legend()

plt.title("Death and birth rate per 1,000 people in " + country, fontsize=24)
plt.xlabel('Years', fontsize=20)
fig.autofmt_xdate()
plt.ylabel('', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=14)

save_filename = input("How would you like to name your chart?: ")
plt.savefig('output/' + save_filename, bbox_inches='tight')
