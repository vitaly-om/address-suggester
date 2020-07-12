from typing import Optional
from fastapi import FastAPI

from suggester.version import VERSION



"""
Address schema:
Region > Subregion > Locality (city, town, country) > Street > Numbers 
+ Postal Index
"""

app = FastAPI()


@app.get('/')
def index():
    """
    HealthCheck

    Returns application runtime info
    """
    return {'app_version': VERSION}


@app.get('/region')
def search_region(region_query: str):
    return {'result': 'ok', 'query': region_query}


@app.get('/subregion')
def search_subregion(subregion_query: str):
    return {'result': 'ok', 'query': subregion_query}


@app.get('/locality')
def search_locality(locality_query: str, region_id: Optional[str] = None):
    """
    Searching city, town, country, etc.
    """
    return {'result': 'ok', 'query': locality_query}


@app.get('/post_index')
def search_post_index(post_index_query: str):
    return {'result': 'ok', 'query': post_index_query}


@app.get('/street')
def search_street(street_query: str, locality_id: Optional[str] = None):
    return {'result': 'ok', 'query': street_query}


@app.get('/search')
def search(full_address_query: str):
    """
    Searching by full address
    """
    return {'result': 'ok', 'query': full_address_query}
