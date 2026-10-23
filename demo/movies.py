import BestMatch as bm

movie_list = bm.extract_date_add_year(
    bm.csv_to_dict_list('data/imdb_movies.csv'),
    'date_x'
)


reference = {'year': 1970, 'score': 70}
relevant = bm.find_relevant(reference, movie_list, 100)

fig, ax = bm.plot_best(relevant, reference, ['year', 'score'], 10)
bm.show()
