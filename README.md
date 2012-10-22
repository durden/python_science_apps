# Building full-stack scientific applications in Python

## Brief outline:

Python has a large collection of tools for scientific computing.  However,
finding the right pieces and assembling them into a fast and scale-able app can
be a daunting task.  This talk will explore common requirements of scientific
apps and how to fulfill those from the Python ecosystem.  It will also provide
a blueprint for building applications using tools like PyQt, PyQwt, numpy, and
HDF5.

## Detailed abstract

Python is a common tool for serious scientists of all disciplines. However,
many people outside the scientific and Python communities still fail to see
Python's potential in the world of scientific computing.  This talk will
provide you with the background for starting to prototype your own scientific
applications and showing Python doubters the potential power of the ecosystem.

This talk will give a few solid reasons for considering Python for a high
performance scientific application.  For example, many novices don't
know that Python plays very nicely with many accepted 'fast' languages such
as C and Fortran.  Both of these languages are considered cornerstones of the
scientific computing world and by interfacing with them Python can instantly
tap into fast, robust libraries.

In fact, the SciPy package is built directly on top of some very robust Fortran
and C libraries.  So not all of your number crunching needs to be in Python.
You can use Python to prototype quickly and build infrastructure while still
utilizing these faster languages for some of the heavy duty work.

Another benefit of using Python is easy access to lots of open source GUI and
plotting libraries such as PyQt, matplotlib, and PyQwt.  These projects allow
you to easily visualize your data so you can spent more time reasoning about
the cutting-edge data instead of plotting it.  In addition, all of these
projects are cross-platform so your users can be comfortable in their own
computing environments.

However, just knowing some of the tools available only gets you so far.  So
this talk will also explain how to use these tools to piece together a typical
MVC (Model-View-Controller) application.  So, you'll see how you can store
massive amounts of data on disk with the fast HDF5 binary format, manipulate
that data easily in memory with the numpy, and then use the PyQwt plotting
tools to quickly display nice customizable graphs.

### Requirements

The presentation requires [landslide](https://github.com/adamzap/landslide)
to view.  This can be installed via pip and the included `requirements.txt`
file (`pip install -r requirements.txt`).

The code samples require the following libraries.  However, there is no
provided requirements file because these require C-extentions, etc.  Please see
the associated websites for information about installing on your platform.

- [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro)
- [PyTables](http://pytables.github.com/)
- [PyQwt](http://pyqwt.sourceforge.net/)
- [xlrd](http://pypi.python.org/pypi/xlrd)
- [numpy](http://numpy.scipy.org/)

### Live

You can view a live version of the presentation
[here](http://durden.github.com/python_science_apps).
