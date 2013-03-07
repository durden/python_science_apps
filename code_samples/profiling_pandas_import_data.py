"""
Simple script to create test data file and profile performance of reading a
space separated file into an ordered dict or pandas dataframe.

1. Run default profiling from the commandline:
        - python profiling_pandas_import.py [-d, --rm]

2. Use magic IPython %timeit commands to test more scenarios:
        >>> %timeit file_to_pandas_dataframe(filename)
        >>> %timeit file_to_ordered_dict(filename)

3. Use magic IPython %lprun to profile line by line and see what lines are slow
   in custom implementation (requires line_profiler package and IPython
   extension to be installed:
       - http://pythonhosted.org/line_profiler/
       - http://scikit-learn.org/0.11/developers/performance.html

    >>> from code_samples.profiling_pandas_import import file_to_ordered_dict
    >>> from code_samples.profiling_pandas_import import generate_test_data
    >>> generate_test_data(['a', 'b', 'c'], 1000, 'test.dat')
    >>> %lprun -f file_to_ordered_dict file_to_ordered_dict('test.dat')
"""

import collections
import os
import string
import sys
import tempfile
import timeit

import numpy as np
import pandas as pd


def generate_test_data(column_names, row_count, filename):
    """
    Generate file of random test data of size (row_count, len(column_names))

    column_names - List of column name strings to use as header row
    row_count - Number of rows of data to generate
    filename - Name of file to write test data to
    """

    col_count = len(column_names)
    rand_arr = np.random.rand(row_count, col_count)
    header_line = ' '.join(column_names)
    np.savetxt(filename, rand_arr, delimiter=' ', fmt='%1.5f',
                  header=header_line, comments='')


def file_to_pandas_dataframe(filename):
    """Read space-separated file into a pandas.DataFrame"""
    return pd.read_csv(filename, delim_whitespace=True)


def file_to_ordered_dict(filename):
    """
    Read a space-separated file as a dict of columns, keyed by
    column header where each column (dict value) is a standard python list.
    """

    columns = collections.OrderedDict()

    with open(filename, "r") as file_obj:

        # First line is header of column names
        for colname in file_obj.readline().split():
            columns[colname] = []

        col_keys = columns.keys()

        for line in file_obj:

            # Notice we are omitting any error detection here like verifying
            # that the number of values matches the number of column headers,
            # etc.

            # Break up each line into columns and append to the column that it
            # goes with.  Assuming that each row has a value for each column.
            vals = line.split()
            for colname, val in zip(col_keys, vals):
                columns[colname].append(val)

    return columns


def file_to_numpy_ordered_dict(filename):
    """
    Read a space-separated-value file as a dict of columns, keyed by
    column header where each column (dict value) is a numpy array.
    """

    with open(filename, 'r') as file_obj:
        headers = file_obj.readline().split()

        # unpack=True b/c want data organized as column based arrays, not rows
        arrs = np.loadtxt(file_obj, unpack=True)

    ret_dict = collections.OrderedDict()
    for ii, colname in enumerate(headers):
        ret_dict[colname] = arrs[ii]

    return ret_dict


def run_profile(filename, columns, row_count):
    generate_test_data(columns, row_count, filename)
    filesize_bytes = os.path.getsize(filename)
    filesize_kb = filesize_bytes / 1024.0
    filesize_mb = filesize_kb / 1024.0

    print ('Populated %s with test data, file NOT deleted '
            '(use -d or --rm to remove).' % (filename))

    pandas_time = timeit.timeit('file_to_pandas_dataframe(filename)',
                                setup='from __main__ import file_to_pandas_dataframe, filename',
                                number=100)

    dict_time = timeit.timeit('file_to_ordered_dict(filename)',
                                setup='from __main__ import file_to_ordered_dict, filename',
                                number=100)

    numpy_time = timeit.timeit('file_to_numpy_ordered_dict(filename)',
                                setup='from __main__ import file_to_numpy_ordered_dict, filename',
                                number=100)

    print 'Read with Pandas: %f seconds' % (pandas_time)
    print 'Read with custom OrderedDict: %f seconds' % (dict_time)
    print 'Read with numpy.loadtxt: %f seconds' % (numpy_time)
    print 'File size: %d bytes (%.2f kb, %.2f mb)' % (filesize_bytes,
                                                      filesize_kb,
                                                      filesize_mb)


if __name__ == '__main__':
    # For testing just create a column for each lower case letter in english
    # alphabet
    columns = [char for char in string.lowercase]
    row_count = 1000

    # Don't need the file open.  In order to time things properly we should
    # allow each method to open the file, etc. itself.
    fd, filename = tempfile.mkstemp()
    os.close(fd)

    run_profile(filename, columns, row_count)

    if '-d' in sys.argv or '--rm' in sys.argv:
        os.unlink(filename)
        print 'Test file %s removed' % (filename)
