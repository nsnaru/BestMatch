import BestMatch as bm

# Convert CSV file detailing diamonds into a list of dictionaries.
diamond_list = bm.csv_to_dict_list('data/diamonds.csv')

# Define a search term.
reference = {'depth': 62, 'price': 365}

# Return top 100 search results.
relevant = bm.find_relevant(reference, diamond_list, 100)

# Plot the reference point and the top 100 search results, highlighting the top 10.
fig, ax = bm.plot_best(relevant, reference, ['depth', 'price'], 10)
bm.show()
