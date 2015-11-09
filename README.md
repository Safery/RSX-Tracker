# Basic Description
RSX Tracker is a pure python script that uses the MatPlotLib module to read GPS data and live update it on a GUI.

# How does it work?
RSX Tracker is unfinished but many of its core component are working. When started RSX tracker will ask for two coordinates (upper right, lower left). These coordinates will help RSX Tracker to create a **‘plane’ space** where users can input the type of **map background**. It is important that the two given coordinates are a square-like shape, due to RSX Tracker design, it is much easier to input the **map background** and move around the tracker.

* **Plane Space** - Plane space is a square like shape where top right and left coordinates are given by user and RSX Tracker implements a square like map where each xy= 0.001 is a new GCS coordinate. This works for a small section (depending on zoom level), but as more plane space is added to the GUI, the less accurate the tracker becomes.
* **Map Background** - Map backgrounds are added after RSX Tracker implements the plane space. These backgrounds may contain satellite images, google map image or anything that can be added.

# How to initiate RSX Tracker?
RSX Tracker can initate after importing the src file and setting its coordinates NOTE: The given coordinate is not real and only to show how it works!
```
From RSX_TrackerV2 import RSX_Mapper
Set_map = RSX_Mapper([00.123,-34.2324], [00.4142123, -41.5325235])
```

After the coordinates were set up, call the set_range method to set up the x/y.
```
Set_map.set_range(auto=True)
```

You can also set up the background image using `set_img()` but that method still needs work done.

# How will RSX Tracker point a GPS Coordinates?
There are two ways RSX Tracker can implement GPS cordinates. There needs to be a method which inputs coordinates from a file or given. These coordinate will be inputted live onto the GUI.

* IF there are no background image:
RSX Tracker can have a method that adds a point on the GUI using `plt.subplots().plot(‘’,’’,.r)`.

* IF there is a background imge:
RSX Tracker can have a method that adds an alpha background image into the map (much like Google red point) using `add_artist()`. Since it is not possible for an image to get put into certain position, user needs to implement `AnnotationBbox()` which gets its .png using `OffsetImage()` this will help the user set up a gps point on the map at certain position (much like Google Map).


## Finished:
* Creating plane space
* creating range for x/y


