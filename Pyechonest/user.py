from pyechonest import catalog
from SET_API_KEY import *

SET_API_KEY()

def user_LH(query):
    return catalog.Catalog(query).get_item_dicts()
