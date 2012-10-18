#!/usr/bin/env python

"""
Convert excel spreadsheet to hdf5 format
"""

import datetime
import time

import xlrd
import tables


HDF5_FILENAME = 'oil_production.h5'
XLS_FILENAME = './sample_data/PET_CRD_CRPDN_ADC_MBBL_M.xls'


class OilProductionByMonth(tables.IsDescription):
    """Data model class for oil production by month"""

    date = tables.Time64Col()
    barrels = tables.Int32Col()


class OilProductionByStateAndMonth(tables.IsDescription):
    """Data model class for oil production by state and month/year"""

    date = tables.Time64Col()
    la_barrels = tables.Int32Col()
    tx_barrels = tables.Int32Col()
    ak_barrels = tables.Int32Col()
    ca_barrels = tables.Int32Col()


class ExcelToHdf5(object):
    """Create hdf5 file from excel workbook"""

    def __init__(self, xls_filename, hdf5_filename, supported_sheets=None):
        """Convert given filename to hdf5"""

        self.xls_filename = xls_filename
        self.hdf5_filename = hdf5_filename

        self.workbook = None
        self.hdf5_file = None

        # Sheet indexes we support
        if supported_sheets is None:
            self.supported_sheets = [1, 2]

        # Table for each sheet in xls file
        self.tables = []

    def load_xls_data(self):
        """Load data from given xls filename"""

        self.workbook = xlrd.open_workbook(filename=self.xls_filename)

    def create_hdf5_file(self):
        """Create hdf5 file with given filename, return file and table"""

        # Open a file in "w"rite mode
        self.hdf5_file = tables.openFile(self.hdf5_filename, mode="w",
                                                title="Oil Production by Year")

        # Create a new group under "/" (root)
        group = self.hdf5_file.createGroup("/", 'data', 'Production by Year')

        for sheet_idx in self.supported_sheets:
            if sheet_idx == 1:
                table = self.hdf5_file.createTable(group,
                                                        'production_by_month',
                                                        OilProductionByMonth,
                                                        "Oil Production")
            elif sheet_idx == 2:
                table = self.hdf5_file.createTable(group,
                                                'production_by_state_month',
                                                OilProductionByStateAndMonth,
                                                "Oil Production")
            else:
                raise Exception("Unsupported sheet index %d" % sheet_idx)

            self.tables.append(table)

    def convert_xldate_to_timestamp(self, xldate, data_book):
        """Convert an xldate tuple (from xlrd.xldate_as_tuple) to timestamp"""

        xldate = xlrd.xldate_as_tuple(xldate, data_book.datemode)
        date = datetime.date(xldate[0], xldate[1], xldate[2])
        return time.mktime(date.timetuple())

    def _convert_overall_usa_sheet(self, data_sheet, hdf5_row):
        """
        Convert sheet of data that only contains a month/year and barrels for
        entire usa
        """

        for row in xrange(3, data_sheet.nrows):
            values = data_sheet.row_values(row)[:2]
            hdf5_row['date'] = self.convert_xldate_to_timestamp(values[0],
                                                                self.workbook)
            hdf5_row['barrels'] = values[1]
            hdf5_row.append()

    def _convert_state_sheet(self, data_sheet, hdf5_row):
        """
        Convert sheet of data that contains a month/year and barrels by state
        """

        for row_idx in xrange(3, data_sheet.nrows):
            row = data_sheet.row_values(row_idx)
            hdf5_row['date'] = self.convert_xldate_to_timestamp(row[0],
                                                                self.workbook)
            # Ignore first column b/c it's aggregate value for all states
            hdf5_row['la_barrels'] = row[2]
            hdf5_row['tx_barrels'] = row[3]
            hdf5_row['ak_barrels'] = row[4]
            hdf5_row['ca_barrels'] = row[5]
            hdf5_row.append()

    def populate_hdf5(self, sheet_idx, hdf5_table):
        """Populate given hdf5 table with given data"""

        data_sheet = self.workbook.sheet_by_index(sheet_idx)
        if sheet_idx == 1:
            self._convert_overall_usa_sheet(data_sheet, hdf5_table.row)
        elif sheet_idx == 2:
            self._convert_state_sheet(data_sheet, hdf5_table.row)

        else:
            raise Exception("Unsupported sheet index %d" % sheet_idx)

    def convert(self):
        """Convert excel sheet to hdf5 file"""

        self.load_xls_data()
        self.create_hdf5_file()

        for sheet_idx, table in zip(self.supported_sheets, self.tables):
            self.populate_hdf5(sheet_idx, table)

        self.hdf5_file.close()


def convert_xls_to_hdf5(xls_filename, hdf5_filename):
    """Convert given xls data to hdf5"""

    converter = ExcelToHdf5(xls_filename, hdf5_filename)
    converter.convert()


if __name__ == "__main__":
    convert_xls_to_hdf5(XLS_FILENAME, HDF5_FILENAME)
