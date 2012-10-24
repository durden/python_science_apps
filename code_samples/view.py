"""
View portion of sample app
"""

import datetime

from PyQt4 import QtGui, QtCore
import PyQt4.Qwt5 as Qwt


class TimeScaleDraw(Qwt.QwtScaleDraw):
    """Scale to display time values in month/year"""

    def label(self, value):
        """
        Convert time value into string-friendly label to be placed on a plot
        """

        super(TimeScaleDraw, self).label(value)

        date = datetime.datetime.fromtimestamp(value)
        return Qwt.QwtText((date.strftime("%b/%Y")))


class ProductionByMonthDialog(QtGui.QDialog):
    """Dialog to plot oil production by month"""

    def __init__(self, parent):
        """init"""

        super(ProductionByMonthDialog, self).__init__(parent)

        self._plot = Qwt.QwtPlot()

        self._plot.setTitle("Oil Production for USA by Month")
        self._plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
        self._plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")

        self._curve = Qwt.QwtPlotCurve("Barrels (in thousands)")
        self._curve.attach(self._plot)

        # Need custom scale to set labels to month/year
        self._plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, TimeScaleDraw())

        hlayout = QtGui.QHBoxLayout()
        hlayout.setMargin(0)
        hlayout.addWidget(self._plot)

        self.setLayout(hlayout)

    def loadData(self, x_vals, y_vals):
        """Load data into plot"""

        self._curve.setData(x_vals, y_vals)
        self._plot.replot()


class FilterTxProductionDialog(QtGui.QDialog):
    """Dialog to filter tx production data in/out"""

    #filter_str = QtCore.pyqtSignal(str)
        #self._txtbox.editingFinished.connect(
                        #lambda: self.filter_str.emit(str(self._txtbox.text())))

        #vlayout = QtGui.QVBoxLayout()
        #vlayout.setMargin(0)
        #vlayout.addWidget(self._label)
        #vlayout.addWidget(self._txtbox)

        #self.setLayout(vlayout)
    #self._label = QtGui.QLabel('Filter Tx Production')
    #self._txtbox = QtGui.QLineEdit()


class StateProductionDialog(QtGui.QDialog):
    """Plot production by state"""

    def __init__(self, parent):
        """init"""

        super(StateProductionDialog, self).__init__(parent)

        self._plot = Qwt.QwtPlot()

        self._plot.setTitle("Oil Production by State")
        self._plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
        self._plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")
        self._plot.insertLegend(Qwt.QwtLegend())

        # Need custom scale to set labels to month/year
        self._plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, TimeScaleDraw())

        self._la_curve = None
        self._ak_curve = None
        self._ca_curve = None
        self._tx_curve = None

        vlayout = QtGui.QVBoxLayout()
        vlayout.setMargin(0)
        vlayout.addWidget(self._plot)

        self.setLayout(vlayout)

    def loadData(self, state_abbr, x_vals, y_vals):
        """Load data into plot"""

        if state_abbr == 'la':
            self._la_curve = create_curve('La', x_vals, y_vals,
                                          QtCore.Qt.green)
            self._la_curve.attach(self._plot)

        elif state_abbr == 'tx':
            self._tx_curve = create_curve('Tx', x_vals, y_vals, QtCore.Qt.blue)
            self._tx_curve.attach(self._plot)
        elif state_abbr == 'ak':
            self._ak_curve = create_curve('Ak', x_vals, y_vals, QtCore.Qt.red)
            self._ak_curve.attach(self._plot)
        elif state_abbr == 'ca':
            self._ca_curve = create_curve('Ca', x_vals, y_vals, QtCore.Qt.yellow)
            self._ca_curve.attach(self._plot)
        else:
            raise ValueError('Invalid state')

        self._plot.replot()


def create_curve(title, xvals, yvals, color):
    """Helper to create a new curve with given data and color"""

    curve = Qwt.QwtPlotCurve(title)
    curve.setPen(QtGui.QPen(color))
    curve.setData(xvals, yvals)
    curve.setCurveType(Qwt.QwtPlotCurve.Yfx)
    curve.setStyle(Qwt.QwtPlotCurve.Lines)

    return curve
