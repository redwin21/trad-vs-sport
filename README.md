# What type of rock climbing is harder, trad or sport?
There are a myriad of different types of rock climbing, both indoors and outdoors. Among the most popular are trad (short for traditional) and sport climbing.

<table border="0"><tr>
    <td><img src='images/trad_climber.jpg' align='left' style='width: 500px;'></td>
    <td><img src='images/sport_climber.jpeg' align='right' style='width: 500px;'></td>
</tr></table>

*Trad climber on the left, sport climber on the right. ([source](https://www.powercompanyclimbing.com/blog/2019/4/19/guest-post-chad-volk))*

Trad climbing involves placing your own protection as you lead the rope up to the top, and usually involves climbing in a crack where the gear can be placed. Sport climbing is oriented towards climbing on the face of the rock, where bolts are added to clip the rope into as protection. Both of these types of climbing, while very different, are rated on the same difficulty scale. It is a notorious notion in the climbing community that trad climbing is harder than sport climbing. Is this true? Are trad and sport different enough that they should be graded differently? Bouldering, which is another style of rock climbing, has its own difficulty scale, sho why don't trad or sport? This analysis is going to try to shed light on that these questions.

---

## Mountain Project Data

The data for this project was collected from [Mountain Project](https://www.mountainproject.com/), a site designed for climbers to investigate climbing routes and track their climbs. There are thousands of climbers active on the site, with thousands of routes listed. Mountain project provides an [api](https://www.mountainproject.com/data) which provides data in a clean, nested map structure. However, collecting all of the data used in the project was not as simple as running a few api calls. The parameters for the calls are user Ids and route Ids, which are not readily listed. 

A workaround was required to get ahold of these Ids. One function of the api allowed for receiving routes based on geographic coordinates as parameters. This provided a set of routes that included route Ids and the url to each of the route pages. On those pages includes a list of climbers who rated those routes, along with links to their own personal page. I first called the coordinate-based route api and then web-scraped the user Ids from the voters on each of those routes to get a list of user Ids. With those Ids, I could use an api call to get data on all of the routes that those climbers had climbed. And finally, with that data, I could again call the api to get the route information with those route Ids. This data collection process can be seen in more detail on the [Data Collection page](https://github.com/redwin21/trad-vs-sport/tree/master/data_collection).

Due to the process required for collecting the data, only a small subset of the existing data on the site was collected. The primary focus was starting with routes in the Pacific Northwest, acquiring data on the climbers who voted on those routes, and going from there. This resulted in a dataset of about 80,000 routes, 8,000 climbers, and 500,000 climbs.

---

## Exploratory Data Analysis

There are many types of rock climbing routes, including routes that are combinations of various types. Some of the most popular and distinct types are trad, sport, bouldering, TR (top-rope), alpine, aid, ice, and mixed. Of the data collected, trad, sport and bouldering are the most pupular. The project will focus mainly on these three.

<table border="0"><tr>
    <td><img src='analysis/images/route_types.png' align='center' style='width: 500px;'></td>
</tr></table>

