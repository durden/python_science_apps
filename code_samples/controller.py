"""
Controller for sample app
"""

from PyQt4 import QtCore
import PyQt4.Qwt5 as Qwt

import tables

import view
import model


def plot_production_by_month():
    """Show data in qwt plot"""

    plot = Qwt.QwtPlot()
    plot.setTitle("Oil Production for USA by Month")
    plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
    plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")

    # Need custom scale to set labels to month/year
    plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, view.TimeScaleDraw())

    hdf5 = tables.openFile(model.HDF5_FILENAME)
    x_vals = []
    y_vals = []

    for row in hdf5.root.data.production_by_month:
        y_vals.append(row[0])
        x_vals.append(row[1])

    curve = Qwt.QwtPlotCurve("Barrels (in thousands)")
    curve.attach(plot)
    curve.setData(x_vals, y_vals)

    plot.replot()

    return plot


def plot_production_by_state():
    """Show data in qwt plot"""

    plot = Qwt.QwtPlot()
    plot.setTitle("Oil Production by State")
    plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
    plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")

    # Need custom scale to set labels to month/year
    plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, view.TimeScaleDraw())

    hdf5 = tables.openFile(model.HDF5_FILENAME)

    x_vals = hdf5.root.data.production_by_state_month.cols.date[:]
    la_vals = hdf5.root.data.production_by_state_month.cols.la_barrels[:]
    tx_vals = hdf5.root.data.production_by_state_month.cols.tx_barrels[:]
    ak_vals = hdf5.root.data.production_by_state_month.cols.ak_barrels[:]
    ca_vals = hdf5.root.data.production_by_state_month.cols.ca_barrels[:]

    curve = view.create_curve('La', x_vals, la_vals, QtCore.Qt.green)
    curve.attach(plot)

    curve = view.create_curve('Tx', x_vals, tx_vals, QtCore.Qt.blue)
    curve.attach(plot)

    curve = view.create_curve('Ak', x_vals, ak_vals, QtCore.Qt.red)
    curve.attach(plot)

    curve = view.create_curve('Ca', x_vals, ca_vals, QtCore.Qt.yellow)
    curve.attach(plot)

    plot.insertLegend(Qwt.QwtLegend())
    plot.replot()

    return plot
