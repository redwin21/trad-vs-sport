## Data Collection Process

The data collection process involves a series of steps calling Mountain Project's data api as well as web scraping from the site itself.

The Mountain Project api can be found at [https://www.mountainproject.com/data](https://www.mountainproject.com/data).

An access key is required to use the api url's. The key can be acquired by creating a user account with Mountain Project. The key is stored in `trad-vs-sport/data/mp_api_key.txt` (not commited to git).

The idea for the project required having data on various climbing routes as well as a list of the climbers who have climbed them. Acquiring this data required a slightly convoluted path. The api calls allow for requesting route data based on route ids and climber data based on user ids, but Mountain Project does not provide a list of either of those ids. It does, however, have another api call that takes in a longitude and latitude and reports X number of routes within Y distance (X and Y also being parameters). Each route's site contains a list of climbers who have rated it, with their user pages (and ids) linked. 

Given this information, the following steps were taken to acquire the data:

1. The first step in acquiring the data was to run this api call with a list of known climbing locations and their coordinates, acquired from the site's [route guide](https://www.mountainproject.com/route-guide). This location data was put in a simple txt file called `climb_locations.txt`. The data was stored in MongoDB. An example of one of the data entries:

```json
{
            "id": 105806397,
            "name": "The Grand Wall",
            "type": "Trad, Aid",
            "rating": "5.11a A0",
            "stars": 4.9,
            "starVotes": 324,
            "pitches": 9,
            "location": [
                "International",
                "North America",
                "Canada",
                "British Columbia",
                "Squamish",
                "The Chief",
                "Grand Wall Area"
            ],
            "url": "https:\/\/www.mountainproject.com\/route\/105806397\/the-grand-wall",
            "imgSqSmall": "https:\/\/cdn-files.apstatic.com\/climb\/106069105_sqsmall_1558470675.jpg",
            "imgSmall": "https:\/\/cdn-files.apstatic.com\/climb\/106069105_small_1558470675.jpg",
            "imgSmallMed": "https:\/\/cdn-files.apstatic.com\/climb\/106069105_smallMed_1558470675.jpg",
            "imgMedium": "https:\/\/cdn-files.apstatic.com\/climb\/106069105_medium_1558470675.jpg",
            "longitude": -123.148,
            "latitude": 49.6822
        }
```


2. The next step was to extract the url's of each of the routes, which are provided in the data entry for each route. Steps 1 and 2 were accomplished in `initial_get_routes.ipynb`, and the url's were stored in `trad-vs-sport/data/route_urls.txt`.

3. Next, each url was modified to address the "stats" page for the route by including the word `stats` after the word `route` and before the route id in each url, as in:

> https://www.mountainproject.com/route/105806397/the-grand-wall ---> https://www.mountainproject.com/route/stats/105806397/the-grand-wall


4. Each url was visited and the entire site was scraped into MongoDB.

5. Each page, now in MongoDB, was analyzed and the user id from each user url (users who rated the route) was recorded and stored in a text file of unique user ids called `trad-vs-sport/data/user_ids.txt`. Steps 3, 4, and 5 were completed in `scrape_routes_stats_page.ipynb`.

6. Using all of the user ids, the getTicks api was called to get up to 200 of the climbs that each climber has climbed. This data was stored in MongoDB with each entry being a user id. An example of a data entry is:

```json
{
    "user_id": "200527767",
    "ticks": [
            {
                "routeId": 106002151,
                "date": "2019-11-02",
                "pitches": 1,
                "notes": "",
                "style": "TR",
                "leadStyle": "",
                "tickId": 118003759,
                "userStars": -1,
                "userRating": ""
            },
            {
                "routeId": 106241707,
                "date": "2019-11-02",
                "pitches": 1,
                "notes": "",
                "style": "TR",
                "leadStyle": "",
                "tickId": 118003758,
                "userStars": -1,
                "userRating": ""
            }
    }
```

7. The next step was to extract a list of route ids for each of the ticks for each user. This creates the relation between each climber and the routes they have climbed. This route id list is stored in `trad-vs-sport/data/route_ids.txt`. Steps 6 and 7 were completed using `get_user_ticks.ipynb`.

8. The final step was to use the list of route ids to call the api for information on the routes. This was a separate api call than step 1 (using route ids in the api instead of geographic coordinates), but provides data in the same format, completing the data created in step 1. This data was stored in a new MongDB. This step was run using `get_routes.ipynb`.

With the data from steps 7 and 8, the hypothesis testing can take place, so the data collection is complete.