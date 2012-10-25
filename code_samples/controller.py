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

        self._main_window = QtGui.QMainWindow()
        self._month_prod_dialog = view.ProductionByMonthDialog(
                                                            self._main_window)
        self._state_prod_dialog = view.StateProductionDialog(self._main_window)

        x_vals, y_vals = model.production_by_month()
        self._month_prod_dialog.loadData(x_vals, y_vals)

        self._filter_ak_dialog = view.FilterAkProductionDialog(
                                                            self._main_window)
        self._filter_ak_dialog.filter_values.connect(self._filter)

        for st in model.STATES:
            x_vals, y_vals = model.production_by_state(st)
            self._state_prod_dialog.loadData(st, x_vals, y_vals)

            if st == 'ak':
                self._filter_ak_dialog.filterBoundaries(numpy.min(y_vals),
                                                        numpy.max(y_vals))

    def launch(self):
        """Launch controller"""

        self._main_window.setWindowTitle('Sample App')
        self._main_window.setCentralWidget(self._month_prod_dialog)

        self._month_prod_dialog.show()
        self._state_prod_dialog.show()
        self._filter_ak_dialog.show()

    def _filter(self, max_val, min_val):
        """Filter AK state values by max value"""

        import pdb;pdb.set_trace()

        # Just doing ak here for simplicity
        st = 'ak'
        x_vals, y_vals = model.production_by_state(st)

        # FIXME: Should sanitize this data in a real application since it comes
        # directly from user...
        y_vals = y_vals[y_vals <= max_val]
        y_vals = y_vals[y_vals >= min_val]
        self._state_prod_dialog.loadData(st, x_vals, y_vals)

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
