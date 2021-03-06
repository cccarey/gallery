from config import DB

from models import *

def clear():
    DB.query('delete from galleries')
    
def save(model):
    for item in model:
        DB.insert(
            'galleries',
            name=item['name'],
            num_collections=item['num_collections'],
            num_images=item['num_images'],
            cover_thumb=item['cover_thumb'],
            last_update=item['last_update']
        )

def read():
    results = list(DB.select('galleries',order="last_update desc"))
    if len(results) == 0: return None
    return results

