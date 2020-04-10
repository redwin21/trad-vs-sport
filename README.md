# What type of rock climbing is harder, trad or sport?
There are a myriad of different types of rock climbing, both indoors and outdoors. Among the most popular are trad (short for traditional) and sport climbing.

<!-- <table border="0"><tr>
    <td><img src='images/trad_climber.jpg' align='left' style='width: 500px;'></td>
    <td><img src='images/sport_climber.jpeg' align='right' style='width: 500px;'></td>
</tr></table>

*Trad climber on the left, sport climber on the right. ([source](https://www.powercompanyclimbing.com/blog/2019/4/19/guest-post-chad-volk))* -->

Trad Climber           |  Sport Climber *([source](https://www.powercompanyclimbing.com/blog/2019/4/19/guest-post-chad-volk))*
:-------------------------:|:-------------------------:
![](images/trad_climber.jpg)  |  ![](images/sport_climber.jpeg)

Trad climbing involves placing your own protection as you lead the rope up to the top, and usually involves climbing in a crack where the gear can be placed. Sport climbing is oriented towards climbing on the face of the rock, where bolts are added to clip the rope into as protection. Both of these types of climbing, while very different, are rated on the same difficulty scale. It is a notorious notion in the climbing community that trad climbing is harder than sport climbing. Is this true? Are trad and sport different enough that they should be graded differently? Bouldering, which is another style of rock climbing, has its own difficulty scale, sho why don't trad or sport? This analysis is going to try to shed light on that these questions.

---

## Mountain Project Data

The data for this project was collected from [Mountain Project](https://www.mountainproject.com/), a site designed for climbers to investigate climbing routes and track their climbs. There are thousands of climbers active on the site, with thousands of routes listed. Mountain project provides an [api](https://www.mountainproject.com/data) which provides data in a clean, nested map structure. However, collecting all of the data used in the project was not as simple as running a few api calls. The parameters for the calls are user Ids and route Ids, which are not readily listed. 

A workaround was required to get ahold of these Ids. One function of the api allowed for receiving routes based on geographic coordinates as parameters. This provided a set of routes that included route Ids and the url to each of the route pages. On those pages includes a list of climbers who rated those routes, along with links to their own personal page. I first called the coordinate-based route api and then web-scraped the user Ids from the voters on each of those routes to get a list of user Ids. With those Ids, I could use an api call to get data on all of the routes that those climbers had climbed. And finally, with that data, I could again call the api to get the route information with those route Ids. This data collection process can be seen in more detail on the [Data Collection page](https://github.com/redwin21/trad-vs-sport/tree/master/data_collection).

Due to the process required for collecting the data, only a small subset of the existing data on the site was collected. The primary focus was starting with routes in the Pacific Northwest, acquiring data on the climbers who voted on those routes, and going from there. This resulted in a dataset of about 80,000 routes, 8,000 climbers, and 500,000 climbs.

---

## What's in the data?

There are many types of rock climbing routes, including routes that are combinations of various types. Some of the most popular and distinct types are trad, sport, bouldering, TR (top-rope), alpine, aid, ice, and mixed. Of the data collected, trad, sport and bouldering are the most pupular. The project will focus mainly on these three.

<p align='middle'>
    <td><img src='analysis/images/route_types.png' align='center' style='width: 500px;'></td>
</p>

Currently in the U.S., roped climbing such as trad, sport, and TR are given a difficulty rating on the Yosemite Decimal Scale (YDS).  Bouldering is graded on the Vermin (V) scale. *([source](https://squamishclimbing.com/articles/grade-conversion-chart/))*

<p align='middle'>
    <td><img src='images/grade-convert.jpg' align='center' style='width: 300px;'></td>
</p>

A breakdown of the route ratings collected in the dataset shows that a lot of routes fall in the 5.7 to 5.11 range for rope climbing and V0-V5 for bouldering.

<p align='middle'>
    <td><img src='analysis/images/route_ratings_bar.png' align='center' style='width: 800px;'></td>
</p>

For user in analysis, the ratings were converted to a numerical rating based on the chart provided above. For instance, *5.6* would be 6.0, *5.11b* was given 11.8, *V5* is now 12.0, etc. This allowed for proper comparison and analysis. Distributions of trad, sport, and boulder routes based on their numerical rating can be seen int he following plots. Unfortunately, due to the numeric conversion of the ratings being based on discrete keys, the bin size for these, and all following histograms, have to be rather large so the plots look coarse. 

<p align='middle'>
    <td><img src='analysis/images/route_difficulty.png' align='center' style='width: 800px;'></td>
</p>

We can get an idea of what type of climbing people favor based on the relationship between the routes *"stars"*, on a 0-5 scale, and the number of people who have made those votes, differentiated by type of climbing. It seems like, while more people have climbed sport in this dataset, they tend to rate trad routes higher. It also makes sense that the lower a route is rated, the less people would want to go climb it, menaing it would have less votes.

<p align='middle'>
    <td><img src='analysis/images/route_stars.png' align='center' style='width: 500px;'></td>
</p>

We can see that same perspective from a slightly different angle by looking at how many routes of a certain type a climber has climbed in our dataset. It seems like people tend to climb more sport, which coincides with the data that shows it is more abundant.

<p align='middle'>
    <td><img src='analysis/images/num_climbs.png' align='center' style='width: 500px;'></td>
</p>