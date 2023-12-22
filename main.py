from src.gmaps import Gmaps

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = [
   "Movenpick Ambassador Hotel Accra"
]

Gmaps.places(queries, scrape_reviews=True, reviews_max= Gmaps.ALL_REVIEWS)