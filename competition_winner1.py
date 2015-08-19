import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Tkinter import *
from tkFileDialog import *            
import time
from random import sample, randrange

# start chrono
start_time = time.time()


# Load csv file
root = Tk()
root.withdraw()
file = askopenfilename()
entries = pd.read_csv(file, delimiter="|", error_bad_lines=False)
total_entries = (len(entries))


# get correct answers
ans1 = raw_input("Correct answer 1? ")
#ans2 = raw_input("Correct answer 2? ")
#ans3 = raw_input("Correct answer 3? ")


# Remove duplicates
duplicated_names = entries[entries.duplicated(['First name', 'Last name'])]
duplicated_names = duplicated_names.ix[:, ['First name', 'Last name', 'Email']].sort(['Last name'])
entries = entries.drop_duplicates(['First name', 'Last name'], take_last=True)
non_duplicate_names = (len(entries))

duplicated_addresses = entries[entries.duplicated(['Address1'])]
duplicated_addresses = duplicated_addresses.ix[:, ['Address1', 'Email']].sort(['Address1'])
#entries = entries.drop_duplicates(['Address1'], take_last=True)
non_duplicate_addresses = (len(entries))


# Find correct answers
correct_answer_1 = entries[entries['Answers'].str.contains(ans1)] 
#correct_answer_2 = correct_answer_1[correct_answer_1['Answers'].str.contains(ans2)]    
#correct_answers = correct_answer_2[correct_answer_2['Answers'].str.contains(ans3)]  
#correct_answers_total = (len(correct_answers))

print("Total number of entries:"), total_entries
print("Total without duplicates:"), non_duplicate_names
# print("Duplicate names were: ")
# print(duplicated_names)
# print("Total number of entries after removing duplicate addresses: ")
# print(non_duplicate_addresses)
print("Total number of correct entries:"), len(correct_answer_1)
#print("Duplicated addresses were: ")
#print(duplicated_addresses)

# create random index
rindex =  np.array(sample(xrange(len(correct_answer_1)), 3))
#print(rindex)

# get 3 random rows from entries
winners = correct_answer_1.ix[rindex]
winners = winners.drop(['Title', 'Answers', 'Favourite brand', 'Source'], axis=1)
print("Winners: ")
print(winners)


# Get stats
countries = entries['Country'].value_counts()
print("Top 10 countries: ")
print(countries[0:10])
cities = entries['City'].str.lower()
cities = cities.value_counts()
print("Top 10 cities: ")
print(cities[0:10])

sources = entries['Source'].value_counts()
print("Top sources: ")
print(sources)
favourite_brands = entries['Favourite brand'].str.lower()
favourite_brands = favourite_brands.value_counts()
favourite_brands = favourite_brands[0:10]
print("Top 10 favourite brands: ")
print(favourite_brands)

# stop chrono
print("%f seconds" % (time.time() - start_time))


