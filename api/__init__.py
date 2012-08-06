import json, time, datetime, decimal, fractions
from config import *

def set_headers(allow_cache=False):
    web.header('Content-Type', 'application/json')
    if not allow_cache:
        web.header('Cache-Control', 'no-store, no-cache, must-revalidate')
        web.header('Cache-Control', 'post-check=0, pre-check=0', False)
    web.header('Pragma', 'no-cache')
    
def set_to_list(theSet):
    listresults = []    
    for item in theSet:
        listresults.append(item_to_dict(item))
    return listresults
    
def iterBetter_to_JSON(iterbetter):
    return json.dumps(set_to_list(iterbetter))

def item_to_JSON(item):
    listresults = []
    listresults.append(item_to_dict(item))
    return json.dumps(listresults)
    
def serializable_value(value):
    if isinstance(value, datetime.datetime):
        return "%s" % value
    if isinstance(value, set):
        return set_to_list(value)
    if isinstance(value, decimal.Decimal) or isinstance(value, fractions.Fraction):
        return "%f" % value
    return value
    
def item_to_dict(item):
    dictitem = dict()
    for key in item.keys():
        dictitem[key] = serializable_value(item.get(key))
    return dictitem
