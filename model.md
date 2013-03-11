# Model
## HDF5

- Built for scientific data
- Designed for big data
- Hierarchical format
- Fast parallel/random access
- Portable binary format
- Easy to discover/crawl structure

# Presenter Notes

- Started by a bunch of smart supercomputing guys
    - Version 5 in 1998
- Built on lots of limitations of hdf4
- Lots of compression/chunking available:
    - 30 columns and 1 million entries using ~ 13 MB
- Usable from lots of languages, C/Java/Fortran
- Mostly C, not RDBMS replacement
- Very active despite being

--------------------------------------------------

# Model
## PyTables

- Read/write HDF5 files
- No concurrency
- NumPy to boost performance
- Think ORM for HDF5
- More comprehensive than h5py

# Presenter Notes

- Built for big data
- Not a replacement for relational DB, more like companion
- Tools being aware of NumPy avoids copying to Python datatypes first
- Great community/developer support

--------------------------------------------------

# Model
## PyTables

    !python
    for row in ro.where('pressure > 10'):
        print row['energy'] 
