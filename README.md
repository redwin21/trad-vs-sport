# What type of rock climbing is harder, trad or sport?
There are a myriad of different types of rock climbing, both indoors and outdoors. Among the most popular are trad (short for traditional) and sport climbing.

<table><tr><td><img src='images/trad_climber.jpg' align='left' style='width: 500px;'></td><td><img src='images/sport_climber.jpeg' align='right' style='width: 500px;'></td></tr></table>

*Trad climber on the left, sport climber on the right. ([source](https://www.powercompanyclimbing.com/blog/2019/4/19/guest-post-chad-volk))*

Trad climbing involves placing your own protection as you lead the rope up to the top, and usually involves climbing in a crack where the gear can be placed. Sport climbing is oriented towards climbing on the face of the rock, where bolts are added to clip the rope into as protection. Both of these types of climbing, while very different, are rated on the same difficulty scale. It is a nororious notion in the climbing community that trad climbing is harder than sport climbing. This analysis going to try to shed light on that idea.

---

## Mountain Project Data

The data for this project was collected from [Mountain Project](https://www.mountainproject.com/), a site designed for climbers to investigate climbing routes and track their climbs. There are thousands of climbers active on the site, with thousands of routes listed. Mountain project provides an [api](https://www.mountainproject.com/data) which provides data in a clean, nested map structure. However, collecting all of the data used in the project was not as simple as running a few api calls. The parameters for the calls are user Ids and route Ids, which are not readily listed 