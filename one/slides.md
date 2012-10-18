<!SLIDE bullets>

.notes Links to open for talk:
.notes durden.github.com/pyhou_oil
.notes https://docs.google.com/spreadsheet/ccc?key=0AnUBhQqsJgE5dDlyQTFwWDkxbmtCbFRqUUp2b0x3bHc&hl=en_US&pli=1#gid=2
.notes http://explore.data.gov/Energy-and-Utilities/Monthly-Crude-Oil-Production/nxvx-he4x
.notes http://www.pytables.org/moin/HowToUse#GettingStarted

Python in the Oil and Gas industry
========================

- [http://durden.github.com/pyhou_oil](http://durden.github.com/pyhou_oil)

<!SLIDE>

Luke Lee
========
.notes So who am I and why am I qualified to talk about this?  As most of you
know I was the lonely embedded systems C developer.  I recently got the
opportunity to write Python full time at BBR.  So, Ive only been a a developer
in the Oil/Gas industry for a few months.  This talk is meant to explain what
tools Ive learned in the past few months to start becoming a productive Python
developer in the energy business.

Software Engineer at [Blueback Reservoir](http://www.blueback-reservoir.com/)

Scientific computing/data mining apps in Python

Previously embedded C Developer

Django enthusiast

<!SLIDE>

Goals
=====
Get job in industry with existing Python skills

Sell your boss on Python

<!SLIDE>

Not just technical
========
Get away from computer!

Get into open source!

<!SLIDE>

Blueback Reservoir
========
[http://www.blueback-reservoir.com/](http://www.blueback-reservoir.com/)

Uses Python extensively

John Fuqua - Global Software Services Manager

<!SLIDE>

Overview
========
- Industry problems/applications
- Why Python
- Tools
- Sample app

<!SLIDE smaller>

Industry problems/applications
========
- Get hydrocarbons out of Earth in safe/environmentally way
- Lots of planning/analysis
- Historical data
- Requirements
    - Crunch numbers (big data)
    - Visualize
    - Location data

<!SLIDE incremental smaller>

Why Python
==========
.notes People are solving big problems with Python
.notes Space, Weather, Model molecultes, etc.
.notes This is useful b/c lots of massive computing happens in *nix
.notes environments so good to have same environment for visualzation and
.notes number crunching/batch processing.

- Open source/great tools
- Runs everywhere (Windows/OS X/*nix)
- Scientific community
- Works with other fast languages
    - C/C++/Fortran
- Works with other virtual machines/platforms
    - IronPython/Jython
- Good packaging tool for easy deployment
    - Pyinstaller

<!SLIDE incremental smaller>

Python tools
============
.notes Lets go back to requirements of our app
.notes Esri embraced Python as scripting lang for ArcGIS

- Crunch numbers
    - Numpy, scipy, pytables, HDF5
- Visualize
    - 2/3 D plots (PyQt, PyQwt, Pyside, VTK, mayavi, matplotlib)
- Location
    - Esri (ArcPy/geoprocessing)
    - SGeMS (geostatical modeling)
    - SegyPY (geophysical file format)

<!SLIDE incremental smaller>

Let's build an app!
==========
.notes Ok so we know Python can handle the problem weve outlined.
.notes Lots of choices, So how do we use all that with Python tools?
.notes Lets assume were going to make stand-alone GUI app
.notes Use MVC b/c we're hip and it works

- MVC design pattern
- Django - MVC (or MVT) you've seen before

- Model
    - Sqlite/Django ORM
- View
    - HTML/CSS/Javascript
- Controller
    - Python glue/Django/Flask

<!SLIDE incremental smaller>

Our app
=======
.notes Think back to requirements
.notes Crunch big numbers, visualization
.notes Forget location data for now

- Sample oil data from data.gov

- Model
    - HDF5, PyTables
- View
    - PyQt/PyQwt/Pyside
- Controller
    - Numpy, Scipy

<!SLIDE incremental>

Model
=====
HDF5
----

- Big datasets
- Hierarchial (think filesystem)
- Not relational
- Groups/Datasets

<!SLIDE incremental smaller>

Model
=====
.notes Mostly C, not RDBMS replacement

PyTables
--------

- Read/write HDF5 files
- Massive data sets
    - In-memory optimization
    - 30 columns and 1 million entries using ~ 13 MB
- No concurrency
- Numpy to boost performance (in memory buffers)
- Think ORM for HDF5

<!SLIDE incremental smaller>

View
=====
PyQt/PyQwt
---------
- PyQt
    - Python bindings to Qt toolkit
    - Cross-platform
    - Includes GUI, network, XML, SQL, etc.
- PyQwt
    - Built on PyQt/Qwt for science/engineering apps
    - Much faster than matplotlib
    - Bad Python docs, use C++ docs

<!SLIDE incremental>

Controller
=====
- Numpy
    - Arrays with brains
    - Linear algebra
- Scipy
    - Stats
    - Integration
    - Optimization

<!SLIDE>
Code!
=====

<!SLIDE smaller>

Links
=====
- Code
    - [references](http://www.pinboard.in/u:durden/t:pyhou_oil/)
    - [presentation code](https://github.com/durden/pyhou_oil)
    - [showoff](https://github.com/schacon/showoff)

- Me
    - [@durden20](http://twitter.com/#!/durden20)
    - [http://github.com/durden](http://github.com/durden)
    - [http://www.lukelee.net](http://www.lukelee.net)

- Pycon
    - [hdf5](https://us.pycon.org/2012/schedule/presentation/231/)
    - [pyqt](https://us.pycon.org/2012/schedule/presentation/374/)
    - [matplotlib](https://us.pycon.org/2012/schedule/presentation/238/)
    - [high performance 1](https://us.pycon.org/2012/schedule/presentation/174/)
    - [scikit-learn](https://us.pycon.org/2012/schedule/presentation/195/)
    - [high performance 2](https://us.pycon.org/2012/schedule/presentation/343/)
