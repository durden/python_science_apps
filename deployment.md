# Deployment

- pip/requirements.txt
- PyInstaller
- py2exe

# Presenter notes

- Too many choices
- pip is easy but could be tricky b/c end-users in my area don't like to get
  into the command line and install tools
- Tough b/c users can always ugrade their own stuff and break things

--------------------------------------------------

# PyInstaller

- Package app into nice executable
- Finds your dependencies automatically
- Explicit support for PyQt/Django/matplotlib
- Major improvements in Pyinstaller 2.x
- Customizable with hooks

# Presenter notes

- Hook architecture to package in support for a custom app if needed 

--------------------------------------------------

# PyInstaller pitfalls

- Beware of
    - dynamic imports
    - sys.path mods
- No cross-compiles
[http://www.pyinstaller.org/wiki/SupportedPackages](http://www.pyinstaller.org/wiki/SupportedPackages)

# Presenter notes

- Can use hooks to tell about dynamic imports/sys.path issues
- pyqtgraph is big offender of dynamic imports
- Tries to dynamically import everything into single namespace for convience
  but turns out to be a huge pain
- Pyinstaller doesn't see dynamic imports
