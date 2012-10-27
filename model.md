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
- Numpy to boost performance (in memory buffers)
- Think ORM for HDF5
- [Example](https://github.com/durden/python_science_apps/blob/master/code_samples/model.py#L154)

# Presenter Notes

- Great community/developer support
- Read numpy or Python lists
