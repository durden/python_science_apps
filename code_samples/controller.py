#!/usr/bin/env python

"""
Simple app to demonstrate writing an MVC application for oil industry.
"""

import sys

from PyQt4 import QtGui, QtCore
import numpy

import view
import model


class Controller(QtCore.QObject):
    """Controller for sample app"""

    def __init__(self):
        """Setup controller"""

        super(Controller, self).__init__()

        self._main_window = QtGui.QMainWindow()
        self._month_prod_dialog = view.ProductionByMonthDialog(
                                                            self._main_window)
        self._state_prod_dialog = view.StateProductionDialog(self._main_window)

        x_vals, y_vals = model.production_by_month()
        self._month_prod_dialog.loadData(x_vals, y_vals)

        self._filter_ak_dialog = view.FilterAkProductionDialog(
                                                            self._main_window)
        self._filter_ak_dialog.filter_range.connect(self._filter_range)
        self._filter_ak_dialog.filter_max.connect(self._filter_max)
        self._filter_ak_dialog.reset_values.connect(self._reset)

        for st in model.STATES:
            x_vals, y_vals = model.production_by_state(st)
            self._state_prod_dialog.loadData(st, x_vals, y_vals)

            if st == 'ak':
                self._filter_ak_dialog.filter_boundaries(numpy.min(y_vals),
                                                         numpy.max(y_vals))

    def launch(self):
        """Launch controller"""

        self._main_window.setWindowTitle('Sample App')
        self._main_window.setCentralWidget(self._month_prod_dialog)

        self._month_prod_dialog.show()
        self._state_prod_dialog.show()
        self._filter_ak_dialog.show()

    def _get_filter_state_vals(self):
        """Get x/y values for state we are filtering"""

        # Just doing ak here for simplicity
        st = 'ak'
        x_vals, y_vals = model.production_by_state('ak')
        return (st, x_vals, y_vals)

    def _reset(self):
        """Reset AK state values to originals"""

        st, x_vals, y_vals = self._get_filter_state_vals()
        self._state_prod_dialog.loadData(st, x_vals, y_vals)
        self._filter_ak_dialog.filter_boundaries(numpy.min(y_vals),
                                                 numpy.max(y_vals))

    def _filter_max(self, max_val):
        """Filter Ak state max"""

        st, x_vals, y_vals = self._get_filter_state_vals()

        # FIXME: Should sanitize this data in a real application since it comes
        # directly from user...

        # Create true arrays to index with
        filtered_max = y_vals <= max_val

        self._state_prod_dialog.loadData(st, x_vals[filtered_max],
                                         y_vals[filtered_max])

    def _filter_range(self, min_val, max_val):
        """Filter AK state values supplied range"""

        st, x_vals, y_vals = self._get_filter_state_vals()

        # FIXME: Should sanitize this data in a real application since it comes
        # directly from user...

        # Create true arrays to index with
        filtered_max = y_vals <= max_val
        filtered_min = y_vals >= min_val

        filtered_x = numpy.intersect1d(x_vals[filtered_min],
                                       x_vals[filtered_max])
        filtered_y = numpy.intersect1d(y_vals[filtered_min],
                                       y_vals[filtered_max])

        self._state_prod_dialog.loadData(st, filtered_x, filtered_y)

def main():
    """main"""

    # Convert data then we can interface with pytables exclusively
    model.convert_xls_to_hdf5(model.XLS_FILENAME, model.HDF5_FILENAME)

    app = QtGui.QApplication(sys.argv)

    controller = Controller()
    controller.launch()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
