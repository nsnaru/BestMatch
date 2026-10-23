###
# BestMatch: Search
###

import numpy as np

# From the Python Standard Library:
import csv
from operator import itemgetter # To sort a list of dictionaries by keys

# Import a CSV file and turn it into a list of dictionaries.
def csv_to_dict_list(location):
    with open(location, newline='') as movies_csv:
        reader = csv.DictReader(movies_csv)
        return list(reader)

# Convert str of format XX/XX/YYYY to int of format YYYY.
def extract_date_add_year(dict_list, column):
    tmp = dict_list.copy()

    for row in tmp:
        row['year'] = int(row[column].split('/')[2])

    return tmp

# Find the best results for a multi-dimensinoal search.
def find_relevant(dict_ref, dict_list_all, top_n):
    keys = list(dict_ref.keys())
    dict_list_tmp = dict_list_all.copy()

    for row in dict_list_tmp:
        p = 0

        # Euclidean distance calc.
        for key in keys:
            p += (dict_ref[key] - float(row[key])) ** 2
        
        p = np.sqrt(p)
        row['prox'] = p

    # Sort list by proximity to reference attributes.
    dict_list_tmp = sorted(dict_list_tmp, key=itemgetter('prox'))  

    # Only return the top top_n results.
    return dict_list_tmp[0:top_n]
