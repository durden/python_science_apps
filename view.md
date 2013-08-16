# View

## PyQt

- Python bindings to Qt toolkit
- Cross-platform
- Includes GUI, network, XML, SQL, etc.
- Pyside for LGPL

# Presenter Notes

- General UI widgets; menubars, toolbars, etc.
- Qt is old and hardened, first release 1992
- PyQt first released around 1998
- Beware of licenses; PySide is LGPL, PyQt is GPL

--------------------------------------------------

# View

## PyQwt

- For science/engineering apps
- Much smaller/faster than matplotlib
- Bad Python docs, use C++ docs

# Presenter Notes

- Stable, but not a lot of dev. activity
- Not compatible with PySide?
- PyQt/PyQwt can feel a bit awkward at times b/c they wrap C++ code with
  automated tools

--------------------------------------------------

# Pyqtgraph

- Possible PyQwt replacement
- Doesn't rely on Qwt
    - Pure python (PyQt/Pyside/numpy)
- 3D
- Fast performance?

# Presenter Notes

- Recommending use of pyqtgraph for future
- Docs claim very fast performance on part with PyQwt
    - Haven't tested myself
- Uses numpy and Qt GraphicsView under hood for performance
