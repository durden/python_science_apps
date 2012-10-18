"""
View portion of sample app
"""

import datetime

from PyQt4 import QtGui
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


class StateProductionDialog(QtGui.QDialog):
    """Dialog to plot oil production by state"""

    def __init__(self, plot, parent):
        """init"""

        super(StateProductionDialog, self).__init__(parent)

        hlayout = QtGui.QHBoxLayout()
        hlayout.setMargin(0)
        hlayout.addWidget(plot)
        self.setLayout(hlayout)


def create_curve(title, xvals, yvals, color):
    """Helper to create a new curve with given data and color"""

    curve = Qwt.QwtPlotCurve(title)
    curve.setPen(QtGui.QPen(color))
    curve.setData(xvals, yvals)
    curve.setCurveType(Qwt.QwtPlotCurve.Yfx)
    curve.setStyle(Qwt.QwtPlotCurve.Lines)

    return curve
