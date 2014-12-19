from pyechonest import artist
from SET_KEY import *

SET_API_KEY()

def artist_similar(query):
    return artist.Artist(query)
