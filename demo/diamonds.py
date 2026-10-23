import BestMatch as bm

diamond_list = bm.csv_to_dict_list('data/diamonds.csv')

reference = {'depth': 62, 'price': 370}
relevant = bm.find_relevant(reference, diamond_list, 100)

fig, ax = bm.plot_best(relevant, reference, ['depth', 'price'], 10)
bm.show()
