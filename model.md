# Model
## HDF5

- Hierarchical format
- Designed for big data
    - 30 columns and 1 million entries using ~ 13 MB
- Fast parallel/random/sequential access
- Portable format
- Easy to discover/crawl structure

# Presenter Notes

- Usable from lots of languages, C/Java/etc.
- Mostly C, not RDBMS replacement

--------------------------------------------------

# Model
## PyTables

- Read/write HDF5 files
- No concurrency
- NumPy to boost performance (in memory buffers)
- Think ORM for HDF5

# Presenter Notes

- Built for big data
- Not a replacement for relational DB, more like companion
- Great community/developer support
- Read NumPy or Python lists

--------------------------------------------------

# Model
## PyTables

    !python
    for row in ro.where('pressure > 10'):
        print row['energy'] 
