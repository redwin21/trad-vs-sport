from pymongo import MongoClient
import json, re, requests, urllib
from bs4 import BeautifulSoup

# this class runs api calls of the Mountain Project api
class MP:

    # initialize the class with an api key and a mongo client
    def __init__(self, key, client, db, collection):
        self.key = key
        self.client = client
        self.db = self.client[db]
        self.collection = self.db[collection]


    # return an HTML of routes
    def api_get_routes_lat_long(self, region, lat, lon, dist=50, num_routes=500):

        # inputs: latitude, longitude, max distance (max is 50), number of routes (max is 500)

        api_url = f'https://www.mountainproject.com/data/get-routes-for-lat-lon?lat={lat}&lon={lon}&maxDistance={dist}&minDiff=5.1&maxDiff=5.15&maxResults={num_routes}&key={self.key}'
        
        response = urllib.request.urlopen(api_url)
        data = json.load(response)
        self.collection.insert_one({'region':region, 'data': data['routes']})




    def api_get_routes(self, routes):

        # inputs: list of route ids

        api_url = f'''https://www.mountainproject.com/data/
                    get-routes?
                    routeIds={','.join(list(routes))}
                    &key={self.key}
                    '''
        pass

    def api_get_climbers(self, user):

        # inputs: user id

        api_url = f'''https://www.mountainproject.com/data/
                    get-ticks?
                    userId={user}
                    &key={self.key}
                    '''
        pass